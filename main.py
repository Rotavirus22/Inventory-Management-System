from tkinter import *
from tkinter import font

root = Tk()

root.title("Stock Panda")
root.config(bg="#8A908B")
root.geometry("1100x700")
root.maxsize(height=700, width=1100)
root.minsize(height=700, width=1100)

# Custom text styles
customButtonFont = font.Font(size=10, weight="bold")
customTitleFont = font.Font(size=20, weight="bold")

# to display text logo
textlogo = PhotoImage(file="textlogo.png")
logoDispaly = Label(root, image=textlogo, bg="#8A908B")
logoDispaly.place(x=30, y=20)

# for hero text
Label(root, text="Stock Panda", bg="#8A908B", font=("Arial", 30, "bold")).place(x=30, y=290)
Label(root, text="Some Description about the software", bg="#8A908B", font=("Arial", 20, "bold")).place(x=30, y=340)



container = Frame(bg="#D9D9D9", height=700, width=450)
container.pack_propagate(False)
container.pack(side=RIGHT)

h1 = Label(container, text="Get Started", bg="#D9D9D9", font=customTitleFont)
h1.place(x=150, y=250)

buttonContainer = Frame(container, height=5, width=400, bg="#D9D9D9")
buttonContainer.place(x=60, y=300)

login = Button(buttonContainer, text="Log in", height=2, width=20, border=0, bg="#FF5252", fg="white",
               font=customButtonFont)
login.grid(column=0, row=0)

signup = Button(buttonContainer, text="Sign up", height=2, width=20, border=0, bg="#FF5252", fg="white",
                font=customButtonFont)
signup.grid(column=1, row=0, padx=15)

root.mainloop()