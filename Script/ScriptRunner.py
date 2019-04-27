from Services.ConfigLoader.Implementation.JSONConfigLoader import JSONConfigLoader
from Services.Logger.Implementation.Logging import Logging
from Services.Logger.Implementation.ConsoleLogger import ConsoleLogger
from Services.Logger.Implementation.TextFileLogger import TextFileLogger
from Services.FileService.Implementation.TextFileService import TextFileService
from Config.Constants.Constants import Constants
from ResultData.ResultData import ResultData
from Reporters.Implementation.ConsoleReporter import ConsoleReporter
from Reporters.Implementation.TextFileReporter import TextFileReporter
from selenium import webdriver


class ScriptRunner:
    def __init__(self):
        self.config = None
        self.browser = None

    def prep(self):
        parser = JSONConfigLoader("Config/Configurable/config.json")
        self.config = parser.parse()

        Logging.text_file_logger = TextFileLogger(self.config["LOG_FILE_PATH"], self.config["TXT_LOG_LEVEL"])
        Logging.console_logger = ConsoleLogger(self.config["CONSOLE_LOG_LEVEL"])
        Logging.init(self.config["TEXT_LOGGING"], self.config["CONSOLE_LOGGING"])
        Logging.start()

        options = webdriver.ChromeOptions()
        options.binary_location = self.config["PATH_TO_BINARY"]

        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)

        chrome_driver_binary = self.config["PATH_TO_DRIVER"]

        try:
            self.browser = webdriver.Chrome(chrome_driver_binary, options=options)
        except Exception:
            Logging.error("Couldn't properly start browser. Please check driver and binary and try again!")
            exit(self.config["SELENIUM_ERROR"])

    def run(self):
        Logging.info("Script run has started")
        try:
            self.browser.get(Constants.FACEBOOK_URL)
            self.browser.find_element_by_id(Constants.LOGIN_TAG_ID).send_keys(self.config["LOGIN"])
            self.browser.find_element_by_id(Constants.PASS_TAG_ID).send_keys(self.config["PASS"])
            self.browser.find_element_by_id(Constants.BUTTON_ID).click()
            self.browser.get(Constants.FRIEND_LIST_LINK)

            container = self.browser.find_element_by_id(Constants.FRIENDS_CONTAINER)
            friends_list = container.find_elements_by_tag_name("li")

            for item in friends_list:
                Logging.info("Reading next friends info")
                link_a = item.find_element_by_tag_name("a")
                link = link_a.get_attribute("href")
                name_a = item.find_elements_by_tag_name("a")[2]
                name = name_a.get_property("innerHTML")
                ResultData.names_and_links[name] = link

            self.browser.quit()
        except Exception:
            Logging.error("Something went wrong. Please re-launch the script!")
            exit(self.config["SELENIUM_ERROR"])

    def show_results(self):
        Logging.info("Showing results")
        console_reporter = ConsoleReporter()
        console_reporter.report()
        text_file_reporter = TextFileReporter(self.config["RESULT_FILE_PATH"], TextFileService(self.config))
        text_file_reporter.report()
