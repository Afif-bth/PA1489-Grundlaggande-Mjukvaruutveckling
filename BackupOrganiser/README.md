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

## Author

Afif Mohammed