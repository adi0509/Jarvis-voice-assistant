from gtts import gTTS  #for text to speech
import os 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import vlc 
from vlc import Instance
from random import shuffle
import time

language = 'en'


def speak(audio):
	myobj = gTTS(text=audio, lang=language, slow=False) 	
	myobj.save("welcome.mp3") 
	os.system("mpg123 welcome.mp3") 

def wishme():
	hour = 	int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning Sir")
	elif hour>=12 and hour<18:
		speak("Good Afternoon Sir")
	else:
		speak("Good Evening Sir") 
	# speak("I am Jarvis, How may I help you!")

def takeCommand():
	'''
		It takes microphone voice as an input and returns string as an Output
	'''
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recongnizing....")
		query = r.recognize_google(audio, language='en-in')
		print('User said: ', query)
	except Exception as e:
		print(e)
		print("Say it again please...")
		speak("Say it again please...")
		return "None"
	return query

# this class is used for playing song 
music_dir = '/home/adarsh/Adi/music'
class testVLC:
    def __init__(self):
        self.list1 = playlist
        self.Player = Instance('--loop')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        for music in self.list1:
            self.mediaList.add_media(self.Player.media_new(music_dir+'/'+music))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
        # self.Player.set_playback_mode(vlc.PlaybackMode.loop)
    def playPlaylist(self):
        self.listPlayer.play()
    def nextPlay(self):
        self.listPlayer.next()
    def pausePlaylist(self):
        self.listPlayer.pause()
    def stopPlaylist(self):
        self.listPlayer.stop()
playlist = os.listdir(music_dir)
shuffle(playlist)
test = testVLC()
test.addPlaylist()


if __name__ == "__main__":
    wishme()
    while True:		
        query = takeCommand().lower()

		#logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = "According to wikipedia " + wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'youtube' in query:
			if 'open' in query:
				webbrowser.open("https://youtube.com")
			else: 
				query = query.replace("youtube", "")
				query = query.replace("search", "")
				query = query.replace(" ", "+")
				print("search: ", query)
				webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif 'google' in query:
			if 'open' in query:
				webbrowser.open("https://google.com")
			else:
				query = query.replace("google", "")
				query = query.replace("search", "")
				query = query.replace(" ", "+")
				webbrowser.open("https://google.com/search?q="+query)
        elif ('quit' in query) or ('bye' in query):
            speak('Ok bye sir')
            break
        elif ('music' in query) or ('song' in query):
            if 'play' in query:
                # songs = os.listdir(music_dir)
                # print(songs)
                # os.system(os.path.join(music_dir, songs[0]))
                # os.system("mpg123 /home/adarsh/Adi/music/"+ songs[0])
                test.playPlaylist()      
                
            elif 'pause' in query:
                test.pausePlaylist()
            elif 'stop' in query: 
                test.stopPlaylist()
            elif 'next' in query:
                test.nextPlay() 
            elif 'resume' in query:
                test.pausePlaylist()
        elif 'time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			print(strTime)
			speak("Sir, the time is "+strTime)

        elif 'open code' in query:
			os.system("code")