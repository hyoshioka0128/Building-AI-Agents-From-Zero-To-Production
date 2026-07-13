"""
Setup Vector Store - Creates a Microsoft Foundry vector store for the Employee Search Agent

This is a one-time setup script. It:
1. Creates a vector store in your Microsoft Foundry project
2. Uploads the Zava employee directory (../data/employees.md) into it
3. Prints the VECTOR_STORE_ID to copy into your .env file

The Employee Search Agent (employee-search-agent.py) reads VECTOR_STORE_ID and uses the
Microsoft Foundry hosted file search tool to answer questions about the directory.

Prerequisites:
- az login  (see the lesson README)
- FOUNDRY_PROJECT_ENDPOINT set in your .env

Usage:
    python setup_vector_store.py
"""

import os
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

# The employee directory lives at the repository root under data/employees.md
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "employees.md"


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Employee data file not found: {DATA_FILE}")

    endpoint = os.environ.get("FOUNDRY_PROJECT_ENDPOINT") or os.environ.get(
        "AZURE_AI_PROJECT_ENDPOINT"
    )
    if not endpoint:
        raise EnvironmentError(
            "Set FOUNDRY_PROJECT_ENDPOINT in your .env "
            "(Foundry portal -> your project -> Overview -> Endpoints)."
        )

    project_client = AIProjectClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential(),
        api_version="2025-11-15-preview",
    )
    openai_client = project_client.get_openai_client()

    print("Creating vector store 'zava-employee-directory'...")
    vector_store = openai_client.vector_stores.create(name="zava-employee-directory")

    print(f"Uploading {DATA_FILE.name} ...")
    with DATA_FILE.open("rb") as f:
        batch = openai_client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id,
            files=[f],
        )

    print(f"Upload status: {batch.status}  (files: {batch.file_counts})")
    print()
    print("Vector store ready. Add this line to your .env file:")
    print()
    print(f"    VECTOR_STORE_ID={vector_store.id}")


if __name__ == "__main__":
    main()
