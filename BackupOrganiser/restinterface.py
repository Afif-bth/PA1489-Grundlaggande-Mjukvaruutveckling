from flask import Flask, request, render_template
from collection_manager import CollectionManager
from backup_manager import BackupManager
# restinterface.py is the main entry point for the REST interface of the Backup Organiser application. It sets up the Flask application, defines the API endpoints, and handles requests related to data collections and backups.
app = Flask(__name__)

# Managers , we create instances of CollectionManager and BackupManager to handle the operations related to data collections and backups, respectively.
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

# Home endpoint
@app.route("/")
def home():
    return render_template("index.html")


# Overview endpoint
@app.route("/api/Overview")
def overview():
    return collection_manager.overview_json()


# List endpoint
@app.route("/api/List")
def list_collections():
    return collection_manager.detailed_overview_json()


# Info endpoint
@app.route("/api/Info")
def info():
    name = request.args.get("name")
    return collection_manager.info_json(name)



# -----
# Add Collection endpoint
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


# Add Backup endpoint
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

# Search endpoint
@app.route("/api/Search")
def search():

    name = request.args.get("name")

    return {
        "collections": collection_manager.search(name)
    }

# Edit endpoint
@app.route("/api/Edit", methods=["POST"])
def edit():

    data = request.get_json()

    success = collection_manager.edit(
        data["name"],
        data["modification_date"],
        data["still_updated"]
    )

    return {"success": success}

# Delete endpoint
@app.route("/api/Delete", methods=["DELETE"])
def delete():

    name = request.args.get("name", "")

    success = collection_manager.delete(name)

    return {"success": success}

# Unbackup endpoint
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

    # running the application : 
    # source .venv/bin/activate
    #   python3 restinterface.py
    #   http://localhost:5000
    #   docker compose build
    #   docker compose up



