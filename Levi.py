## Main Script for Levi program Final Project COSC 072
## Implements Google API's for speech to text Mac OS for text to speech
## Implements a vector analysis of speech to text data to answer questions/respond
# perform functionality.
#Luke Hudspeth COSC 072
# Using Python 3.0
# for weather https://pypi.org/project/weather-api/

import sys
import os
import speech_recognition as sr
from gtts import gTTS
import time
from question_processor import *
from weather import Weather, Unit
import webbrowser



r = sr.Recognizer()
mics = sr.Microphone.list_microphone_names()

#check to make sure correct mic is entered here, this is for Mac OS
microphone_id = mics.index(u'Built-in Microphone')

#buffer to store bytes of data
CHUNK_SIZE = 2048


#how often data is recorded
SAMPLE_RATE = 48000


global RESPOND
RESPOND = False

def Levi():
    global RESPOND
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    with sr.Microphone(microphone_id, SAMPLE_RATE, CHUNK_SIZE) as source:

        #built in function to adjust for background noises
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            words = text.split()



            #shut down
            if "quit" in words:
                text_to_speech("Goodbye")
                return False


            valid_command = False




            #only pick up on things that contain "Levi" or if engaged in response sequence
            if "Levi" in words or RESPOND == True or "Levi's" in words:
                text = text.replace("Levi's", "Levi")
                print "\""+text+"\""
                valid_command = True


            #process question to determine what user meant for Levi to do
            if valid_command == True:
                function = question_processor(text).answer_questions()

                #print function


                if function == "music.txt":
                    music()
                elif function == "greetings.txt":
                    greet()
                elif function == "naming.txt":
                    RESPOND = False
                    respond(words)
                elif function == "datetime.txt":
                    date_time()
                elif function == "weather.txt":
                    weather()
                elif function == "none":
                    text_to_speech("Sorry, I didn't understand")
                elif function == "google.txt":
                    google(words)
                elif function == "spanish.txt":
                    spanish()




        # error occurs when google could not understand what was said
        except sr.UnknownValueError:
            print ("Did you say something?")


        except sr.RequestError as e:
            print ("Could not request results from Google Speech Recognition service; {0}".format(e))
    #
    os.dup2(old_stderr, 2)
    os.close(old_stderr)

    return True


def spanish():
    string = "Si, hablo espanol. Es un placer a servirle"
    os.system("say -v Juan -r 0.7 " + string)
    print "Levi: " + string


# https://stackoverflow.com/questions/38459894/opening-google-searches-with-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
def google(words):
    search = []

    start_words = ["Google", "search", "open"]
    for i in range(len(words)):
        if words[i] in start_words:
            #assume the search will be whatever the user says after a start_word
            search = words[i+1:len(words)]
    print search
    text = ""
    for word in search:
        text += " " + word


    print text
    url = "https://www.google.com.tr/search?q={}".format(text)
    webbrowser.open_new_tab(url)

#https://pypi.org/project/weather-api/
def weather():

    weather = Weather(unit=Unit.FAHRENHEIT)

    location = weather.lookup_by_location('Hanover, NH')
    condition = location.condition
    text_to_speech("The weather in Hanover, NH looks " +condition.text+ " and is " +str(condition.temp) +" degrees Fahrenheit.")


#output the date and time
def date_time():
    time_now = time.localtime()
    date = time_now.tm_mday
    month = time_now.tm_mon
    year = time_now.tm_year
    hours = time_now.tm_hour
    minutes = time_now.tm_min
    text_to_speech("Today is: " + str(month) + "-" + str(date) + "-" + str(year) + " and the time is: " + str(hours) + ":" +str(minutes))



#responding to a name
def respond(words):
    name = ""
    for word in words:
        for letter in word:
            if letter.isupper():
                name = word

    if name != "":
        text_to_speech("Hello " + name + " nice to meet you, how can I help?")
    else:
        text_to_speech("Sorry, I didn't catch that, how can I help you?")



#greeting sequence
def greet():
    global RESPOND
    text_to_speech("Hello, my name is Levi, what is yours?")
    RESPOND = True


#small function either for mac OS or other, to convert text to speech.
def text_to_speech(text):

    # apple os version
    # playing audio out with voice of Lee, and speed of 0.7 normal
    print "Levi: " + text
    if sys.platform == "darwin":
        os.system("say -v Lee -r 0.7 " + "\""+text+"\"")
    else:
        #google api version
        tts = gTTS(text,'en-uk')
        tts.save("parts/test.mp3")
        os.system("afplay parts/test.mp3")





#function to play music
def music():
    text_to_speech("Okay, I'm going to play you my favorite song")
    time.sleep(1)
    os.system("(afplay parts/TheLionSleepsTonight.mp3&)")
    time.sleep(15)
    os.system("killall afplay")









#starting sequence
text_to_speech("Hello, I am Levi, a 'semi' intelligent A-I. Please say my name then what you \n would like me to do")
#print ("Hello, I am Levi, a 'semi' intelligent A-I. Please say my name then what you \n would like me to do")

#run Levi program until user says "quit"
while Levi():
    None

