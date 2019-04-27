from Services.ConfigLoader.API.ConfigLoader import ConfigLoader
from Services.Logger.Implementation.Logging import Logging
from Config.Constants.ConfigDefaults import ConfigDefaults
import json


class JSONConfigLoader(ConfigLoader):
    def __init__(self, path):
        self.path = path
        self.config = None

    def parse(self):
        try:
            with open(self.path) as json_file:
                self.config = json.load(json_file)
        except OSError:
            Logging.error("Couldn't parse JSON file")

        self.__verify()
        return self.config

    def __verify(self):
        self.__verify_paths()
        self.__verify_logs()
        self.__verify_credentials()
        self.__verify_error_codes()

    def __verify_paths(self):
        if type(self.config["PATH_TO_DRIVER"]) != str or self.config["PATH_TO_DRIVER"] == "":
            self.config["PATH_TO_DRIVER"] = ConfigDefaults.PATH_TO_DRIVER
        if type(self.config["PATH_TO_BINARY"]) != str or self.config["PATH_TO_BINARY"] == "":
            self.config["PATH_TO_BINARY"] = ConfigDefaults.PATH_TO_BINARY
        if type(self.config["LOG_FILE_PATH"]) != str or self.config["LOG_FILE_PATH"] == "":
            self.config["LOG_FILE_PATH"] = ConfigDefaults.LOG_FILE_PATH
        if type(self.config["RESULT_FILE_PATH"]) != str or self.config["RESULT_FILE_PATH"] == "":
            self.config["RESULT_FILE_PATH"] = ConfigDefaults.RESULT_FILE_PATH

    def __verify_logs(self):
        if type(self.config["TEXT_LOGGING"]) != int or not (-1 < self.config["TEXT_LOGGING"] < 2):
            self.config["TEXT_LOGGING"] = ConfigDefaults.TEXT_LOGGING
        if type(self.config["TXT_LOG_LEVEL"]) != int:
            self.config["TXT_LOG_LEVEL"] = ConfigDefaults.TXT_LOG_LEVEL
        if type(self.config["CONSOLE_LOGGING"]) != int or not (-1 < self.config["CONSOLE_LOGGING"] < 2):
            self.config["CONSOLE_LOGGING"] = ConfigDefaults.CONSOLE_LOGGING
        if type(self.config["CONSOLE_LOG_LEVEL"]) != int:
            self.config["CONSOLE_LOG_LEVEL"] = ConfigDefaults.CONSOLE_LOG_LEVEL

    def __verify_credentials(self):
        if type(self.config["LOGIN"]) != str or self.config["LOGIN"] == "":
            self.config["LOGIN"] = ConfigDefaults.LOGIN
        if type(self.config["PASS"]) != str or self.config["PASS"] == "":
            self.config["PASS"] = ConfigDefaults.PASS

    def __verify_error_codes(self):
        if type(self.config["FILE_OPEN_ERROR"]) != int:
            self.config["FILE_OPEN_ERROR"] = ConfigDefaults.FILE_OPEN_ERROR
        if type(self.config["SELENIUM_ERROR"]) != int:
            self.config["SELENIUM_ERROR"] = ConfigDefaults.SELENIUM_ERROR
