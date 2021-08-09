# Project_AI_smartmethods_chatbot_voice-ar

It's Celine Voice Assist's smart methods of helping, welcoming, and delivering company services and can be programmed to do more.

# Used libraries:

import the library

pyjokes

speech_recognition as sr

webbrowser

time

playsound

os

random

ctime

gTTS


# Its current capabilities:

Introduce herself and remember the name of the speaker.

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

# 2: She can receive and respond to greetings.


 # 2: التحية=Greeting
    if there_exists([" هلا  "," سلام  ","  السلام عليكم "," مرحبا"]): 
        smartmethods_speak(f"  أهلا وسهلا ومرحبا بك في شركة الأساليب الذكية , كيف أساعدك؟ ")

    if there_exists(["كيف حالك","ما أخبارك","شخبارك","كيف هي أحوالك"]):
        smartmethods_speak(f"الحمدلله أنا بأفضل حال  ,  شكرا لسؤالك , وأنت كيف حالك؟ {person_obj.name}")

    if there_exists(["بأفضل حال ","أشكر الله ","بخير ","الحمدلله"]):
        smartmethods_speak(f"    إن شاء الله دائماً   {person_obj.name}  كيف أساعدك؟")

# 3: She can help you with services.


# 3: الخدمات=Serves 
    if there_exists([" ماذا تفعلين ","ماهي خدماتك  "," ماذا تقدمين لي","ماذا تصنعين"]):
        smartmethods_speak(f"  أنا هنا للترحيب بكم بإسم شركة الأساليب الذكية ")
        
        
# 4: She can reply thanks.       
        
# 4: الشكر= Thanks        
    if there_exists(["  أشكرك "," شكرا جزيلا  "," شكرا  "," شكراً لك"]):
        smartmethods_speak(f" العفو أنا هنا لخدمتكم , نحن الذين نشكرك لحضوركم الكريم {person_obj.name}  ")

# 5: She can tell a joke.

# 5: نكتة = Joke  
    if ' نكتة ' in voice_data:
        smartmethods_speak(pyjokes.get_joke())

# 6: She can introduce the company.

# 6: تعريف بالشركة = Company Introduction
    if there_exists(["  من هي شركة الأساليب ","  ماذا تصنع الأساليب الذكية  ","  ماخدمات الأساليب الذكية "," من هي الأساليب الذكية "]):
        smartmethods_speak(f" شركة الأساليب الذكية مؤسسة وطنية سعودية متخصصة في مجال الروبوت والذكاء الصناعي ونفخر بحصولنا على تصنيف فوربس كواحدة من أكثر الشركات ابداعا ونفخر أيضا بترشيحنا من قبل المنشئات كواحدة من أكثر الشركات ابتكارا في عام 2020 ")


# 7: She can search in Google, YouTube and Google Map.

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
        
# 8: She can stop.

# 8:  إغلاق= Close
    if there_exists([" وداع  "," إغلاق  "," توقفي  ","إلى اللقاء"]):
        smartmethods_speak(f"   حسنا إلى اللقاء وليس وداعاً , أراك بخير {person_obj.name} ")
      
