def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! How can I help you?"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day."
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple chatbot built with Python!"
    else:
        return "Sorry, I didn't understand that."


def start_chat():
    print("🤖 Chatbot: Hello! Type something to chat. Type 'bye' to exit.")
    
    while True:
        user_message = input("🧑 You: ")
        response = chatbot_response(user_message)
        print("🤖 Chatbot:", response)

        if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
            break


start_chat()
