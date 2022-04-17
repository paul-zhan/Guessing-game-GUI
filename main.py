import tkinter as tk
import random
from PIL import ImageTk, Image


window = tk.Tk()
window.geometry("700x500")
number_to_guess = random.randint(0, 100)
print(number_to_guess)
# greeting
greeting = tk.Label(text="Welcome to the guessing game ",
                    background="red",
                    font=40)
greeting.pack()

# instruction
question = tk.Label(text="choose a number between 0 and 100",
                    font=20)
question.pack()

# Entry where the user choose a number
number_reply = tk.Entry()
number_reply.pack()


def guess(number):
    if int(number) == number_to_guess:
        lab1 = tk.Label(window, text="well done")
        lab1.pack()
        global img1
        img1 = ImageTk.PhotoImage(Image.open("well-done-smiley.jpg"))
        label_win = tk.Label(window, image=img1)
        label_win.pack()
        # delete the label after 2 seconds
        print("well done")
        window.after(2000, lambda :lab1.destroy())
        window.after(2000, lambda:label_win.destroy())
        number_reply.delete(0, 'end')

    else:
        lab = tk.Label(window, text="wrong number try again !!")
        lab.pack()
        global img
        img = ImageTk.PhotoImage(Image.open("wrong_image.png"))
        label_loose = tk.Label(window, image=img)
        label_loose.pack()
        # delete the label after 2 seconds
        window.after(2000, lambda: lab.destroy())
        window.after(2000, lambda : label_loose.destroy())
        number_reply.delete(0, 'end')


def clearText(label):
    label.destroy()
    number_reply.delete(0, 'end')


# function to get the number in the entry
def get_answer():
    result = number_reply.get()
    print("get answer is " + result)
    if result.isdigit():
        guess(result)
    else:
        error_label = tk.Label(window, text="Not digit")
        error_label.pack()
        window.after(2000, lambda: clearText(error_label, ))
    return result


# make the submit button
button = tk.Button(window, text="submit", command=get_answer)
button.pack()


window.mainloop()
