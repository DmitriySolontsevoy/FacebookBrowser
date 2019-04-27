import abc


class Reporter:
    @abc.abstractmethod
    def report(self):
        pass
