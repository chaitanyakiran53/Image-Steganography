
#importing modules for python Image Steganography project
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox

#Initializing the screen for python Image Steganography project
# decoding the file for python Image Steganography project
def Decode():
    Screen.destroy()
    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg","*png"),("all type of files","*.*")))
        
    def Decoder():
        #Output
        Message=stg.reveal(FileOpen)
        label3 = Label(DecScreen, text=Message)
        label3.place(x=20, y=200)
        

    DecScreen = Tk()
    DecScreen.title("Decode an Image")
    DecScreen.geometry('600x300')
    DecScreen.resizable(0, 0)
    DecScreen.config(bg='Bisque')
    Label(DecScreen, text='Decode an Image', font=("Comic Sans MS", 15), bg='Bisque').place(x=220, rely=0)
    Label(DecScreen, text='Select the path to the image :', font=("Times New Roman", 14),
          bg='Bisque').place(x=10, y=50)
    SelectButton1 = Button(DecScreen,text="Select the file",  font =('Times New Roman',10),command=OpenFile)
    SelectButton1.place(x=350, y=50)
    text_strvar = StringVar()
    Button(DecScreen, text='Decode the Image', font=('Helvetica', 12), bg='PaleTurquoise',command=Decoder).place(x=220, y=110)
    Label(DecScreen, text='Text that has been encoded in the image:', font=("Times New Roman", 12), bg='Bisque').place(
        x=180, y=150)
    

def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode Images")
    EncScreen.geometry('600x220')
    EncScreen.resizable(0, 0)
    EncScreen.config(bg='AntiqueWhite')


    Label(EncScreen, text='Encode an Image', font=("Comic Sans MS", 15), bg='AntiqueWhite').place(x=220, rely=0)
    # Label(EncScreen, text='Enter the path to the image(with extension):', font=("Times New Roman", 13),
    #       bg='AntiqueWhite').place(x=10, y=50)
    Label(EncScreen, text='Enter the data to be encoded:', font=("Times New Roman", 13), bg='AntiqueWhite').place(
        x=10, y=90)
    Label(EncScreen, text='Enter the output file name (without extension):', font=("Times New Roman", 13),
          bg='AntiqueWhite').place(x=10, y=130)
    # img_path = Entry(EncScreen, width=35)
    # img_path.place(x=350, y=50)
    text_to_be_encoded = Entry(EncScreen, width=35)
    text_to_be_encoded.place(x=350, y=90)
    after_save_path = Entry(EncScreen, width=35)
    after_save_path.place(x=350, y=130)
    
 
    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir = "/Desktop" , title = "SelectFile",filetypes=(("jpeg files","*jpg"),("all files","*.*")))
 
        label2 = Label(text=FileOpen)
        label2.place(x=360, y=52)
 
    def Encoder():
        Response= messagebox.askyesno("PopUp","Do you want to encode the image")
        if Response == 1:
            stg.hide(FileOpen,after_save_path.get()+".jpg",text_to_be_encoded.get())
            messagebox.showinfo("Pop Up","Successfully Encoded the image")
        else:
            messagebox.showwarning("Pop Up","Unsuccessful,please try again")
 
    SelectButton = Button(text="Select the file",command=OpenFile)
    SelectButton.place(x=250, y=50)
    EncodeButton=Button(EncScreen, text='Encode the Image', font=('Helvetica', 12), bg='PaleTurquoise', command=Encoder )
    EncodeButton.place(x=220, y=175)

#creating buttons
Screen = Tk()
Screen.title('Image Steganography')
Screen.geometry('300x200')
Screen.resizable(0, 0)
Screen.config(bg='NavajoWhite')
Label(Screen, text='Image Steganography', font=('Comic Sans MS', 15), bg='NavajoWhite',
      wraplength=300).place(x=40, y=0)
Button(Screen, text='Encode', width=25, font=('Times New Roman', 13), bg='SteelBlue',command=Encode ).place(
    x=30, y=80)
Button(Screen, text='Decode', width=25, font=('Times New Roman', 13), bg='SteelBlue',command=Decode).place(
    x=30, y=130)
mainloop()