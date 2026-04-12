from actions import open_google, search_google, close_browser,open_make_my_trip

def process_command(command: str):
    command = command.lower()

    if "open google" in command:
        open_google()
        return "Opened Google"

    elif "search" in command:
        query = command.replace("search", "").strip()
        search_google(query)
        return f"Searched for {query}"

    elif "flight" in command:
        open_make_my_trip()
        return "Opened flight booking site"
    
    elif "close" in command:
        return close_browser()

    else:
        return "Sorry, I don't understand this command"