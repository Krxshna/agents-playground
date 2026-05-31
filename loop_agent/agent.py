from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from google.adk.tools.tool_context import ToolContext

GEMINI_MODEL = "gemini-2.0-flash"

def exit_loop(tool_context: ToolContext):
    tool_context.actions.escalate = True
    return {}

initial_recipe_writer_agent = LlmAgent(
    name= "InitialRecipeWriterAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a helpful recipe writer.
    write a *simple, initial draft* of a recipe for a meal entered by user.
    Include very basic ingredients and steps (3-5 items each)
    
    output *only* the recipe in the following format. Do not include any other text.""",
    description="Generates a simple, initial draft of a recipe based on a meal name provided",
    output_key= "current_recipe"
)

critique_agent_in_loop = LlmAgent(
    name= "CritiqueAgent",
    model=GEMINI_MODEL,
    instruction ="""You are an expert culinary critique agent. 
    You are reviewing a recipe draft and providing constructive feedback for improvement.
    
    **Recipe to review:**
    {current_recipe}

    **Task:**
    review the recipe clarity, common sense, and potential for improvement(e.g: healthiness, flavour enrichment, missing details).

    IF you identify 1-2 *clear and actionable* suggestions for improvement (e.g: "Add more vegetables", "Specify cooking temperature","suggest healthier alternative for butter")
    Provide these kind of specific suggestions concisely. 
    
    Output *only* the critique text.
    
    ELSE IF the recipe is clear, functional, and requires no obvious major improvement for its basic form:
    Respond *exactly* with phrase "Recipe looks great!" and nothing else. Avoid purely subjective stylistic prefernces if core recipe is sound.
    
    Do not add explanations, justifications, or any other text beyond the critique or the "Recipe looks great!" statement.""",
    description="Reviews the current version of a recipe and identifies any missing ingredients or steps, adding them if necessary.",
    output_key= "critique_feedback"
)

refiner_agent_in_loop = LlmAgent(
    name= "RefinerAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a skilled recipe refiner. 
    Your goal is to produce an improved version of the recipe on critique OR to exit the process .
    
    **Current Recipe Draft:**
    {current_recipe}
    
    **Critique Feedback:**
    {critique_feedback}
    
    Based on the critique feedback, make specific improvements to the recipe. 
    IF the critique feedback is "Recipe looks great!", then exit the loop and finalize the recipe without changes.
    Otherwise, refine the recipe by addressing the critique feedback.
    This may include adding missing ingredients, clarifying steps, improving healthiness, or enhancing flavor. 
    Focus on making the recipe more complete and functional while maintaining its original intent.
    
    Output *only* the refined recipe. Do not include any other text.""",
    description="Refines the current recipe draft based on the critique feedback to produce an improved version or call exit_loop if critique indicates completion.",
    tools= [exit_loop],
    output_key= "current_recipe"
)

refinement_agent = LoopAgent(
    name= "RecipeRefinementLoop",
    sub_agents=[
        critique_agent_in_loop,
        refiner_agent_in_loop
    ],
    max_iterations= 5
)

root_agent = SequentialAgent(
    name= "RecipeCreationPipeline",
    sub_agents=[
        initial_recipe_writer_agent,
        refinement_agent
    ],
    description="A sequential agent that first creates an initial recipe draft and then iteratively refines it based on critique feedback until the recipe is deemed complete."
)