from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import random

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"
    
    def login(self, uname, pw):
        with open("users.json", 'r') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pw:
            self.manager.current = "home_screen"
        else:
            self.ids.alert.text = "Incorect Username or Password"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json", "r") as file:
            user = json.load(file)
        with open("users.json", "w") as file:
            user[uname] = {'username': uname, 'password': pword, 'created': datetime.now().strftime("%Y-%m-%d %r")}
            json.dump(user, file)
            self.manager.current = "successregister_screen"

class SuccessRegisterScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

class HomeScreen(Screen):
    def logout(self):
        self.manager.current = "login_screen"
    
    def search(self, feel):
        if feel in ["happy", "sad", "unloved"]:
            with open(f"{feel}.txt", 'r') as file:
                word = [w for w in file.readlines()]
            self.ids.quote.text = random.choice(word)
        else:
            self.ids.quote.text = "Please fill correct input"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
