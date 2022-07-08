from tkinter import *

root = Tk()
root.title("DICTIONARY")
root.geometry("400x400")
root.configure(background='cyan')


label_codepen = Label(root)
label_vs = Label(root)
label_thunkable = Label(root)


ide = {'Codepen':'Its an online programing tool for web designing',
       'Visual Studio Code':'Its an offline progaminging tool for web designing',
       'Thunkable':'Its an online block-coding tool'}

def codepen():
    label_codepen["text"]=ide['Codepen']

def vs():
    label_vs["text"]=ide['Visual Studio Code']

def thunkable():
    label_thunkable["text"]=ide['Thunkable']
    



button_codepen = Button(root,text = "Codepen",command=codepen)
button_codepen.place(relx=0.5,rely=0.2,anchor=CENTER)
label_codepen.place(relx=0.5,rely=0.3,anchor=CENTER)

button_vs = Button(root,text = "Visual Studio Code",command=vs)
button_vs.place(relx=0.5,rely=0.4,anchor=CENTER)
label_vs.place(relx=0.5,rely=0.5,anchor=CENTER)

button_thunkable = Button(root,text = "Thunkable",command=thunkable)
button_thunkable.place(relx=0.5,rely=0.6,anchor=CENTER)
label_thunkable.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()