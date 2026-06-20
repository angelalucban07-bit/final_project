from timer import Timer

class Statistics(Timer):
    start_time: float
    end_time: float
    paragraph: str
    _get_user_text: str

    def calculate_result(self) -> tuple:
        """Calculating accuracy, actual accuracy, word per minute(wpm) and total time taken to type paragraph"""

        total_time = int(self.end_time - self.start_time)
        if total_time == 0:
            total_time = 1

        correct_letters = 0
        correct_words = 0

        correct_flag = 1

        for para_char, user_char in zip(
                self.paragraph,
                self._get_user_text
        ):
            if para_char == user_char:
                correct_letters += 1
            else:
                correct_flag = 0

            if (
                para_char == ' '
                or para_char == '\n'
                or para_char == '\t'
            ):
                correct_words += 1 if correct_flag == 1 else 0
                correct_flag = 1

        correct_words += 1 if correct_flag == 1 else 0

        wpm = correct_words / (float(total_time) / 60)

        accuracy = (
            correct_letters * 100
        ) / len(self.paragraph)

        actual_accuracy = (
            (correct_letters - self._backspace_count)
            * 100
        ) / len(self.paragraph)

        return (
            int(accuracy),
            int(actual_accuracy),
            int(wpm),
            self.formatted_time(total_time)
        )
