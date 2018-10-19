# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.lang.builder import Builder
# from kivy.uix.boxlayout import BoxLayout
#
# class LoginPage(Screen):
#     # def __init__(self, username, password):
#     #          self.username = username
#     #          self.password = password
#     def verify_credentials(self):
#         button = Button(text='My first button')
#         self.username = 'hello'
#         self.password = 'world'
#         if self.ids["login"].text == "username" and self.ids["passw"].text == "password":
#             self.manager.current = "user"
#
# class UserPage(Screen):
#     pass
#
# class ScreenManagement(ScreenManager):
#     pass
#
# kv_file = Builder.load_file('kivy_app.kv')
#
# class LoginApp(App):
#     def builder(self):
#         return kv_file
#
# if __name__ == '__main__':
#     LoginApp().run()
import os
from Tkinter import *
# import Tkinter as tk
# master = Tk()
users = {}

def save_users():
    pass

def create_note_file(name, message=""):
    file_name = str(name)+".txt"
    file= open(file_name,"w+")
    file.write(message)
    file.close()

def read_note_file(name):
    file_name = str(name)+".txt"
    file=open("guru99.txt", "r")
    if file.mode == 'r':
        contents =file.read()
        return contents

def update_note_file(name):
    file_name = str(name)+".txt"
    pass

def delete_note_file(name):
    file_name = str(name)+".txt"
    if(os.path.exists(file_name)):
        os.remove(file_name)

def logout():
    pass

def note_page(name):
    pass

    note_body = Message(top, text=read_note_file(name))
    note_body.pack()


def return_to_overview():
    notes_screen.destroy()
    notes_overview()

def notes_overview(): #This will be the overview of the notes
    top = Toplevel()
    top.title("Notes!")
    msg = Message(top, text="Placeholder...")
    msg.pack()
    # note_name = Entry()
    # note_name.pack()
    new_note_button = Button(top, text="New note", command=note_page(note_name))
    new_note_button.pack()
    del_note_button = Button(top, text="Delete NOte", command=delete_note_file(note_name))
    del_note_button.pack()
    view_note_button = Button(top, text="view Note", command=read_note_file(note_name))
    view_note_button.pack()

def clear_text():
    user.delete(0, 'end')
    password.delete(0, 'end')

def save_person():
    users[user.get()]=password.get()
    clear_text()

def verify():
    for key, values in users.items():
        if user.get() == key:
            if password.get() == users[key]:
                login_screen.destroy()
                notes_overview()
            else:
                print("wrong password")
        else:
            print("no user with that username")

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    entry.delete(0,'end')
    return entry

login_screen = Toplevel()
login_screen.title("new or returning user")
user = makeentry(login_screen, "User name:", 10)
password = makeentry(login_screen, "Password:", 10, show="*")
user.pack()
password.pack()
sign_up = Button(login_screen, text="Sign Up!", command=save_person)
login = Button(login_screen, text="Log In!", command=verify)
sign_up.pack()
login.pack()

mainloop()
