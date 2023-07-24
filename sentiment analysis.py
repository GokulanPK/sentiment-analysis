from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
recogonizer=sr.Recognizer()
with sr.Microphone() as source:
    print("clearing background noise ")
    recogonizer.adjust_for_ambient_noise(source,duration=1)
    print('waiting for your message')
    recordedaudio=recogonizer.listen(source)
    print('Done recording')

try:
    print('printing the message..')
    text=recogonizer.recognize_google(recordedaudio,language='en-US')
    print('your message:{}'.format(text))
except Exception as ex:
    print(ex)


Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v)