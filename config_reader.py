import json
import os


class ConfigReader:
    def __init__(self, config_file):
        self.config_path = os.path.abspath(config_file)
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def get_value(self, key):
        return self.config_data.get(key, '')
