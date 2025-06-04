#!/bin/bash
set -e

echo "📥 Ingesting trace data into NLWeb (site = OtelTraces)"
python -m tools.db_load /Users/fabswill/Repos/LuxMentis/dotnet/CAPS/otelnlwebbetter/trace-export.jsonl OtelTraces

echo "🚀 Starting NLWeb server"
python app-file.py
