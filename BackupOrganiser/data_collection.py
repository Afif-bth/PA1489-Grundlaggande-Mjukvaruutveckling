class DataCollection:
    """
    Represents one data collection and its backups.
    """
    # Initializes a new data collection with the given name, description, creation date, modification date, and still_updated status.
    def __init__(
        self,
        name,
        description,
        creation_date,
        modification_date,
        still_updated
    ):
        """
        Creates a new data collection.
        """
        # Name of the collection and its description 
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.still_updated = still_updated

        # List of backups
        self.backups = []

    # Returns a JSON representation of the collection and its backups.
    def full_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "modification_date": self.modification_date,
            "still_updated": self.still_updated,
            "backups": self.backups
        }