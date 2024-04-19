from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

from media import gop

img_bw = "./models/Default_Image/bg.webp"

root = Tk()

img1 = ImageTk.PhotoImage(Image.open(img_bw).resize((500, 300), Image.Resampling.LANCZOS))
Dis_pic_1 = Label(root, image=img1)
Dis_pic_1.place(x=400, y=70)

root.geometry("1200x800+10+20")
root.title("GAME ON POSE")

def conversion():
    messagebox.showinfo("Alert!", "To Stop the Program , Press Q key")
    gop()

cvtbtn = Button(root, text="Start GOP", padx=50, pady=5, width=20, command=conversion)
cvtbtn.place(x=500, y=500)

# Create a Label widget to display "Hill Climb" text
hill_climb_label = Label(root, text="Hill Climb", font=("Helvetica", 24  , 'bold'))
hill_climb_label.place(x=550, y=400)

root.mainloop()
