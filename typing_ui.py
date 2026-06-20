from tkinter import *
import time
from paragraph_text import get_paragraph_text
from statistics import Statistics

class TypingUI(Statistics):
    def show_typing_result(self) -> None:
        '''Setting result interface for typing speed'''
        self.clear_frame()

        (accuracy, actual_accuracy, wpm, total_time) = self.calculate_result()
        result = Label(
            self.current_frame,
            text="Result",
            fg='black',
            bg='skyblue1',
            font='Lucida\\ Calligraphy 26 underline'
        )
        result.grid(row=0, columnspan=3, pady=40)

        lb_accuracy = Label(
            self.current_frame,
            text='Accuracy',
            fg='black',
            bg='LightSalmon2',
            font='Lucida\\ Fax 22')
        lb_accuracy.grid(row=1, column=0)

        accuracy_val = Label(
            self.current_frame,
            text=f'{accuracy}%',
            fg='red',
            bg='khaki',
            font='Lucida\\ Fax 22 bold'
        )
        accuracy_val.grid(row=1, column=1, columnspan=2)

        lb_actual_accuracy = Label(
            self.current_frame,
            text='Actual Accuracy',
            fg='black',
            bg='LightSalmon2',
            font='Lucida\\ Fax 22'
        )
        lb_actual_accuracy.grid(row=2, column=0, pady=(25, 0))
        accuracy_actual_val = Label(
            self.current_frame,
            text=f'{actual_accuracy}%',
            fg='red',
            bg='khaki',
            font='Lucida\\ Fax 22 bold'
        )
        accuracy_actual_val.grid(row=2, column=1, columnspan=2, pady=(25, 0))

        lb_wpm = Label(
            self.current_frame,
            text="WPM", fg='black',
            bg='LightSalmon2',
            font='Lucida\\ Fax 22'
        )
        lb_wpm.grid(row=3, column=0)
        val_wpm = Label(
            self.current_frame,
            text=f'{wpm}',
            fg='red',
            bg='khaki',
            font='Lucida\\ Fax 22 bold'
        )
        val_wpm.grid(row=3, column=1, columnspan=2, pady=25)

        lb_time = Label(
            self.current_frame,
            text="Total Time",
            fg='black',
            bg='LightSalmon2',
            font='Lucida\\ Fax 22'
        )
        lb_time.grid(row=4, column=0)
        val_time = Label(
            self.current_frame,
            text=f'{total_time}',
            fg='red', bg='khaki',
            font='Lucida\\ Fax 22 bold'
        )
        val_time.grid(
            row=4,
            column=1,
            columnspan=2
        )

        lb_exit = Button(
            self.current_frame,
            text='EXIT',
            fg='red',
            bg='plum1',
            font='Verdana\\ Pro 18 bold',
            borderwidth=3,
            command=self.get_exit
        )
        lb_exit.grid(
            row=5,
            column=1,
            pady=50,
            padx=30
        )
        lb_home = Button(
            self.current_frame,
            text='HOME',
            fg='red',
            bg='plum1',
            font='Verdana\\ Pro 18 bold',
            borderwidth=3,
            command=self.back_to_home
        )
        lb_home.grid(
            row=5,
            column=2,
            pady=50,
            padx=30
        )

    def key_release(self, event) -> None:
        '''Start timer and get user inputs'''
        if self.start_flag == 0:
            self.start_flag = 1
            self.start_time = time.time()
            self.update_timer(self.start_time)

        self.get_user_text = self.user_input.get('1.0', 'end - 1c')

        if self.paragraph.startswith(self.get_user_text):
            self.user_input.config(fg='green')
        else:
            self.user_input.config(fg='red')

        if event.keysym == 'BackSpace':
            self.backspace_count += 1

        self.key_press_count = len(self.get_user_text)
        if self.key_press_count >= len(self.paragraph):
            self.end_time = time.time()
            self.show_typing_result()

    def start_typing(self) -> None:
        '''Setting environment for user to type paragraph text to check speed and accuracy'''
        self.clear_frame()

        title = Label(
            self.current_frame,
            fg='black',
            bg='white',
            text=self.topic.get(),
            font='Lucida\\ Console 26 underline'
        )
        title.grid(row=0, column=0, columnspan=1, pady=50)

        global time_count
        time_count = Label(
            self.current_frame,
            fg='red',
            bg='skyblue1',
            text='00:00',
            font='Lucida\\ Console 22 bold'
        )
        time_count.grid(row=0, column=2, pady=50)

        place_holder = Message(
            self.current_frame,
            text=self.paragraph,
            fg='black',
            bg='ivory3',
            width=1000,
            justify='center',
            font='Verdana\\ Pro 18'
        )
        place_holder.grid(row=2, column=0, columnspan=3, padx=80, pady=40)

        self.user_input = Text(
            self.current_frame,
            width=80,
            height=10,
            bg='floral white',
            fg='black',
            insertbackground='green',
            borderwidth=5,
            relief=RAISED,
            padx=5,
            pady=5,
            font='Verdana\\ Pro 16')

        self.user_input.grid(row=3, column=0, columnspan=3, padx=30)

        self.user_input.bind('<KeyRelease>', self.key_release)
        self.user_input.focus()
        self.user_input.bind('<Control-x>', lambda e: 'break')  # disable cut
        self.user_input.bind('<Control-c>', lambda e: 'break')  # disable copy
        self.user_input.bind('<Control-v>', lambda e: 'break')  # disable paste
        self.user_input.bind('<Button-3>', lambda e: 'break')  # disable right-click

    def set_typing_home(self) -> None:
        '''Setting home environment for Typing Speed Test'''
        if (self.current_frame != None):
            self.clear_frame()

        self.para_count.set(0)
        self.topic.set(self.paragraph_topic[0])

        header = Label(
            self.current_frame,
            text='Select Paragraph For Test',
            font='rockwell 25 bold underline',
            bg='white', fg='black'
        )
        header.grid(row=0, column=1, pady=(40, 20))

        backward = Button(
            self.current_frame,
            text='<<',
            bg='lightblue1',
            fg='black',
            relief=RAISED,
            font='Helvetica 20',
            state=DISABLED,
            command=lambda: self.go_backward(
                backward,
                forward,
                title,
                place_holder
            )
        )

        title = Label(
            self.current_frame,
            fg='black',
            bg='white',
            text=self.topic.get(),
            font='Helvetica 22'
        )

        forward = Button(
            self.current_frame,
            text='>>',
            bg='lightblue1',
            fg='black',
            relief=RAISED,
            font='Helvetica 20',
            command=lambda: self.go_forward(
                backward,
                forward,
                title,
                place_holder)
        )

        backward.grid(row=1, column=0, pady=35)
        title.grid(row=1, column=1, pady=35)
        forward.grid(row=1, column=2, pady=(35))

        self.paragraph = get_paragraph_text(self.topic.get())

        place_holder = Message(
            self.current_frame,
            text=self.paragraph,
            fg='black',
            bg='ivory3',
            width=1000,
            justify='center',
            font='Verdana\\ Pro 18'
        )
        place_holder.grid(row=3, column=0, columnspan=3)

        start_test = Button(
            self.current_frame,
            text="Start Test",
            font='Verdana\\ Pro 15',
            borderwidth=3,
            bg='lightblue1',
            fg='black',
            relief=RAISED,
            command=self.start_typing
        )
        start_test.grid(row=4, column=1, pady=10)

        exit = Button(
            self.current_frame,
            text='Exit',
            font='Verdana\\ Pro 15',
            borderwidth=3,
            bg='lightblue1',
            fg='black',
            relief=RAISED,
            command=self.get_exit
        )
        exit.grid(row=5, column=1)