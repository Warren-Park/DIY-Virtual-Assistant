import azure.cognitiveservices.speech as speechsdk
def STT(credential):
    """RECOGNISES human voice and convert the speech into a text
    https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python
    """


    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = credential[0],credential[1]
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("I'm listening...")

    # Performs recognition. recognize_once() returns when the first utterance has been recognized,
    # so it is suitable only for single shot recognition like command or query. For long-running
    # recognition, use start_continuous_recognition() instead, or if you want to run recognition in a
    # non-blocking manner, use recognize_once_async().
    try:
        result = speech_recognizer.recognize_once()
    except:
        raise Exception("Cancelled the task.")

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        raise ValueError("You did not speak.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        raise BlockingIOError("Speech Recognition canceled.")