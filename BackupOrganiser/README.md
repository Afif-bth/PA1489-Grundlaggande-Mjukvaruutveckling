# BackupOrganiser

## Course
PA1489 – Grundläggande mjukvaruutveckling

## Assignment 2
Implementation and Documentation

---

## Project Description

BackupOrganiser is a small web application used to keep track of data collections and their backups.

A data collection contains:

- Name
- Description
- Creation date
- Last modification date
- Still updated (True/False)
- List of backups

A backup contains:

- Name
- Date
- Location

The application follows the CRUD pattern:

- Create
- Read
- Update
- Delete

---
# TA Presentation Notes

## Start application

Run:

```bash
docker compose up
```

Open:

```text
http://localhost:5000
```

---

## Show Add Collection

Endpoint:

```text
POST /api/Collection
```

Source code:

```text
restinterface.py
```

Function:

```python
def add_collection():
```

Uses:

```python
collection_manager.add_collection(...)
```

---

## Show Overview

Endpoint:

```text
GET /api/Overview
```

Source code:

```text
restinterface.py
```

Uses:

```python
collection_manager.overview_json()
```

Implementation:

```text
collection_manager.py
```

Method:

```python
def overview_json():
```

---

## Show Detailed List

Endpoint:

```text
GET /api/List
```

Source code:

```text
restinterface.py
```

Uses:

```python
collection_manager.detailed_overview_json()
```

Implementation:

```text
collection_manager.py
```

---

## Show Info

Endpoint:

```text
GET /api/Info?name=Photos
```

Source code:

```text
restinterface.py
```

Uses:

```python
collection_manager.info_json()
```

Implementation:

```text
collection_manager.py
```

---

## Show Search

Endpoint:

```text
GET /api/Search?name=Pho
```

Source code:

```text
restinterface.py
```

Implementation:

```python
def search()
```

File:

```text
collection_manager.py
```

---

## Show Add Backup

Endpoint:

```text
POST /api/Backup
```

Source code:

```text
restinterface.py
```

Uses:

```python
backup_manager.add_backup()
```

Implementation:

```text
backup_manager.py
```

---

## Show Edit Collection

Endpoint:

```text
POST /api/Edit
```

Implementation:

```python
def edit()
```

File:

```text
collection_manager.py
```

---

## Show Delete Collection

Endpoint:

```text
DELETE /api/Delete
```

Implementation:

```python
def delete()
```

File:

```text
collection_manager.py
```

---

## Show Remove Backup

Endpoint:

```text
POST /api/Unbackup
```

Implementation:

```python
def unbackup()
```

File:

```text
backup_manager.py
```

---

## Class Overview

### DataCollection

File:

```text
data_collection.py
```

Stores collection information.

---

### BackupEntry

File:

```text
backup_entry.py
```

Stores backup information.

---

### CollectionManager

File:

```text
collection_manager.py
```

Manages collections.

---

### BackupManager

File:

```text
backup_manager.py
```

Manages backups.

---

### RestInterface

File:

```text
restinterface.py
```

Provides the Flask REST API.




---

## Implemented Functionality

### Create

- Add Collection
- Add Backup

### Read

- Overview of Collections
- Detailed List of Collections
- Detailed Information about one Collection
- Search Collections

### Update

- Edit Collection

### Delete

- Delete Collection
- Remove Backup (Unbackup)

---

## Project Structure

### DataCollection

Represents one data collection and stores:

- Name
- Description
- Dates
- Update status
- Backup list

### BackupEntry

Represents one backup entry.

### CollectionManager

Responsible for managing all collections.

Functions:

- add_collection()
- get()
- overview()
- detailed_overview()
- info()
- search()
- edit()
- delete()

### BackupManager

Responsible for managing backups.

Functions:

- add_backup()
- unbackup()

### RestInterface

Provides HTTP endpoints using Flask.

---

## REST API Endpoints

### GET

```text
/api/Overview
/api/List
/api/Info?name=<collection>
/api/Search?name=<text>
```

