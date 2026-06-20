from base_window import BaseWindow
import time

class Timer(BaseWindow):
    def update_timer(self, s_time) -> None:
        '''Update timer in minute and second'''
        current_time = time.time()

        if int(current_time - s_time) >= 0):
            self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        min_p = '{:0>2d}'.format(int(self.minutes))
        sec_p = '{:0>2d}'.format(int(self.seconds))

        time_count.config(text=f'{min_p}:{sec_p}')
        time_count.after(
        1000,
        lambda: self.update_timer(s_time)
        )

    def formatted_time(self, total_time) -> str:
        '''Formating total time in minutes and seconds'''
        time_format = ""
        time_format = '{:0>2d}'.format(int(total_time / 60))
        time_format += ':' + '{:0>2d}'.format(int(total_time % 60))
        return time_format

    def get_time(self):
        """Return current time as mm:ss"""
        return f"{self.minutes:02}:{self.seconds:02}"

    def get_total_seconds(self):
        """Return total elapsed seconds"""
        if self.running:
        return int(self.end_time - self.start_time)