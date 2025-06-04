import os
import json
from pathlib import Path
from dotenv import load_dotenv
from contentful import Client

load_dotenv()

# Load environment variables
SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

assert SPACE_ID and ACCESS_TOKEN, "Missing Contentful credentials"

client = Client(SPACE_ID, ACCESS_TOKEN)

# Extract plain text from Contentful rich text
def extract_text(node):
    if isinstance(node, dict):
        if node.get("nodeType") == "text":
            return node.get("value", "")
        return " ".join(extract_text(c) for c in node.get("content", []))
    elif isinstance(node, list):
        return " ".join(extract_text(c) for c in node)
    return ""

# Fetch FAQ entries
entries = client.entries({'content_type': 'faq'})
print(f"Fetched {len(entries)} FAQs")

# Prepare output path
output_path = Path("content/faqs.jsonl")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Write to JSONL (as tab-separated: URL \t JSON)
with output_path.open("w") as f:
    for i, entry in enumerate(entries):
        question = entry.fields().get("question", "(No question)")
        answer_obj = entry.fields().get("answer", {})
        rendered_answer = extract_text(answer_obj).strip()

        schema = {
            "@type": "FAQPage",
            "question": question,
            "answer": rendered_answer
        }

        url = f"https://andmyagent.com/faq#q{i+1}"
        f.write(f"{url}\t{json.dumps(schema)}\n")

print(f"✅ Saved {len(entries)} entries to {output_path}")
