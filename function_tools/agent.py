import requests
from typing import Dict, Any
from google.adk.agents import LlmAgent

def fetch_user_data(user_id: int) -> Dict[str, Any]:
    """
    Fetches user data from a placeholder API based on the provided user ID.
    
    This tool makes an HTTP GET request to the JSONPlaceholder API to retrieve user information.
    
    Args:
        user_id (int): The ID of the user to fetch data for(e.g: 1 to 10)
        
    Returns:
        Dict[str, Any]: A dictionary containing the user's data if the request is successful.
        otherwise a dictionary with an error message.
        The structure aligns with the JSONPlaceholder user data format.
    """
    
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        response.raise_for_status()
        user_data= response.json()
        if user_data:
            return {"status": "success", "user_data": user_data}
        else:
            return {"status": "error", "message": f"No user found with ID {user_id}"}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}
    
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}
    

def format_user_profile(user_data: Dict[str, Any]) -> str:
    """
    Formats user data into a readable profile string using markdown.
    
    This tool takes a dictionary of user data and formats it into a structured string that includes the user's name, email, address, and company information.
    with Markdownn for improved readability.
    
    Args:
        user_data (Dict[str, Any]): A dictionary containing user information, expected to have keys like 'name', 'email', 'address', and 'company'.
                                    Typically the 'user_data' field from the output of 'fetch_user_data' tool.
                                    
    Returns:
        str: A Multi line formatted string representing the user's profile, including their name, email, address, and company details.
             Returns an error message if the input data is not in the expected format or if input data is invalid.
    """
    print(f" [Tool Call] format_user_profile called with input: {user_data}")
    user_data_string = user_data

    if not isinstance(user_data_string, dict):
        return "Error: Invalid input format. Expected a dictionary containing user data."
    
    name= user_data_string.get("name", "N/A")
    username = user_data_string.get("username", "N/A")
    email = user_data_string.get("email", "N/A")
    phone= user_data_string.get("phone", "N/A").split(" ")[0]

    website = user_data_string.get("website", "N/A")
    company_name= user_data_string.get("company", {}).get("name", "N/A")
    city= user_data_string.get("address", {}).get("city", "N/A")

    markdown_profile_string =(
        f"## User Profile: {name})\n"
        f"- **Username:** {username}\n"
        f"- **Email:** {email}\n"
        f"- **Phone:** {phone}\n"
        f"- **Website:** {website}\n"
        f"- **Company:** {company_name}\n"
        f"- **City:** {city}"
    )

    return markdown_profile_string


root_agent = LlmAgent(
    name= "UserProfileAgent",
    model="gemini-2.5-flash",
    instruction ="""You are a user profile agent that fetches user data based on a provided user ID and formats it into a readable profile string.
    
    **Tools Available**
    
    1. fetch_user_data(user_id: int) -> Dict[str, Any]: Fetches user data from an API based on the provided user ID.
    2. format_user_profile(user_data: Dict[str, Any]) -> str: Formats the fetched user data into a structured profile string.
    
    **Task**
    
    Given a user ID, use the 'fetch_user_data' tool to retrieve the user's information. 
    If the data is successfully retrieved, pass the relevant user data to the 'format_user_profile' tool to create a formatted profile string.
    If there are any errors during data fetching or formatting, return the error message instead.
    
    Output *only* the final formatted user profile string. Do not include any other text in your response.""",
    description="An agent that fetches user data based on a provided user ID and formats it into a readable profile string.",
    tools=[fetch_user_data, format_user_profile]
)

