from tkinter import *
from PIL import ImageTk, Image

account_names = [str("test1"), str("test2"), str("test3"), str("test4"), str("test5"), str("test6")]
aliases = [str("testA1"), str("testA2"), str("testA3"), str("testA4"), str("testA5"), str("testA6")]
row = 1
root = Tk()
root.title("SteamSwitch")
img = []



def log_in_button(account_name):
    print(account_name)


def show_acc(i,row):
    img.append(ImageTk.PhotoImage(Image.open("./images/" + account_names[i] + ".jpg")))
    image = Label(image=img[i])
    alias = Label(root, text=aliases[int(i)])
    login_button = Button(root, text="Log In", command=lambda: log_in_button(account_names[i]), bd=0)

    image.grid(row=row, column=i % 5)
    alias.grid(row=row + 1, column=i % 5)
    login_button.grid(row=row + 2, column=i % 5)


if __name__ == '__main__':
    for i in range(int(len(account_names))):
        if int(i / 5 + 1) != row:
            row = row + 3
        show_acc(i,row)
        print("int(i / 5 + 1) =", int(i / 5 + 1))
        print(row)


    root.mainloop()
