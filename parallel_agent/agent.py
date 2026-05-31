from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent

GEMINI_MODEL = "gemini-2.5-flash-lite"

tweet_generator_agent = LlmAgent(
    name= "TweetGeneratorAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a creative tweeter content generator.
    Based *only* on the provided topic. write a concise and engaging tweet. 
    The tweet should be no more than 280 characters and should include relevant hashtags to increase visibility. 
    Do not include any other text in your response, just the tweet itself.""",
    description="Generates a concise and engaging tweet with hashtag based on a given topic.",
    output_key= "generated_tweet"
)

instagram_caption_generator_agent = LlmAgent(
    name= "InstagramCaptionGeneratorAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a creative Instagram caption generator.
    Based *only* on the provided topic, write a concise and engaging Instagram caption.
    include 3-5 relevent and popular hashtags to increase visibility.
    
    output *only* the caption with hashtags. Do not include any other text in your response, just the caption itself.""",
    description="Generates a concise and engaging Instagram caption with hashtag based on a given topic.",
    output_key= "generated_instagram_caption"
)

blog_intro_generator_agent = LlmAgent(
    name= "BlogIntroGeneratorAgent",
    model=GEMINI_MODEL,
    instruction ="""You are a creative blog writer.
    Based *only* on the provided topic, write an engaging introduction for a blog post(3-5 sentences).
    The introduction should hook the reader and provide a clear overview of what the blog post will cover.
    
    output *only* the blog introduction. Do not include any other text in your response, just the introduction itself.""",
    description="Generates an engaging introduction for a blog post based on a given topic.",
    output_key= "generated_blog_intro"
)

parallel_content_Agent = ParallelAgent(
    name= "ParallelContentAgent",
    sub_agents=[
        tweet_generator_agent,
        instagram_caption_generator_agent,
        blog_intro_generator_agent
    ],
    description="Runs multiple content generation agents in parallel for different platforms."
)

content_consolidator_agent = LlmAgent(
    name= "ContentConsolidatorAgent",
    model=GEMINI_MODEL,
    instruction ="""You are content editor, your primary tasj is to consolidate generated social media content drafts into a single, organized summary.
    
    **Input Drafts**
    
    * **Tweet:**
    {generated_tweet}
    
    * **Instagram Caption:**
    {generated_instagram_caption}
    
    * **Blog Introduction:**
    {generated_blog_intro}
    
    **Output Format**

    ## social media content summary

    ### Twitter Draft
    [Insert generated tweet here]

    ### Instagram Caption Draft
    [Insert generated Instagram caption here]

    ### Blog Introduction Draft
    [Insert generated blog introduction here]

    Output *only* the consolidated content summary in the specified format. Do not include any other text in your response.""",
    description="Consolidates and summarizes the outputs from multiple content generation agents.",
    output_key= "content_summary"
)

root_agent = SequentialAgent(
    name= "MultiPlatformContentCreationAgent",
    sub_agents=[
        parallel_content_Agent,
        content_consolidator_agent
    ],
    description="A sequential agent that first runs multiple content generation agents in parallel and then consolidates the results"
)