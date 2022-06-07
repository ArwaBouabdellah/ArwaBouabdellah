import pyttsx3 
import datetime 
import speech_recognition as sr   
import wikipedia   
import smtplib   
import  webbrowser as wb  

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    time=datetime.datetime.now().strftime("%H heure: %M minutes et %S secondes") #for 12 hours oclock
    #time= datetime.datetime.now().strftime("%I : %M: %S")  #For 24hours
    speak("l'heure actuelle est :" )
    speak(time)

def date_():
    year= datetime.datetime.now().year
    month= datetime.datetime.now().month
    day= datetime.datetime.now().day
    speak("la date actuelle est :")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Bienvenue Arwa!")

    heure= datetime.datetime.now().hour
    if (heure>=6) and (heure<12) :
         speak("Bonjour Mme !")
    elif heure>=12 and heure<18:
        speak("Bon Midi Mme !")
    elif heure>=18 and heure<24:
        speak("Bonne après-midi Mme !")
    else:
        speak('Bonne nuit Mme !')
    speak ("Sizi à votre service. Comment je peux vous aider?")

def PrendreCommande():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Écoute en cours....")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Reconnaître.....")
        query = r.recognize_google(audio, language= 'fr-France')
        print(query)
    except Exception as e:
        print(e)
        print("Répétez, s'il vous plaît......")
        return "None"
    return query

def EnvEmail(to, content):
        server= smtplib.SMTP('smtp.gmail.com', 587)   #587 le port qui ne convient à aucun type de server
        server.ehlo()  #pour nous nous identifier.
        server.starttls()  #la connexion entre le user et le server
        server.login('username@gmail.com', 'password')
        server.sendmail('username@gmail.com', to, content)


if __name__ == '__main__':
    wishme()
    while True:
        query = PrendreCommande().lower()
        if 'temps' in query:
            time_()         
        elif 'date' in query:
            date_()          
        elif 'stop' in query:
            quit()          
        elif 'wikipédia' in query:
            speak('Cherche en cours....')
            query= query.replace('wikipedia', '')
            result=wikipedia.summary(query, sentences=3)
            speak('selon wikipedia :')
            print(result)
            speak(result)
        elif 'envoyer un email' in query:
            try:
                speak('Quoi le content?')
                content= PrendreCommande()   
                speak('qui est le destinataire? ')

                receiver= input("entrer l'email du destinataire: ")
                to= receiver
                EnvEmail(to,content)
                speak(content)
                speak('Email envoyé ')

            except Exception as e:
                print(e)
                speak('Email non envoyé')
        elif 'chercher dans chrome' in query:
               speak('quoi chercher?')
               chromepath= 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome'
               cherche= PrendreCommande().lower()
               wb.get(chromepath).open_new_tab(chercher+'.com')   #ouvrir seulement les sites avec .com a la fin
