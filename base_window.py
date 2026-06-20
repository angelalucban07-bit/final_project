from tkinter import *
from paragraph_text import *

class BaseWindow:
    def __init__(self):
        '''Creating TKinter window and Frame '''
        self.window = Tk()
        self.window.geometry("1345x680+0+0")
        self.window.title("Typing Speed And Accuracy Test")
        self.window.configure(bg="azure2")
        self.window.minsize(1300, 680)

        self.current_frame = Frame(
            self.window,
            bg="bisque2",
            width=1000,
            height=600
        )
        self.current_frame.pack()


    def get_exit(self) -> None:
        '''Exit from the Tkinter window'''
        self.window.quit()

    def clear_frame(self) -> None:
        '''Destroy/Clear all widgets from current frame'''
        for wid in self.current_frame.winfo_children():
            wid.destroy()

    def go_backward(
            self,
            backward,
            forward,
            title,
            place_holder
    ) -> None:
        '''Travel back in Paragraph dictinary'''

        if self.para_count.get() == 1:
            backward.config(state=DISABLED)
        else:
            backward.config(state=NORMAL)

        forward.config(state=NORMAL)

        self.para_count.set(
            self.para_count.get() - 1)
        self.topic.set(self.paragraph_topic[self.para_count.get()])
        title.config(text=self.topic.get())

        self.paragraph = get_paragraph_text(self.topic.get())
        place_holder.config(text=self.paragraph)

    def go_forward(self, backward, forward, title, place_holder) -> None:
        '''Traverse forward in Paragraph dictionary'''
        if (self.para_count.get() == (len(self.paragraph_topic) - 2)):
            forward.config(state=DISABLED)
        else:
            forward.config(state=NORMAL)

        backward.config(state=NORMAL)

        self.para_count.set(self.para_count.get() + 1)
        self.topic.set(self.paragraph_topic[self.para_count.get()])
        title.config(text=self.topic.get())

        self.paragraph = get_paragraph_text(self.topic.get())
        place_holder.config(text=self.paragraph)