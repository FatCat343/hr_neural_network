import uuid

from src.Embedder import embedder
from src.EmbeddingStorage import embedding_storage
from src.Summarizer import summarizer


class MatchingVacanciesService:
    def __init__(self):
        self.matching_resumes_threshold = 5

    def add_vacancy(self, vacancy_description):
        vacancy_id = uuid.uuid4()
        summarized = summarizer.summarize(vacancy_description)
        embedding = embedder.create_embedding(summarized)
        embedding_storage.add(vacancy_id, embedding)
        return vacancy_id

    def find_matching_for_resume(self, resume_description):
        summarized = summarizer.summarize(resume_description)
        embedding = embedder.create_embedding(summarized)
        return embedding_storage.find_closest_to(embedding, self.matching_resumes_threshold)


matchingVacanciesService = MatchingVacanciesService()
