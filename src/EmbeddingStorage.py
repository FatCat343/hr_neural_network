from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct


class EmbeddingStorage:
    def __init__(self):
        self.dataBaseClient = QdrantClient("localhost", port=6333)
        self.collectionName = "test_collection"
        if len(self.dataBaseClient.get_collections().collections) == 0:
            self.dataBaseClient.create_collection(
                collection_name=self.collectionName,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )

    def add(self, embedding_id, embedding):
        self.dataBaseClient.upsert(
            collection_name=self.collectionName,
            wait=True,
            points=[PointStruct(id=str(embedding_id), vector=embedding, payload={"id": str(embedding_id)})]
        )

    def find_closest_to(self, tgt_embedding, count):
        search_result = self.dataBaseClient.search(
            collection_name=self.collectionName, query_vector=tgt_embedding, limit=count
        )
        return list(map(lambda x: x.id, search_result))


embedding_storage = EmbeddingStorage()
