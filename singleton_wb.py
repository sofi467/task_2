from selenium import webdriver


class WebDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = webdriver.Chrome()
        return cls._instance

    @classmethod
    def quit(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None
