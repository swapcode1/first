from tkinter import *
from datetime import date
from datetime import datetime

'''this are liabraries for playing music'''
from pygame import mixer

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


                                                                                                                                                                                      #print("Today's date:", tm)
root = Tk()
def send():
    send = "You:" + e.get().lower()
    text.insert(END, "\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "bot: hi")
    elif (e.get() == 'what is your name'):
        text.insert(END, "\n" + "bot: hi")
    elif (e.get() == 'how are you'):
        text.insert(END, "\n" + "bot: i'm fine and you?")
    elif(e.get()=='i am fine too'):
        text.insert(END, "\n" + "bot: oh! nice to hear that...")
    elif (e.get() == 'hi robo'):
        text.insert(END, "\n" + "bot: What can I do for you?")
        text.insert(END,"\n" + "1.Show me date")
        text.insert(END, "\n" + "2.Show me time")
        text.insert(END, "\n" + "3.play some music")
                                                                                                                                                                                      #send = "You:" + e.get()
                                                                                                                                                                                      #text.insert(END, "\n" + send)
    elif(e.get()=='1'):
        text.insert(END, "\n" + "bot: Today is..")
        text.insert(END,today)
    elif(e.get() == '2'):
        text.insert(END, "\n" + "bot:Its about " + current_time)
    elif(e.get() == '3'):
        text.insert(END,"\n"+"music ...")
        r1 = Tk()
        r1.geometry("300x300")
        r1.config(bg='pink')
        mixer.init()
        mixer.music.load("sample1.mp3")
        mixer.music.play()
        def pause():
            mixer.music.pause()

        def play():
            mixer.music.play()


        #Label(r1, text="Welcome to music player", font="lucidia 30 bold").pack()
        Button(r1,text="Pause", bg='skyblue', fg='black', command=pause).place(x=150, y=100)


    else:
        text.insert(END, "\n" + "bot: i didnt got it..")
text=Text(root,bg='gray', fg='white', font=20)
text.grid(row=0,column=0,columnspan=3)
e = Entry(root,width=100)
send = Button(root,text='Send' ,bg='skyblue' ,fg='white',width=40,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('robo')
root.mainloop()


