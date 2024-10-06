# Real-Time Scam Detection using OpenAI and Speech Recognition

This Python project analyzes real-time conversations, identifying potential scams using OpenAI's GPT-4 model. The application listens to audio input through speech recognition and provides analysis, follow-up questions, and suggestions for safe actions in case of a scam call.

## Features

- **Speech Recognition**: Uses `speech_recognition` to capture audio in real time.
- **Conversation Analysis**: Integrates OpenAI's GPT-4 to analyze the text of the conversation.
- **Follow-up Questions**: GPT-4 generates follow-up questions to further identify scams.
- **Safety Suggestions**: Provides suggestions on how to safely handle potential scam calls.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/scam-call-detector.git
   cd scam-call-detector
   ```

2. Install the required dependencies:

```bash
pip install openai SpeechRecognition
```
Add your OpenAI API key, you can get it from openai dashboard.

Open the main.py file and insert your OpenAI API key where indicated:

```python
api_key = "your_openai_api_key"
```
## Usage
Run the script:

```bash
python main.py
```
Press "Enter" to start recording your conversation.

The system will:

Transcribe the audio using Google Speech Recognition.
Analyze the conversation using OpenAI's GPT-4.
Provide follow-up questions to identify the scam.
Suggest safe actions based on the context.



## Dependencies
openai - For GPT-4 based analysis.
speech_recognition - For capturing and transcribing real-time audio.
Install all dependencies using:

```bash
pip install openai speech_recognition
```


## Contributors 
Aditya - @aditya10avg
Dev Rai- @dev-rai1
Nuhayd 
