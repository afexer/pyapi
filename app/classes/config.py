import os
from os import path

BASE_PATH = os.environ['BASE_PATH']


class Config:
    config_path = BASE_PATH+'app/configs/config.env'

    config = {
        # DEFAULT
        'DEFAULTS': ({
            'image_path': 'images/'
        }),

        # API
        'API': ({
            'api_db': '',
            'api_user': '',
            'api_password': '',
            'api_secret': '',
        }),
    }

    map = {
        'data_path': 'DEFAULTS',
        'api_db': 'API',
        'api_user': 'API',
        'api_password': 'API',
        'api_secret': 'API',
    }

    def __init__(self):
        if not path.exists(self.config_path):
            open(self.config_path, 'w').close()
            self.save_config()
        else:
            self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as f:
            for line in f:
                value = line.split("=")
                if len(value) > 1:
                    self.set(value[0], value[1].rstrip('\n'))

    def save_config(self):
        with open(self.config_path, 'a') as cf:
            for group, settings in self.config.items():
                if group == 'DEFAULTS':
                    continue
                cf.write("["+group+"]\n")
                for key, value in settings.items():
                    cf.write(key+"="+value+"\n")
                cf.write("\n")
            cf.close()

    def getConfig(self):
        conf = {}
        for group, settings in self.config.items():
            for key, value in settings.items():
                conf[key] = value
        return conf

    def setConfig(self, conf):
        if isinstance(conf, dict):
            for key, value in conf.items():
                self.set(key, value)

    def get(self, key):
        group = self.map[key]
        return self.config[group][key]

    def set(self, key, value):
        group = self.map[key]
        self.config[group][key] = value


config = Config()
