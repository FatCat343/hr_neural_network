from sentence_transformers import SentenceTransformer


class EmbedderRu:
    def __init__(self):
        self.model = SentenceTransformer('cointegrated/rubert-tiny2')

    def create_embedding(self, text):
        embedding = self.model.encode(text)
        return embedding


embedderRu = EmbedderRu()
