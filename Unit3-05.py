# Created by : peter zhu

import ui

def calculate_touch_up_inside(sender):
    user_number = int(view['user_number_textfield'].text)
    
    if user_number < 0:
        view['answer_label'].text = "Enter positive integer"
    elif user_number == 0:
        view['answer_label'].text = "1"
    else:
        factorial = counter = 1
        while (counter < user_number):
            counter = (counter + 1)
            factorial = counter * factorial
            view['answer_label'].text = str(factorial)

view = ui.load_view()
view.present('full_view')
