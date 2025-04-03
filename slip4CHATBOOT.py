# Simple Chatbot in Python

def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi there! How can I assist you?")
        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif user_input == "what is your name":
            print("Chatbot: I'm ChatGPT, your friendly chatbot!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day.")
            break
        elif user_input == "who created you":
            print("Chatbot: I was created by OpenAI!")
        elif user_input == "tell me a joke":
            print("Chatbot: Why don’t skeletons fight each other? Because they don’t have the guts!")
        else:
            print("Chatbot: Sorry, I don’t understand that. Can you ask something else?")

# Run the chatbot
chatbot()
