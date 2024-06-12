import os.path

from jproperties import Properties


class PropertiesReader:
    def __init__(self):
        self.configs = Properties()

        rel_path = "application.properties"
        prop_path = os.path.join(os.path.dirname(__file__), rel_path)
        with open(prop_path, 'rb') as config_file:
            self.configs.load(config_file)

    def read_property(self, property_name):
        return self.configs.get(property_name).data


propertiesReader = PropertiesReader()
