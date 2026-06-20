from tkinter import *
from paragraph_text import *
from typing_ui import TypingUI

class TypingTest(TypingUI):
    '''Includes all operation for Typing Test'''

    def __init__(self):
        super().__init__()

        self.para_count = IntVar()
        self.topic = StringVar()
        self.paragraph_topic = list(
            get_paragraph_topic()
        )

        self.start_time = 0
        self.end_time = 0
        self.seconds = 0
        self.minutes = 0

        self._start_flag = 0
        self._backspace_count = 0
        self._key_press_count = 0
        self._get_user_text = ""

        self._paragraph = ""

    def reset_data(self) -> None:
        '''Reset variables for next typing test'''

        self.start_flag = 0
        self.seconds = 0
        self.minutes = 0
        self.backspace_count = 0

    def back_to_home(self) -> None:
        '''Return to home page'''
        self.reset_data()
        self.clear_frame()
        self.set_typing_home()

if __name__ == '__main__':
    '''Creating Typing Class Instance'''
    typing_test = TypingTest()
    typing_test.set_typing_home()
    typing_test.window.mainloop()