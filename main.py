from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import SpeechRecognition as s
import threading

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("MyBot")
convo = [
   "Hello",
    "Hi there!",
    "What is your name?",
    "My name is chatbot prepared by Abhijit Chingalwar.",
    "WHere are you studying?",
    "Nit jalandhar",
    "How are you doing?",
    "I'm doing great,what about you?",
    "M fine",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
 #now training the bot with the help of trainer
trainer = ListTrainer(bot)
trainer.train(convo)

#answer = bot.get_response("How are you doing?")
#print(answer)

#print("Talk to bot")
#while True:
  #query = input()
  #if query == 'exit':
     # break
  #answer = bot.get_response(query)
  #print("bot: ",answer)

main = Tk()
main.geometry("500x650")  #500 is width and 650 is height
main.title("mychatbot")
img =PhotoImage(file="mat1.png") #img is object of class PhotoImage
photoL = Label(main,image=img)
photoL.pack(pady=5) #yaxis pading=5


#query takin:It takes audio ias a input froma a user and convert it into a astring
def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening to you")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textf.insert(0,query)
            ask_from_bot()
        except exception as e:
            print(e)
            print("Not recongnized")

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END,"you :" +query)
    msgs.insert(END,"bot : "+str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)


frame =Frame(main) #list window for conversation
sc = Scrollbar(frame)
msgs =Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side =RIGHT ,fill = Y) #appear on right side
msgs.pack(side = LEFT ,fill =BOTH,pady=10)
frame.pack()

#creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill = X,pady=10)
btn =Button(main,text="Ask From Bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

#crating a function
def enter_function(event):
    btn.invoke()

#going to bind main window with eneter key
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()
main.mainloop()