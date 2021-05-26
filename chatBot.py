import tkinter
from tkinter import *
import random

def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text

def chatbot_response(msg):
    name = "MapBot" 
    mood="Great"
    msg=msg.lower()
    res = { 
    "what's your name?": [ 
        "They call me {0}".format(name), 
        "I usually go by {0}".format(name), 
        "My name is the {0}".format(name) ],
    "are you a robot?": [ 
        "What do you think?", 
        "Maybe yes, maybe no!", 
        "Yes, I am a robot with human feelings.", ],
    "how are you?": [ 
        "I am feeling {0}".format(mood), 
        "{0}! How about you?".format(mood), 
        "I am {0}! How about yourself?".format(mood), ]
    }

    more_res={"intents": [
            {
            "patterns": ["hi there", "is anyone there?","hey","hola", "hello", "good day"],
            "responses": ["hello, thanks for asking", "good to see you again", "hi there, how can i help?"],
            "context": [""]
            },
            {
            "patterns": ["bye", "see you later", "goodbye", "nice chatting to you, bye", "till next time"],
            "responses": ["see you!", "have a nice day", "bye! come back again soon."],
            "context": [""]
            },
            {
            "patterns": ["thanks", "thank you", "that's helpful", "awesome, thanks", "thanks for helping me"],
            "responses": ["happy to help!", "any time!", "My pleasure"],
            "context": [""]
            },
            {
            "patterns": ["how you could help me?", "what you can do?", "what help you provide?", "how you can be helpful?", "what support is offered"],
            "responses": ["i can guide you through services of Mapzot"],
            "context": [""]
            }
        ]
    }

    if len(related(msg))>0:
        return random.choice(res[related(msg)])

    elif len(related(msg))==0:
        for ele in more_res['intents']:
            if msg in ele['patterns']:
                return random.choice(ele['responses'])

    return random.choice(["sorry, can't understand you", "please give me more info", "not sure i understand"])
    #switcher={
    #   1: 'Give demo for a service',
    #   2: 'Direct to agent'
    #} 
    #return switcher.get(int(msg),'You have entered invalid input.\nPlease Enter a valid input')

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "MapBot : "+res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("MapBot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="grey", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#First message
first_msg="Welcome to Mapzot.\n"
ChatLog.config(state=NORMAL)
ChatLog.insert(END,"MapBot : "+ first_msg + '\n\n')
ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
ChatLog.config(state=DISABLED)
ChatLog.yview(END)


#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="black",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=6, y=401, height=90, width=265)
SendButton.place(x=275, y=401, height=90,width=120)

base.mainloop()
