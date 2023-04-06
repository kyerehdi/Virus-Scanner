from tkinter import filedialog
def openFileExpoler():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text Files", "*.txt"),("All Files", "*.*")))
    return filename
    
