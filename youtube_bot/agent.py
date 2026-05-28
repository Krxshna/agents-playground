from google.adk.agents import LlmAgent
from google.genai import types

def generate_niche_video_ideas(channel_niche:str,num_ideas:int = 3) -> list:
    """
    Generates creative video ideas tailored to a specific youtube channel niche.
    
    Args:
        Channel_niche (str): The primary topic or genre of YouTube
        Channel (e.g., 'tech reviews','cooking tutorials','gaming news').
        num_ideas (int): The number of videa ideas to generate.
        
    Returns:
        list: A list of strings representing unique video ideas."""
    if "tech reviews" in channel_niche.lower():
        ideas = [
            f"Top 5 Gadgets under $100 for {channel_niche} in 2026",
            f"Deep dive: The latest AI smartphone features",
            f"DIY Smart home setup guide for {channel_niche}",
            f"Budget gaming PC Build: max performance, min cost"
        ]
    elif "cooking tutorials" in channel_niche.lower():
        ideas = [
            f"Quick and easy 30min meals: {channel_niche} edition",
            f"Mastering Sourdough bread: a beginners guide",
            f"Global street food recipes you can make at home",
            f"Ultimate guide to meal prepping for the week"
        ]
    else:
        ideas = [
            f"Exploring the future of {channel_niche}",
            f"The ultimate guide to {channel_niche} basics",
            f"Behind the scenes of {channel_niche} creator",
            f"Top 10 tips for mastering {channel_niche}"
        ]
    return ideas[:num_ideas]

def get_channel_optimization_tips(channel_type:str) -> dict:
    """
    Provides general tips for improving a Youtube channels performance and reach.
    
    Args:
        channel_type (str): The type or category of the youtube channel (eg: 'vlog', 'education', 'entertainment').
        
    Returns: 
        dict: A dictionary containing optimization tips for various aspects.
    """
    tips = {
        "SEO": [
            "Use relevent keywords in titles, description, and tags.",
            "optimize video thumbnails for click-through rate.",
            "Create compelling video description with timestamps."
        ],
        "Engagement": [
            "Encourage comments and questions.",
            "Add end screens and cards to promote other videos.",
            "Respond to comments to build community."
        ],
        "Content Strategy": [
            "Analyze audience retention reports to understand viewer behaviour.",
            "Research trending topics in your niche.",
            "Maintain a consistent upload schedule."
        ]
    }
    return {"status":"success", "tips":tips}

root_agent = LlmAgent(
    name = "Youtube_Content_creator",
    model="gemini-2.5-flash-lite",
    description = (
        "An AI assistant designed to help Youtube creators generate video ideas and optimize their channel"
    ),
    instruction = (
        "You are helpful youtube expert, your goal is to provide creative video content ideas." 
        "these ideas should be based on channel niches and also offer advice for improving youtube channel performance."
        "The advice should include SEO, engagement and content strategy."
    ),
    tools = [generate_niche_video_ideas,get_channel_optimization_tips],
    generate_content_config = types.GenerateContentConfig(
        max_output_tokens=400,
        temperature=0.3
    )
)