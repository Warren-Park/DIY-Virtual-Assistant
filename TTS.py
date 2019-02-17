import requests, time,subprocess
import pyaudio
import wave

class AudioFile:
    """
    https://stackoverflow.com/questions/6951046/pyaudio-help-play-a-file
    Plays an audio file.
    """
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Plays audio """
        data = self.wf.readframes(self.chunk)
        while data!='' and data!=None and data!=b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Close the file """
        self.stream.close()
        self.p.terminate()



def TTS(text,credential):
    """Converts text into a voice."""
    #Based on https://github.com/Azure-Samples/Cognitive-Speech-TTS/blob/master/Samples-Http/Python/TTSSample.py
    subscription_key, service_region = credential[0],credential[1]
    fetch_token_url = "https://"+service_region+".api.cognitive.microsoft.com/sts/v1.0/issueToken"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)

    base_url = 'https://'+service_region+'.tts.speech.microsoft.com/'
    path = 'cognitiveservices/v1'
    url = base_url + path
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'User-Agent': credential[2]
    }
    xml = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-GB'>"
    xml+= "<voice name='Microsoft Server Speech Text to Speech Voice (en-GB, George, Apollo)'>"
    xml+=text
    xml+="</voice></speak>"

    response = requests.post(url, headers=headers, data=xml)

    if response.status_code==200:
        filename = str(time.time())+".wav"
        with open(filename, 'wb') as audio:
            audio.write(response.content)
        print(text)
        aud = AudioFile(filename)
        aud.play()
        aud.close()
        subprocess.call(["rm",filename])
    else:
        raise IOError("Microsoft Speech does not respond.")
