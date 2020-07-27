from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import webbrowser
root=Tk()
root.geometry("1366x768")
root.title("Online Doctor")



from chatterbot import ChatBot
from chatterbot.trainers  import ListTrainer
chatbot = ChatBot("My Bot")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "How are you?",
    "I'm doing great. How are you?",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Where do you live?",
    "I live in calfornia",
    "What is your name?",
    "That's a good name",
    "My name is Jerry- The health care chatbot",
    "My name is Jerry- The health care chatbot",
    "Then check out our services, it will surely help you. Have futher queries?",
    "Sorry to hear. So, have you consulted from our services?",
    "Yes, i did",
    "oh that's great. Get well soon dear",
    "No, i didn't",
    "Then check out our services, it will surely help you. Have futher queries?",
    "What kind of services you provide",
    "Basically we provide three services, disease related query, medicine services and chatbot. In medicine services, you have choice for allopathy, homeopathy or home remedy",
    "Great",
    "Have any other queries?",
    "No, thanks",
    "Most welcome",
    "Sure. We provide doctor consultancy in two well reputed healthcare centres, AIIMS and MEDCARE. Doctor ved from AIIMS, his email id is ved12@gmail.com and doctor krishna from medcare, his email id is krishnamedcare@gmail.com ."
    "Have a nice day"
    
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

def consultancyservice():
    from tkinter import Label,Tk
    from PIL import ImageTk,Image
    import pyttsx3
    main=Toplevel()
    main.title("CHATBOT")
    main.geometry("500x610")
    hey=ImageTk.PhotoImage(Image.open("healthbot.png"))
    l1=Label(main,image=hey)
    l1.pack()

    def askfrombot():
        query=e1.get()
        response = chatbot.get_response(query)
        box.insert(END,"me: ",query)
        box.insert(END,"bot: ",str(response))
        e1.delete(0,END)
        box.yview(END)
        var=pyttsx3.init()
        var1=var.getProperty("voices")
        var.setProperty("voice",var1[1].id)
        var.setProperty("rate",140)
        var.say(str(response))
        var.runAndWait()
        
    frame=Frame(main)
    scroll=Scrollbar(frame)
    scroll.pack(side=RIGHT,fill=Y)
    box=Listbox(frame,height=20,width=80, yscrollcommand=scroll.set)
    box.pack(side=LEFT,fill=BOTH,pady=10)
    frame.pack()
    e1=Entry(main,width=80,font=("candara light",20))
    e1.pack()
    b1=Button(main,text="ASK FROM BOT",width=15,font=("Castellar",20),fg="blue",relief="solid",command=askfrombot)
    b1.pack()
    def enter_function():      # event to be passed here
        b1.invoke()
        
    main.bind("<Return>",lambda e:enter_function())  # if only the function is called without lambda i.e.. enter_function then event is to be passed above in the function definition
    main.mainloop()



def for_alopathy():
    d=disease.get()
    #print("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=",d,"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
    webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=allopathic medicines for "+d+"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
def for_homeopathy():
    d=disease.get()
    #print("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=",d,"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
    webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=homeopathic medicines for "+d+"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
def for_homeremedy():
    d=disease.get()
    #print("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=",d,"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
    webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=home remedy cure for "+d+"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
def services():
    medipage=Toplevel()
    medipage.geometry("1366x768")
    medipage.title("medicine services")
    Button(medipage,text="ALOPATHY",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=for_alopathy).pack(pady=20)
    Button(medipage,text="HOMEOPATHY",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=for_homeopathy).pack(pady=20)
    Button(medipage,text="HOME REMEDY",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=for_homeremedy).pack(pady=20)


def diseasesearch():
    d=disease.get()
    print("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q=",d,"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
    webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNR4y3QpLzvxjAdqYHNcnr73M0fgyA%3A1571923645490&source=hp&ei=vaaxXcOfG6zA3LUPlrK3kA4&q="+d+"&oq=col&gs_l=psy-ab.1.0.35i39l2j0i67l8.1113.1586..3796...0.0..0.312.853.2-2j1......0....1..gws-wiz.CNcchl-LwoI")
def thirdpage():
    tpage=Toplevel()
    tpage.geometry("1366x768")
    tpage.title("Query")
    var1=pyttsx3.init()
    v1=var1.getProperty("voices")
    var1.setProperty("voice",v1[1].id)
    var1.setProperty("volumne",1)
    var1.setProperty("rate",140)
    var1.say("tell us about your disease")
    var1.runAndWait()
    global disease
    disease=StringVar()
    Label(tpage,text="TELL US:-)",font=("Castellar",20,"underline","bold"),fg="midnight blue").pack(pady=60)
    Entry(tpage,textvariable=disease,borderwidth=4,width=30,).pack()
    Button(tpage,text="ENTER",font=(10),borderwidth=4,relief="raised",command=diseasesearch).pack(pady=30)

def secondpage():
    spage=Toplevel()
    spage.geometry("1366x768")
    spage.title("welcome")
    Button(spage,text="DISEASE RELATED QUERY",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=lambda :thirdpage()).pack(pady=20)
    Button(spage,text="MEDICINE SERVICES",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=lambda :services()).pack(pady=20)
    Button(spage,text="DOCTOR CONSULTANCY",font=("Candara Light",15,"bold"),fg="midnight blue",borderwidth=4,relief="raised",command=lambda :consultancyservice()).pack(pady=20)
var=pyttsx3.init()
v=var.getProperty("voices")
var.setProperty("voice",v[1].id)
var.setProperty("volumne",1)
var.setProperty("rate",140)
var.say("Welcome to our online services of health care")
var.runAndWait()
a=ImageTk.PhotoImage(Image.open("doconline.jpg"))
Label(root,image=a,borderwidth=4,bg="midnight blue").pack()
l1=Label(root,text="VISIT OUR PAGE",font=("forte 22 underline bold"),fg="midnight blue")
l1.pack(pady=20)
l1.bind("<Button-1>",lambda second:secondpage())
root.mainloop()

