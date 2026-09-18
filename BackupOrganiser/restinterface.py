from flask import Flask, request, render_template
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
    return render_template("index.html")


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


@app.route("/api/Search")
def search():

    name = request.args.get("name")

    return {
        "collections": collection_manager.search(name)
    }


@app.route("/api/Edit", methods=["POST"])
def edit():

    data = request.get_json()

    success = collection_manager.edit(
        data["name"],
        data["modification_date"],
        data["still_updated"]
    )

    return {"success": success}

@app.route("/api/Delete", methods=["DELETE"])
def delete():

    name = request.args.get("name")

    success = collection_manager.delete(name)

    return {"success": success}


@app.route("/api/Unbackup", methods=["POST"])
def unbackup():

    data = request.get_json()

    collection = collection_manager.get(data["name"])

    if collection is None:
        return {"error": "Collection not found"}

    success = backup_manager.unbackup(
        collection,
        data["backupname"]
    )

    return {"success": success}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)