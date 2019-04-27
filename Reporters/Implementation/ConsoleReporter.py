from Reporters.API.Reporter import Reporter
from Services.Logger.Implementation.Logging import Logging
from ResultData.ResultData import ResultData


class ConsoleReporter(Reporter):
    def __init__(self):
        pass

    def report(self):
        Logging.info("Started console reporting")
        for key, value in ResultData.names_and_links.items():
            print("{}: {}".format(key, value))
        pass
