from abc import ABC, abstractmethod

class TypingFeature(ABC):
    '''abstract class for typing feature'''

    @abstractmethod
    def reset_data(self) -> None:
        '''Reset variables for next typing test'''
        pass

    def back_to_home(self) -> None:
        '''Return to home page'''
        pass