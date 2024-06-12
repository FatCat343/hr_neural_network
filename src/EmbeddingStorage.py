from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct

from src.emdebbing.Embedder import embedder
from src.properties.qdrant.QdrantPropsProvider import qdrantPropsProvider


class EmbeddingStorage:
    def __init__(self):
        self.dataBaseClient = QdrantClient(
            location=qdrantPropsProvider.get_host(),
            port=qdrantPropsProvider.get_port()
        )
        embedding_size = embedder.get_embedding_size()
        self.collectionName = qdrantPropsProvider.get_collection_name()
        existed_collections = self.dataBaseClient.get_collections().collections
        collections_with_same_name = [x for x in existed_collections if x.name == self.collectionName]
        if len(collections_with_same_name) == 0:
            self.dataBaseClient.create_collection(
                collection_name=self.collectionName,
                vectors_config=VectorParams(size=embedding_size, distance=Distance.COSINE)
            )

    def add(self, embedding_id, embedding):
        self.dataBaseClient.upsert(
            collection_name=self.collectionName,
            wait=True,
            points=[PointStruct(id=str(embedding_id), vector=embedding, payload={"id": str(embedding_id)})]
        )

    def find_closest_to(self, tgt_embedding, count):
        search_result = self.dataBaseClient.search(
            collection_name=self.collectionName,
            query_vector=tgt_embedding,
            limit=count
        )
        return list(map(lambda x: x.id, search_result))


embedding_storage = EmbeddingStorage()
