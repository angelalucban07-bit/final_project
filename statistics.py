class Statistics:
    def calculate_result(self) -> tuple:
        '''Calculating accuracy, actual accuracy, word per minute(wpm) and total time taken to type paragraph'''
        total_time = int(self.end_time - self.start_time)

        wpm = correct_letters = correct_words = accuracy = actual_accuracy = 0

        correct_flag = 1
        for para_char, user_char in zip(self.paragraph, self.get_user_text):
            if para_char == user_char:
                correct_letters += 1
            else:
                correct_flag = 0

            if para_char == ' ' or para_char == '\n' or para_char == '\t':
                correct_words += 1 if correct_flag == 1 else 0
                correct_flag = 1

        correct_words += 1 if correct_flag == 1 else 0
        wpm = correct_words / (float(total_time) / 60)

        accuracy = (correct_letters * 100) / len(self.paragraph)
        actual_accuracy = (correct_letters - self.backspace_count) * 100 / len(self.paragraph)

        return int(accuracy), int(actual_accuracy), int(wpm), self.formatted_time(total_time)

    def reset_data(self) -> None:
        self.start_flag = 0
        self.seconds = 0
        self.minutes = 0
        self.backspace_count = 0

    def back_to_home(self) -> None:
        self.reset_data()
        self.clear_frame()
        self.set_typing_home()
