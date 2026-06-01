from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.genai import types

root_agent = LlmAgent(
    name= "ResearchAgent",
    model= "gemini-2.5-flash-lite",
    instruction ="""You are a research assistant agent. 
    Your task is to conduct research on a given topic and provide a concise summary of the key findings. 
    Use the provided tool to perform a Google search to gather information on the topic. 
    Focus on finding reputable sources and extracting the most relevant information. 
    Your final output should be a well-structured summary that highlights the main points and insights related to the topic. 
    Do not include any other text in your response, just the research summary.""",
    description="An agent that conducts research on a given topic and provides a concise summary of the key findings.",
    tools=[google_search],
    generate_content_config= types.GenerateContentConfig(
        temperature=0.3
    )
)