### POST

```text
/api/Collection
/api/Backup
/api/Edit
/api/Unbackup
```

### DELETE

```text
/api/Delete?name=<collection>
```

---

## Technologies Used

- Python 3
- Flask
- Docker
- Docker Compose

---

## Running the Application

### Local

```bash
python3 restinterface.py
```

Open:

```text
http://localhost:5000
```

### Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Open:

```text
http://localhost:5000
```

---

## Demonstration for TA

The following functionality can be demonstrated:

- Add Collection
- View Overview
- View Detailed List
- View Collection Info
- Search Collections
- Add Backup
- Edit Collection
- Delete Collection
- Remove Backup

The application can be started using Docker and accessed through a web browser.

---

## Questions the TA May Ask

### What is DataCollection?

Stores information about one collection and its backups.

### What is CollectionManager?

Manages all collections and provides CRUD operations.

### What is BackupManager?

Manages backup entries for collections.

### What is Flask?

A Python web framework used to create REST APIs.

### What is an API endpoint?

A URL that provides access to application functionality.

Example:

```text
/api/Overview
```

returns information about all collections.

### Why Docker?

Docker makes the application run consistently on different computers without additional setup.

---
# Questions for TA

## 1. What is the purpose of BackupOrganiser?

BackupOrganiser is a CRUD application used to manage data collections and their backups.

A collection contains:

- name
- description
- creation date
- modification date
- still updated
- backups

A backup contains:

- name
- date
- location

---

## 2. What does DataCollection do?

File:

```text
data_collection.py
```

Represents one collection.

Stores:

- name
- description
- creation_date
- modification_date
- still_updated
- backups

---

## 3. What does BackupEntry do?

File:

```text
backup_entry.py
```

Represents one backup.

Stores:

- name
- date
- location

---

## 4. What does CollectionManager do?

File:

```text
collection_manager.py
```

Manages all collections.

Important methods:

```python
add_collection()
get()
overview()
detailed_overview()
info()
search()
edit()
delete()
```

---

## 5. What does BackupManager do?

File:

```text
backup_manager.py
```

Manages backups.

Important methods:

```python
add_backup()
unbackup()
```

---

## 6. What does restinterface.py do?

File:

```text
restinterface.py
```

Creates the Flask web application and REST API endpoints.

Examples:

```text
/api/Overview
/api/List
/api/Info
/api/Search
/api/Collection
/api/Backup
/api/Edit
/api/Delete
/api/Unbackup
```

---

## 7. What is Flask?

Flask is a Python web framework used to build web applications and REST APIs.

---

## 8. What is an API endpoint?

An endpoint is a URL that provides access to application functionality.

Example:

```text
/api/Overview
```

Returns information about all collections.

---

## 9. What is Docker?

Docker is used to package and run the application in a container.

This ensures the application runs the same way on different computers.

Run:

```bash
docker compose up
```

---

## 10. How is Add Collection implemented?

1. User sends a POST request to:

```text
/api/Collection
```

2. Flask receives the JSON data.

3. CollectionManager.add_collection() creates a new DataCollection object.

4. The collection is added to the collections list.

---

## 11. How is Add Backup implemented?

1. User sends a POST request to:

```text
/api/Backup
```

2. Flask finds the collection using:

```python
collection_manager.get()
```

3. BackupManager.add_backup() creates a backup.

4. The backup is added to:

```python
collection.backups
```

---

## 12. How is Search implemented?

File:

```text
collection_manager.py
```

Method:

```python
search()
```

The method loops through all collections and checks if the search text exists in the collection name.

---

## 13. Why did you use classes?

To separate responsibilities:

- DataCollection → collection data
- BackupEntry → backup data
- CollectionManager → collection operations
- BackupManager → backup operations

This makes the code easier to maintain and understand.

---

## 14. How do you start the application?

Local:

```bash
python3 restinterface.py
```

Docker:

```bash
docker compose up
```

Open:

```text
http://localhost:5000
```
---
## Author

Afif Mohammed