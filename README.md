# DIY-Virtual-Assistant
This is a DIY Virtual Assistant application that utilises Microsoft Cognitive Speech API and QnA Maker API.

## What does it do?
A demo video is available on https://youtu.be/paWdhAfJo9s
This is a template application that a developer can write a question-answer pair to build a new virtual assistant application.


## How to use?
Clone the repository and fill in the credentials in the main.py. Credentials can be generated by creating a Microsoft Cognitive Speech API and Microsoft QnA Maker API. You also need to register a knowledge base (question-answer pair) on the QnA Maker API website. Detailed instructions for each service are given below:
- Speech API: https://azure.microsoft.com/en-gb/services/cognitive-services/speech-services/
- QnA Maker API: https://www.qnamaker.ai

You also need to install Python 3 and following Python packages which can be installed using pip:
- azure-cognitiveservices-speech
- wave
- pyaudio (requires portaudio to be installed on your machine.)
(For example, you can install them by typing:
  pip3 install azure-cognitiveservices-speech,wave,pyaudio
  on the command line interface)

If you have obtained keys, then, on the command line interface, cd to the directory that the cloned files are stored and type: python3 main.py
