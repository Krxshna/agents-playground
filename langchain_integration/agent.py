from google.adk.agents import LlmAgent
from google.genai import types

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from google.adk.tools.langchain_tool import LangchainTool

wikipedia_api_wrapper = WikipediaAPIWrapper(
    top_k_results=1, 
    doc_content_chars_max=500
)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)

adk_wikipedia_tool = LangchainTool(tool= wikipedia_tool)

wikipedia_summerizer_agent = LlmAgent(
    name= "WikipediaSummarizerAgent",
    model= "gemini-2.5-flash-lite",
    instruction ="""You are a helpful assistant that provides concise summaries of Wikipedia articles. 
    When given a query, you will use the provided tool to search Wikipedia and retrieve relevant information. 
    Focus on providing factual informative without including unnecessary details. """,
    description="An agent that retrieves information from Wikipedia using a tool and generates concise summaries of the content.",
    tools=[adk_wikipedia_tool],
    generate_content_config= types.GenerateContentConfig(
        temperature=0.2
    )
)

root_agent = wikipedia_summerizer_agent