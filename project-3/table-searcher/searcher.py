from index_schema import schema
from embedder import Embedder
from dto import TableDto
import pymilvus as pm


def search(query: str, embedder: Embedder, function_name: str, paper_ids: list[str], use_hybrid: bool) -> list[TableDto]:
    tables_dto: list[TableDto] = []
    query_vector = embedder.get_sentence_embedding(query).tolist()

    search_params = {"metric_type": "COSINE", "params": {"nprobe": 200}}
    collection_name = ("table_" + embedder.model_name + "_" + function_name).replace("/", "_").replace("-", "_")
    collection = pm.Collection(name=collection_name, schema=schema)

    results = collection.search(
        data=[query_vector],
        anns_field="vector",
        param=search_params,
        limit=50,
        output_fields=["id", "paper_id", "table_id"]
    )

    for hits in results:
        for hit in hits:
            if not use_hybrid or (hit.entity.get('paper_id') in paper_ids):
                tables_dto.append(TableDto(hit.entity.get('paper_id'), hit.entity.get('table_id'), hit.distance))

    return tables_dto