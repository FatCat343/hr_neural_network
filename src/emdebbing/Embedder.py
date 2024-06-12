from src.emdebbing.EmbedderEn import embedderEn
from src.emdebbing.EmbedderRu import embedderRu
from src.properties.language.Language import Language
from src.properties.language.LanguagePropProvider import languagePropProvider


class Embedder:
    def __init__(self):
        self.language = languagePropProvider.get_language()

    def create_embedding(self, text):
        return self.__resolve_embedder().create_embedding(text)

    def get_embedding_size(self):
        match self.language:
            case Language.EN:
                return 768
            case Language.RU:
                return 312

    def __resolve_embedder(self):
        match self.language:
            case Language.EN:
                return embedderEn
            case Language.RU:
                return embedderRu


embedder = Embedder()
