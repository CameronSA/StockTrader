class Strategy:
    def __init__(self):
        self.__long_term_increasing = 'long_term_increasing'
        self.__indicators = 'indicators'
        self.__long_term_decreasing = 'long_term_decreasing'

    @property
    def long_term_increasing(self):
        return self.__long_term_increasing

    @property
    def long_term_decreasing(self):
        return self.__long_term_decreasing

    @property
    def indicators(self):
        return self.__indicators
