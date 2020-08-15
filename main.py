import os.path
from os import path
from tkinter import *
from PIL import ImageTk, Image

account_names = [str("test1"), str("test2"), str("test3"), str("test4"), str("test5"), str("test6"), str("test7")]
aliases = [str("testA1"), str("testA2"), str("testA3"), str("testA4"), str("testA5"), str("testA6"), str("test7")]
row = 0
root = Tk()
root.title("SteamSwitch")
imgs = []
rows = []
pad = 5



def log_in_button(account_name):
    print(account_name)


def show_acc(i,row):
    img_loc = "./images/" + account_names[i] + ".jpg"
    if not path.isfile(img_loc):
        img_loc = "./placeholder.png"
    imgs.append(ImageTk.PhotoImage(Image.open(img_loc)))
    image = Label(rows[row - 1], image=imgs[i], borderwidth=2, relief="solid")
    alias = Label(rows[row - 1], text=aliases[int(i)], wraplength=120)
    login_button = Button(rows[row - 1], text="Log In", command=lambda: log_in_button(account_names[i]), bd=0)

    image.grid(row=1, column=i % 5, padx=pad, pady=pad)
    alias.grid(row=2, column=i % 5, padx=pad, pady=pad)
    login_button.grid(row=3, column=i % 5, padx=pad)


if __name__ == '__main__':
    for i in range(int(len(account_names))):
        if int(i / 5 + 1) != row:
            rows.append(Frame(root))
            row = row + 1
            rows[row - 1].pack()

        show_acc(i,row)


    root.mainloop()
