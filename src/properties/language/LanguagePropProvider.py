from src.properties.PropertiesReader import propertiesReader
from src.properties.language.Language import Language


class LanguagePropProvider:
    def __init__(self):
        self.prop_name = "language"

    def get_language(self):
        prop_value = propertiesReader.read_property(self.prop_name)

        return self.__resolve_language(prop_value)

    def __resolve_language(self, prop_value):
        match prop_value:
            case 'en':
                return Language.EN
            case 'ru':
                return Language.RU


languagePropProvider = LanguagePropProvider()
