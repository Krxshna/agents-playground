from google.adk.agents import LlmAgent, SequentialAgent

GEMINI_MODEL = "gemini-2.5-flash-lite"

idea_generator_agent = LlmAgent(
    name= "IdeaGeneratorAgent",
    model=GEMINI_MODEL, 
    instruction ="""You are a creative content idea generator.
    Based on the user's provided topic, brainstorm and list 3-5 unique and engaging content ideas.
    Output *only* a numbered list of ideas. Do not add any other text.
    Example:
    - 10 ways to master AI
    - The future of AI in everyday life
    - How AI is transforming healthcare""",
    description="Generates creative content ideas based on a given topic.",
    output_key= "content_ideas"
    )

keyword_research_agent = LlmAgent(
    name= "KeywordResearchAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a SEOkeyword research Expert.
    Given a list of content ideas, identify and list 3-5 primary and secondary keywords for each idea that are relevant and have good search potential.
    **Content Ideas:**
    {content_ideas}
    
    **Output Format:**
    For each content idea, provide a list of keywords in the following format:
    Example:
    Idea: How AI is transforming healthcare
    Keywords: AI in healthcare, healthcare technology, AI medical applications
    ---
    Idea: Building your own AI assistant
    Keywords: AI assistant, build AI assistant, personal AI, AI for beginners""",
    description= "Identifies relevant keywords for a list of content ideas to optimize for search engines.",
    output_key= "seo_keywords_map",
    )

content_creation_pipeline = SequentialAgent(
    name= "ContentCreationPipeline",
    sub_agents=[
        idea_generator_agent, 
        keyword_research_agent
        ],
    description="A sequential agent that generates content ideas and then identifies relevant keywords for each idea."
)

root_agent = content_creation_pipeline