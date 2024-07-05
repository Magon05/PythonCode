from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import random

class MainApp(App):

    level = 1

    def generate(self):
        if self.level < 10:
            self.num1 = random.randrange(10, 100)
            self.num2 = random.randrange(10, 100)
        elif self.level >= 10 and self.level < 20:
            self.num1 = random.randrange(100, 1000)
            self.num2 = random.randrange(100, 1000)
        elif self.level >= 20:
            self.num1 = random.randrange(1000, 10000)
            self.num2 = random.randrange(1000, 10000)
        self.ans1 = self.num1 + self.num2 + self.num1
        self.ans2 = self.num1 + self.num2 + self.num2
        self.ans3 = self.num1 + self.num2
        self.answerlist = [self.ans1, self.ans2, self.ans3]
        self.var1 = random.choice(self.answerlist)
        self.answerlist.remove(self.var1)
        self.var2 = random.choice(self.answerlist)
        self.answerlist.remove(self.var2)
        self.var3 = random.choice(self.answerlist)
        self.answerlist.remove(self.var3)

        self.label = Label(text='%s + %s' % (self.num1, self.num2), size_hint=(1, 1),
                           pos_hint={'center_x': .5, 'center_y': .5}, font_size=60)
        self.button1 = Button(text=str(self.var1), pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)
        self.button2 = Button(text=str(self.var2), pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)
        self.button3 = Button(text=str(self.var3), pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)

        self.button1.bind(on_press=self.press_but1)
        self.button2.bind(on_press=self.press_but2)
        self.button3.bind(on_press=self.press_but3)
        print(self.level)

    def update(self):
        self.main_layout.remove_widget(self.label)
        self.main_layout.remove_widget(self.button1)
        self.main_layout.remove_widget(self.button2)
        self.main_layout.remove_widget(self.button3)
        self.main_layout.add_widget(self.label)
        self.main_layout.add_widget(self.button1)
        self.main_layout.add_widget(self.button2)
        self.main_layout.add_widget(self.button3)

    def build(self):
        self.generate()
        self.main_layout = BoxLayout(orientation="vertical")
        #self.answer = TextInput(multiline=False, readonly=True, halign="center", font_size=55, pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.2, .1))
        #main_layout.add_widget(self.answer)
        self.update()

        return self.main_layout

    def press_but1(self, instance):
        if self.num1 + self.num2 == self.var1:
            self.generate()
            self.update()
        else:
            self.button1 = Button(text="Wrong", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)
            self.update()
            self.level -= 1

    def press_but2(self, instance):
        if self.num1 + self.num2 == self.var2:
            self.generate()
            self.update()
        else:
            self.update()
            self.button2 = Button(text="Wrong", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)
            self.level -= 1

    def press_but3(self, instance):
        if self.num1 + self.num2 == self.var3:
            self.level += 1
            self.main_layout.remove_widget(self.label)
            self.main_layout.remove_widget(self.button1)
            self.main_layout.remove_widget(self.button2)
            self.main_layout.remove_widget(self.button3)
            self.generate()
            self.main_layout.add_widget(self.label)
            self.main_layout.add_widget(self.button1)
            self.main_layout.add_widget(self.button2)
            self.main_layout.add_widget(self.button3)
        else:
            self.level -= 1
            self.main_layout.remove_widget(self.button3)
            self.button3 = Button(text="Wrong", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60)
            self.main_layout.add_widget(self.button3)

if __name__ == "__main__":
    app = MainApp()
    app.run()