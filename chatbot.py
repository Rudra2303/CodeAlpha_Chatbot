def get_bot_response(user_input):
    """
    Function to determine the bot's response based on user input.
    """
    # Normalize input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that."

def start_chatbot():
    """
    Main function to run the chatbot loop.
    """
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        # Get input from the user
        user_text = input("You: ")

        # Get the response from our logic function
        response = get_bot_response(user_text)
        print(f"Chatbot: {response}")

        # Break the loop if the user says bye
        if "bye" in user_text.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()