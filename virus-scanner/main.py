import tkinter as tk
from controller import openFileExpoler
from PIL import Image, ImageTk




def on_button_click():
    filename = openFileExpoler()
    print("this is fileName",filename)
    if(filename):
        file_chosen.config(text=filename)
        hasFileBeenUploaded.config(text ="File Uploaded")




root = tk.Tk()
root.configure(bg ="white")

root.geometry("500x500")

root.minsize(500, 500)
 

root.maxsize(500, 500)

root.title("File Checker")


image1 = Image.open(r"virus-scanner\assets\file.png")
test = ImageTk.PhotoImage(image1)

frame = tk.Frame(root, width=500, height=80, highlightbackground="black", highlightthickness=2, background="black" )
frame.place(x = 0, y =0)


label = tk.Label(root, text ="Malware Scanner", font =("Inter", 20), foreground="white", bg="black")



label.place(x=130, y =20)

button = tk.Button(root, text = "Export File", command=on_button_click)
button.place(x=340, y=135)

file_path_frame = tk.LabelFrame(root, "", bg="white", foreground="black", width=260, height=27 )

file_path_frame.place(x = 50, y = 135)

file_chosen = tk.Label(root, text="Choose a file", font=("Inter" ,10), bg="white")

file_chosen.place(x =52, y =138)


button = tk.Button(root, text ="Scan File", height=2, width= 19 )
button.place(x= 190, y=340)

picLabel = tk.Label(image=test, bg="white")
picLabel.image = test

picLabel.place(x=40, y=234)

hasFileBeenUploaded =tk.Label(root, text="File has not been uploaded", bg ="white", font=("Inter", 11))
hasFileBeenUploaded.place(x=120, y =254) 



root.mainloop()
