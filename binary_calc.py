from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import re

class MainApp(App):
    def build(self):
        self.icon = "icon.png"
        self.operators = ["-","+"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black",foreground_color = "white")

        main_layout.add_widget(self.solution)
        buttons = [
            ["1", "0", "-"],
            ["1s", "2s", "+"],
            ["C"]  
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color = "grey",
                    pos_hint = {"center_x":0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)


        equal_button = Button(
            text = "=", font_size=30, background_color = "grey",
            pos_hint = {"center_x":0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout


    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "1s":
            if current:
               #write the negative representation of the binary number
                inverted_binary_string = ""

                for char in self.solution.text: # this for loop covers 1s complement
                    if char == "0":
                        inverted_binary_string += "1"
                    elif char == "1":
                        inverted_binary_string += "0"
                    else:
                        inverted_binary_string += char
                
                self.solution.text = inverted_binary_string
        elif button_text == "2s": # 2s COMPLEMENT CODE - TAKE AWAY "PASS" AND PUT HERE
            pass

        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return 
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                elements = re.findall(r'[01]+|[-+]', text)
            # Split the expression into numbers and operators

            # Initialize variables
                result = elements[0]
                current_operator = None

            # Iterate through the elements and perform binary calculations
                for element in elements[1:]:
                    if element in self.operators:
                        current_operator = element
                    else:
                        if current_operator == "+":
                            result = bin(int(result, 2) + int(element, 2))[2:]
                            if len(result) >= 9:
                                result = "OVERFLOW"
                        elif current_operator == "-":
                            result = bin(int(result, 2) - int(element, 2))[2:]

            # Update the TextInput with the result
                self.solution.text = result
            except Exception as e:
            # Handle any errors or invalid input
                self.solution.text = "Error"
     


if __name__ == "__main__":
    app = MainApp()
    app.run()