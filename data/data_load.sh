#!/bin/sh
echo "Waiting for Elasticsearch to start..."
sleep 40  # Adjust this if needed

echo "Creating index..."
curl -X PUT "http://elasticsearch:9200/products" -H "Content-Type: application/json" -d create_index.json

echo "Checking index..."
curl -X GET "http://elasticsearch:9200/_cat/indices?v"

echo "Loading data..."
curl -X POST "http://elasticsearch:9200/_bulk" -H "Content-Type: application/json" --data-binary @bulk_data.json

echo "Data loaded successfully!"
