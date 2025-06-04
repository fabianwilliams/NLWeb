from qdrant_client import QdrantClient

# Adjust this if you're running remote or using API keys
client = QdrantClient(url="http://localhost:6333")

# List all collections
collections = client.get_collections()
print("✅ Collections in Qdrant:")
print([c.name for c in collections.collections])

# Inspect ContentfulFAQs specifically
collection = "nlweb_collection"
#collection = "nlweb_collection" 

if client.collection_exists(collection):
    count = client.count(collection_name=collection, exact=True)
    print(f"🔍 '{collection}' contains {count.count} vectors")
else:
    print(f"❌ Collection '{collection}' not found in Qdrant.")
