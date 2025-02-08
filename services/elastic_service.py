import json
import os

from elasticsearch import Elasticsearch


class ElasticService:
    # ELASTIC_URL = "http://localhost:9200/"
    INDEX = "products"

    def __init__(self):
        # Connect to Elasticsearch
        elastic_url = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
        self.es = Elasticsearch(elastic_url)

        # Check if the connection is successful
        if self.es.ping():
            print("Connected to Elasticsearch!")
            count_response = self.es.count(index="products")
            print(count_response["count"])

        else:
            print("Could not connect to Elasticsearch.")

    def search(self, keyword: str):
        query = {
            "query": {
                "term": {
                    "category": {
                        "value": keyword
                    }
                }
            }
        }
        search_response = self.es.search(index="products", body=query)
        hits = search_response["hits"]["hits"]
        return [item["_source"]["name"] for item in hits]
