from flask import Flask, request

from collection_manager import CollectionManager
from backup_manager import BackupManager

app = Flask(__name__)

# Managers
collection_manager = CollectionManager()
backup_manager = BackupManager()

# Test data
collection_manager.add_collection(
    "Photos",
    "Family photos",
    "2026-09-01",
    "2026-09-10",
    True
)


@app.route("/")
def home():
    return "BackupOrganiser Running"


# GET /api/Overview
@app.route("/api/Overview")
def overview():
    return collection_manager.overview_json()


# GET /api/List
@app.route("/api/List")
def list_collections():
    return collection_manager.detailed_overview_json()


# GET /api/Info?name=Photos
@app.route("/api/Info")
def info():
    name = request.args.get("name")
    return collection_manager.info_json(name)



# -----
# POST /api/Collection
@app.route("/api/Collection", methods=["POST"])
def add_collection():

    data = request.get_json()

    collection_manager.add_collection(
        data["name"],
        data["description"],
        data["creation_date"],
        data["modification_date"],
        data["still_updated"]
    )

    return {"message": "Collection added"}


# POST /api/Backup
@app.route("/api/Backup", methods=["POST"])
def add_backup():

    data = request.get_json()

    collection = collection_manager.get(data["name"])

    if collection is None:
        return {"error": "Collection not found"}

    backup_manager.add_backup(
        collection,
        data["backupname"],
        data["date"],
        data["location"]
    )

    return {"message": "Backup added"}

if __name__ == "__main__":
    app.run(debug=True)