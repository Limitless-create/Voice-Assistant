import speech_recognition as sr   
import webbrowser                 
import pyttsx3                    
import musiclibary               
import partlibary
import requests                   
from bs4 import BeautifulSoup      

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_google(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"  
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }  
    response = requests.get(url, headers=headers)  
    soup = BeautifulSoup(response.text, 'html.parser') 

    
    results = []
    for item in soup.find_all('div', class_='tF2Cxc'):  
        title = item.find('h3').text if item.find('h3') else 'No title available'
        link = item.find('a')['href'] if item.find('a') else 'No link available'
        description = item.find('span', {'class': 'aCOpRe'}).text if item.find('span', {'class': 'aCOpRe'}) else 'No description available'
        results.append((title, description, link))
    
    return results

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        s = c.lower().split(" ")[1]
        link = musiclibary.music[s]
        webbrowser.open(link)
    elif c.lower().startswith("song"):
        cu = c.lower().split(" ")[1]
        link = partlibary.clip[cu]
        webbrowser.open(link)
    elif "news" in c.lower():
        webbrowser.open("https://bengali.abplive.com/live-tv")
    elif "search" in c.lower(): 
        search_query = c.lower().replace("search", "").strip()
        speak(f"Search {search_query}")
        results = ask_google(search_query)

        # Output the top result
        if results:
            top_result = results[0]
            title, description, link = top_result
            speak(f"Here is what I found: {title}. {description}. Opening the link now.")
            webbrowser.open(link)
        else:
            speak("Sorry sir, I couldn't find any results.")
    else:
        speak("Sorry sir, I don't understand that command.")

if __name__ == "__main__":
    speak("Initialization!!!  ...........")
    while True:
        
        print("Recognizing.......")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=1)
            command = recognizer.recognize_google(audio)
            
            if command.lower() in ["jarvis", "hello", "hi", "buddy"]:
                speak("hello sir! I am jarvis. How can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis active.....")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)
            print(command)
        
        except Exception as e:
            print(f"Error: {e}")
