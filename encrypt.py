from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.geometry("320x250")
root.title("Encrypter/Decrypter")
root.configure(bg="Blue")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg'), ('png file', '*.png'), ('jpeg file', '*.jpeg'), ('pdf file', '*.pdf')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()  # Get the key and remove leading/trailing spaces
        if not key:
            messagebox.showerror("Is mai bhi Error😑🤦‍♂️", "Too bad, you dont even know how to type in a white box")
            return  # Exit the function if no key is entered

        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close() 

#Window management

Label(root,text="Enter key and click on button to Encrypt/Decrypt the file").place(x=10,y=10)

entry1=Text(root,height=1,width=10)
entry1.place(x=110,y=50)

b1=Button(root,text="Enter Key",command=encrypt_image)
b1.place(x=120,y=90)

root.mainloop()



























































































# reference: https://www.youtube.com/watch?v=OGy7K9Zv-4o