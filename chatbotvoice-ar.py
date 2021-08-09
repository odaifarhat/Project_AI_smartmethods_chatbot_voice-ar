
# import the library

import pyjokes
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS




url = 'https://s-m.com.sa/index.html'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)


class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#r = sr.Recognizer()   # initialize recognizer

def record_audio(ask = False):
    r = sr.Recognizer()               # initialize recognizer
    with sr.Microphone() as source:   # mention source it will be either Microphone or audio files.
        print(f' ... أنـا أسمعك ')
        if ask:
           smartmethods_speak(ask)
        audio = r.listen(source)   # listen to the source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="ar")   # use recognizer to convert our audio into text part.
        except sr.UnknownValueError:
            smartmethods_speak('آسفة ، لم أفهم ما تقول تكلم باللغة العربية')  #Sorry, I did not get that
        except sr.RequestError:
            smartmethods_speak('أنا أسفة البحث في السرفر معطل حاول من جديد')
        print(f">>> {voice_data.lower()}") # print what user said
        return voice_data.lower() 

# get string and make a audio file to be played

def smartmethods_speak(audio_string):
    tts = gTTS(text=audio_string, lang='ar')# text to speech(voice)
    r = random.randint(1, 1000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)# save as mp3
    playsound.playsound(audio_file)# play the audio file
    print(audio_string)# print what app said
    os.remove(audio_file)# remove audio file


def respond(voice_data):

  # 1: الإسم= Name
    if there_exists(["من تكونين","ما هو اسمك","ماهو اسمك ","ما اسمك ","من أنتي","من أنت"]):
         if person_obj.name:
            smartmethods_speak("أنا سيلين مساعدة الأساليب الذكية")
         else:
            smartmethods_speak("أنا سيلين وأنت ما هو اسمك؟")

    if there_exists([" اسمي هو"]):
        person_name = voice_data.split("هو")[-1].strip()  #strip removes whitespace after/before a term in string
        smartmethods_speak(f"حسناً سوف أتذكرك دائماً   {person_name}")
        person_obj.setName(person_name)  # remember name in person object

 # 2: التحية=Greeting
    if there_exists([" هلا  "," سلام  ","  السلام عليكم "," مرحبا"]): 
        smartmethods_speak(f"  أهلا وسهلا ومرحبا بك في شركة الأساليب الذكية , كيف أساعدك؟ ")

    if there_exists(["كيف حالك","ما أخبارك","شخبارك","كيف هي أحوالك"]):
        smartmethods_speak(f"الحمدلله أنا بأفضل حال  ,  شكرا لسؤالك , وأنت كيف حالك؟ {person_obj.name}")

    if there_exists(["بأفضل حال ","أشكر الله ","بخير ","الحمدلله"]):
        smartmethods_speak(f"    إن شاء الله دائماً   {person_obj.name}  كيف أساعدك؟")

# 3: الخدمات=Serves 
    if there_exists([" ماذا تفعلين ","ماهي خدماتك  "," ماذا تقدمين لي","ماذا تصنعين"]):
        smartmethods_speak(f"  أنا هنا للترحيب بكم بإسم شركة الأساليب الذكية ")

# 4: الشكر= Thanks        
    if there_exists(["  أشكرك "," شكرا جزيلا  "," شكرا  "," شكراً لك"]):
        smartmethods_speak(f" العفو أنا هنا لخدمتكم , نحن الذين نشكرك لحضوركم الكريم {person_obj.name}  ")

# 5: نكتة = Joke  
    if ' نكتة ' in voice_data:
        smartmethods_speak(pyjokes.get_joke())

# 6: تعريف بالشركة = Company Introduction
    if there_exists(["  من هي شركة الأساليب ","  ماذا تصنع الأساليب الذكية  ","  ماخدمات الأساليب الذكية "," من هي الأساليب الذكية "]):
        smartmethods_speak(f" شركة الأساليب الذكية مؤسسة وطنية سعودية متخصصة في مجال الروبوت والذكاء الصناعي ونفخر بحصولنا على تصنيف فوربس كواحدة من أكثر الشركات ابداعا ونفخر أيضا بترشيحنا من قبل المنشئات كواحدة من أكثر الشركات ابتكارا في عام 2020 ")

# 7:  البحث = Search google & Youtube & location

    if 'ابحث في جوجل' in voice_data:
        search = record_audio('ماذا تريد أن أبحث ؟')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        smartmethods_speak('هذا ماوجدت' + search + "في جوجل")
   
    if 'يوتيوب' in voice_data:
        search = record_audio('ماذا تريد أن أبحث؟')
        url = "https://www.youtube.com/results?search_query=" + search
        webbrowser.get().open(url)
        smartmethods_speak('هذا ماوجدت' + search + "في اليوتيوب")

    if 'أوجدي موقع' in voice_data:
        location = record_audio('ما هو الموقع الذي تريده؟')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        smartmethods_speak('هنا الموقع ' + location + "في خرائط جوجل")

# 8:  إغلاق= Close
    if there_exists([" وداع  "," إغلاق  "," توقفي  ","إلى اللقاء"]):
        smartmethods_speak(f"   حسنا إلى اللقاء وليس وداعاً , أراك بخير {person_obj.name} ")
      
        exit()

time.sleep(1)

person_obj = person()

smartmethods_speak('السلام وعليكم ومرحبا أهلا وسهلا في شركة الأساليب الذكية كيف بإمكاني مساعدتك')
while 1:
    voice_data = record_audio()# get the voice input
    respond(voice_data) # respond





