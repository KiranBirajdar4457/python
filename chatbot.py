from tkinter import *

root = Tk()
root.title("Chatbot")

def send():
    message = "You -> " + e.get()
    txt.insert(END, message + "\n")
    user_input = e.get().lower()
    if user_input == "hello":
        txt.insert(END, "Bot -> Hi\n")
    elif user_input in ["hi", "hii", "hiiii"]:
        txt.insert(END, "Bot -> Hello\n")
    elif user_input == "how are you":
        txt.insert(END, "Bot -> Fine! And you?\n")
    elif user_input in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "Bot -> Great! How can I help you?\n")
    else:
        txt.insert(END, "Bot -> Sorry! I didn't get you\n")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0)

send_button = Button(root, text="Send", command=send)
send_button.grid(row=1, column=1)

root.mainloop()
