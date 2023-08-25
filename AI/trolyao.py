import speech_recognition
import pyttsx3
from datetime import date 
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


while True:
	# nghe
	with speech_recognition.Microphone() as mic:
		print("Robot : I'm listening")
		audio = robot_ear.listen(mic)
	print("Robot : ...")
	try:
		you = robot_ear.recognize_google(audio)
	except: 
		you = ""

	print("you : " + you)



	# --------


	# hiểu
	if you == "":
		robot_brain = "i can't hear you , try agian "
	elif  "hello" in you:
		robot_brain = "Hello Men"
	elif  "today" in you :
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you :
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "name" in you:
		robot_brain = "My name is robot"
	elif "help" in you:
		robot_brain = "yes , i can help you . you can ask me any questions ?"
	elif "bye" in you:
		robot_brain = "Bye Alex"
		print("Robot : " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else : 
		robot_brain = "shut up now  "

	print("Robot : " + robot_brain)

	# ---------
	# nói 



	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
