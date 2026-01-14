from typing import Dict
import os

from pymongo import MongoClient

# Module-level variable to hold a lazily-created MongoClient instance.
# Starts as None and will be set by `get_client()` on first use.
_mongo_client = None


def get_client():
    # Tell Python we mean the module-level `_mongo_client`, not a local var.
    global _mongo_client
    # If no client exists yet, create one using the MONGO_URI env var.
    if _mongo_client is None:
        # Read the `MONGO_URI` environment variable; if absent, default to localhost.
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        # Create a new MongoClient connected to the given URI and store it.
        _mongo_client = MongoClient(uri)
    # Return the cached MongoClient instance.
    return _mongo_client


def get_db(name: str = "lazynews"):
    """Return a MongoDB database object (creates client lazily)."""
    # Use the client to get (and return) the database with the given name.
    return get_client()[name]


def save_news(breaking_news: Dict[str, dict], db_name: str = "lazynews", collection: str = "news") -> None:
    """Save breaking news mapping (URL -> {title, main_content}) into MongoDB.

    Each document uses the URL as `_id` so records are upserted.
    """
    # Get the collection object from the requested database.
    coll = get_db(db_name)[collection]
    # Iterate over the mapping where keys are URLs and values are dicts.
    for url, item in breaking_news.items():
        # Build the document to store; use the URL as the `_id` field.
        doc = {"_id": url, "title": item.get("title", ""), "main_content": item.get("main_content", "")}
        # Replace the existing document with the same _id or insert if missing.
        coll.replace_one({"_id": url}, doc, upsert=True)


def get_news(db_name: str = "lazynews", collection: str = "news") -> Dict[str, dict]:
    """Return a mapping URL -> {title, main_content} from MongoDB."""
    # Access the collection to read documents.
    coll = get_db(db_name)[collection]
    # Prepare an empty dict to collect results.
    out: Dict[str, dict] = {}
    # Iterate all documents in the collection.
    for d in coll.find():
        # Each document stores the URL in the `_id` field.
        url = d.get("_id")
        # Map the URL to a smaller dict with title and main_content (safe defaults).
        out[url] = {"title": d.get("title", ""), "main_content": d.get("main_content", "")}
    # Return the assembled mapping.
    return out


def save_summary(summary: Dict[str, dict], db_name: str = "lazynews", collection: str = "summaries") -> None:
    """Save summaries mapping (URL -> {title, summary}) into MongoDB."""
    # Get the target collection in the specified database.
    coll = get_db(db_name)[collection]
    # For each URL -> item pair, upsert a document with the summary.
    for url, item in summary.items():
        doc = {"_id": url, "title": item.get("title", ""), "summary": item.get("summary", "")}
        coll.replace_one({"_id": url}, doc, upsert=True)


def get_summary(db_name: str = "lazynews", collection: str = "summaries") -> Dict[str, dict]:
    """Return a mapping URL -> {title, summary} from MongoDB."""
    # Read from the summaries collection.
    coll = get_db(db_name)[collection]
    out: Dict[str, dict] = {}
    # Iterate all documents and extract the fields we care about.
    for d in coll.find():
        url = d.get("_id")
        out[url] = {"title": d.get("title", ""), "summary": d.get("summary", "")}
    # Return the mapping of URL to summary info.
    return out
