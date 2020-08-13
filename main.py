import PySimpleGUI as sg

account_name = "stefystefystefy1"

if __name__ == '__main__':

    layout = [[sg.Text(account_name)], [sg.Button("Log in")]]

    window = sg.Window(title="Steam account switcher for Linux by Cshark", layout=layout, margins=(100, 50)).read()

