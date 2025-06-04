from qdrant_client import QdrantClient
from qdrant_client.http import models
from pprint import pprint

# Connect to the running Qdrant instance
client = QdrantClient(url="http://localhost:6333")

# Name of the collection used in NLWeb config
collection_name = "nlweb_collection"

# Optional: Change this to any site label you want to inspect
site_filter_value = "ContentfulFAQs"

# Build a Qdrant filter by 'site'
filter_condition = models.Filter(
    must=[models.FieldCondition(key="site", match=models.MatchValue(value=site_filter_value))]
)

# Query for matching documents
response = client.scroll(
    collection_name=collection_name,
    scroll_filter=filter_condition,
    limit=10,
    with_payload=True
)

# Print the filtered results
print(f"\nDocuments in '{collection_name}' with site = '{site_filter_value}':\n")
for point in response[0]:
    pprint(point.payload)

if not response[0]:
    print("⚠️ No matching documents found.")
