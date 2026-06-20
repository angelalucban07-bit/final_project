from tkinter import *
from tkinter import messagebox

from paragraph_text import *
from typing_ui import TypingUI
from typing_feature import TypingFeature

class TypingTest(TypingUI, TypingFeature):
    """Includes all operation for Typing Test"""

    def __init__(self):
        super().__init__()

#paragraph_variable
        self.paragraph = ""
        self.para_count = IntVar()
        self.topic = StringVar()
        self.paragraph_topic = list(
            get_paragraph_topic()
        )
#timer_variable
        self.start_time = 0
        self.end_time = 0
        self.seconds = 0
        self.minutes = 0
#encap_timer_variable
        self._start_flag = 0
        self._backspace_count = 0
        self._key_press_count = 0
        self._get_user_text = ""

    def reset_data(self) -> None:

        self._start_flag = 0
        self.seconds = 0
        self.minutes = 0
        self._backspace_count = 0

    def back_to_home(self) -> None:
        self.reset_data()
        self.clear_frame()
        self.set_typing_home()

    def get_exit(self) -> None:
        """Override BaseWindow get_exit"""
        answer = messagebox.askyesno(
            "Exit",
            "Do you want to exit?"
        )
        if answer:
            self.window.quit()

if __name__ == '__main__':
    '''Creating Typing Class Instance'''
    typing_test = TypingTest()
    typing_test.set_typing_home()
    typing_test.window.mainloop()