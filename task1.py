def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but thanks for asking! How can I help you?")
        
        elif "what is your name" in user_input:
            print("Chatbot: I'm a simple chatbot created for demonstration purposes.")
        
        elif "help" in user_input:
            print("Chatbot: Sure! What do you need help with?")
        
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()
#this is the last line of my work