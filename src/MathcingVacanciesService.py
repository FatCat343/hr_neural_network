import uuid

from src.emdebbing.Embedder import embedder
from src.EmbeddingStorage import embedding_storage
from src.summarization.Summarizer import summarizer


class MatchingVacanciesService:

    def add_candidate(self, candidate_description):
        candidate_id = uuid.uuid4()
        summarized = summarizer.summarize(candidate_description)
        embedding = embedder.create_embedding(summarized)
        embedding_storage.add(candidate_id, embedding)
        return candidate_id

    def find_matching_for_resume(self, resume_description, count):
        summarized = summarizer.summarize(resume_description)
        embedding = embedder.create_embedding(summarized)
        return embedding_storage.find_closest_to(embedding, count)


matchingVacanciesService = MatchingVacanciesService()
