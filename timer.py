class Timer:
    def __init__(self):
        self.__start_time = 0
        self.__end_time = 0

    def start(self):
        self.__start_time = time.time()

    def stop(self):
        self.__end_time = time.time()

    def get_elapsed_time(self):
        return int(self.__end_time - self.__start_time)