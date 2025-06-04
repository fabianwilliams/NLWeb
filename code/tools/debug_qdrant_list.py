from qdrant_client import QdrantClient
from pprint import pprint

# Connect to your running container on port 6333
client = QdrantClient(url="http://localhost:6333")

# List all collections
collections = client.get_collections().collections
print("✅ Collections in Qdrant:")
for coll in collections:
    print("-", coll.name)

# Try to pull first 5 points from each collection
for coll in collections:
    print(f"\n🔍 Inspecting collection: {coll.name}")
    try:
        response = client.scroll(
            collection_name=coll.name,
            limit=5,
            with_payload=True,
        )
        for point in response[0]:
            pprint(point.payload)
    except Exception as e:
        print(f"❌ Error inspecting collection '{coll.name}': {e}")
