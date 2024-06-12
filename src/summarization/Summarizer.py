from src.properties.language.Language import Language
from src.properties.language.LanguagePropProvider import languagePropProvider
from src.summarization.SummarizerEn import summarizerEn
from src.summarization.SummarizerRu import summarizerRu


class Summarizer:
    def __init__(self):
        self.language = languagePropProvider.get_language()

    def summarize(self, text):
        return self.__resolve_summarizer().summarize(text)

    def __resolve_summarizer(self):
        match self.language:
            case Language.EN:
                return summarizerEn
            case Language.RU:
                return summarizerRu


summarizer = Summarizer()
