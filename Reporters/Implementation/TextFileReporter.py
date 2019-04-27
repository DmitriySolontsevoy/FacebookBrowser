from Reporters.API.Reporter import Reporter
from Services.Logger.Implementation.Logging import Logging
from ResultData.ResultData import ResultData


class TextFileReporter(Reporter):
    def __init__(self, path, file_service):
        self.path = path
        self.file_service = file_service
        self.file = None

    def report(self):
        Logging.info("Attempting to open file for report writing: " + self.path)
        self.file = self.file_service.open_file(self.path, "w")
        for key, value in ResultData.names_and_links.items():
            self.file_service.write_line(self.file, "{}: {}".format(key, value))
        pass
