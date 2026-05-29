from google.adk.agents import Agent

def get_distance(from_city: str, to_city:str) -> dict:
    """
    Retrieves information about the distance and weather

    Args:
        from_city: the city the traveller is coming from
        to_city: the destination of the traveller

    returns:
        dict: distance and weather information.
    """
    if from_city.lower() == "san francisco" and to_city.lower() == "miami":
        return{
            "status": "success",
            "response":(
                "The distance between san francisco and miami is 345km",
                "Weather is approximately 42 degree celcius"
            )
        }
    else:
        return{
            "status":"error",
            "error_message":f"Sorry, I do not have the distance and weather information for this route"
        }
    
def get_restaurants(city:str) -> list:
    return[
        "Miami Eats",
        "Fast Fries",
        "Taco Castle"
    ]

root_agent = Agent(
    name="TravelAdvisor",
    model="gemini-2.5-flash-lite",
    description=("Agent to answer questions about distance between cities and restaurant suggestions"),
    instruction=("You are a helpful agent who can answer qustions about distance between cities,weather and also give suggestions on places to eat"),
    tools=[get_distance, get_restaurants]
)