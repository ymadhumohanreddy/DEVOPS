import google.generativeai as genai


API_KEY = ""
genai.configure(api_key=API_KEY)

def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text 

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_gemini(user_input)
        print("Chatbot:", response)
