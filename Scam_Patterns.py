import openai
import speech_recognition as sr
import threading

# Function to initialize OpenAI API
def init_openai(api_key):
    openai.api_key = api_key

# Function to analyze the conversation
def analyze_conversation(conversation_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an FBI agent who can understand the most likely patterns in financial scam calls. You will sort out important data like the name of the person, the company they are associated with, and all other information that could help track or identify if the person is legit by running a background check. You will also provide time-to-time suggestions to the user to handle the situation wisely."},
            {"role": "user", "content": conversation_text}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to generate follow-up questions
def generate_follow_up(conversation_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You generate follow-up questions to help identify scams."},
            {"role": "user", "content": conversation_text}
        ]
    )
    return response['choices'][0]['message']['content']


# Function to suggest next steps
def suggest_next_steps(conversation_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You suggest safe actions to take in a potential scam situation."},
            {"role": "user", "content": conversation_text}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to handle speech recognition
def listen_and_analyze(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)


    try:
        conversation_text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {conversation_text}")

        # Analyze the conversation
        analysis = analyze_conversation(conversation_text)
        print("Analysis: ", analysis)

        # Generate follow-up questions
        follow_up = generate_follow_up(conversation_text)
        print("Follow-Up Questions: ", follow_up)

        # Suggest next steps
        next_steps = suggest_next_steps(conversation_text)
        print("Next Steps: ", next_steps)

    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")

# Function to start listening when "Enter" is pressed
def start_listening(api_key):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        input("Press Enter to start recording and analyzing...")
        listen_and_analyze(recognizer, microphone)

# Main function to set up and run the real-time monitoring
def run_real_time_monitoring(api_key):
    init_openai(api_key)
    print("Press 'Enter' to start recording and analyzing...")

    listening_thread = threading.Thread(target=start_listening, args=(api_key,))
    listening_thread.start()

# Example usage
if __name__ == "__main__":
    api_key = ""  #add api key 
    run_real_time_monitoring(api_key)
    
