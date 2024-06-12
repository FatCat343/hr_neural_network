from InstructorEmbedding import INSTRUCTOR


class EmbedderEn:
    def __init__(self):
        self.internalEmbedderModel = INSTRUCTOR('hkunlp/instructor-large')
        self.internalEmbedderInstruction = "Represent the HR document"

    def create_embedding(self, text):
        return self.internalEmbedderModel.encode(
            [[self.internalEmbedderInstruction, text]],
            show_progress_bar=True)[0]


embedderEn = EmbedderEn()
