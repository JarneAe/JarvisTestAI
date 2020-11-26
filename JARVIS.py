import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia



warnings.filterwarnings('ignore')

#records audio and returns it as a string
def recordAudio():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('Say something...')
        audio = r.listen(source)

    data = ''

    try:
        data = r.recognize_google(audio)
        print('You said: ' +data)
    except sr.UnknownValueError: 
        print('Google Speech Recognition could not understand you, you dumbass')
    except sr.RequestError as e:
        print('Request results from Google Speech service error'+ e)
    return data

def assistantResponse(text):

    print(text)

    myobj = gTTS(text= text, lang='eng', slow=False)

    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['wake up daddy\'s home' , 'hey jarvis' , 'wake up jarvis']
    
    inputw = text.lower()

    for phrase in WAKE_WORDS:
        if inputw in phrase:
            return True
    
    return False


def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day


    month_names = ['January', 'February', 'March','April','May','June','July','August','September','October','November','December']
    ordinalnumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
 
    return 'Today is ' +weekday+' ' + month_names[int(monthNum) - int(1)]+' the ' + ordinalnumbers[int(dayNum) - int(1)]+ '. '  


def greeting():
    GREETING_INPUTS = ['hi','hello','hey','greetings','wassup']

    GREETING_RESPONSES = ['howdy','what\'s up','Hello there','']

    for Word in text.split():
        if Word.lower in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '. '

    return ' '
 

def getPerson(text):
     wordlist = text.split()

     for i in range(0, len(wordlist)):
         if i + 3 <= len(wordlist) - 1 and wordlist[i].lower() == 'who' and wordlist[i+1].lower() == 'is':
             return wordlist[i+2] + ' '+wordlist[i+3]

def sendFunction(text, foundWakeWord):
    if foundWakeWord != True:
        print("You said: " + text)
    else:
        print("Welcome sir")

    text = recordAudio()


while True:
    text = recordAudio()
    # response = ''

    foundWakeWord = wakeWord(text)
    sendFunction(text, foundWakeWord)