import process,STT,TTS
if __name__=="__main__":
    #NEED TO INSTALL azure-cognitiveservices-speech
    """This is a DIY Virtual Assistant."""
    credentials_speech = ("KEY1","REGION","NAME_OF_THE_RESOURCE_CREATED")
    credentials_qna = ("ENDPOINT KEY","KNOWLEDGE_BASE_ID","RESOURCE_HOST_NAME")

    try:
        while(True):
            TTS.TTS(process.process(STT.STT(credentials_speech),credentials_qna),credentials_speech)

    except KeyboardInterrupt:
        print("Program ended")
