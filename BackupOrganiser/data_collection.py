class DataCollection:
    """
    Represents one data collection and its backups.
    """

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

            Args:
                name: Collection name.
                description: Collection description.
                creation_date: Creation date.
                modification_date: Last modification date.
                still_updated: True if collection is still maintained.
        """


        
        # Collection name
        self.name = name

        # Short description of the collection
        self.description = description

        # When the collection was created
        self.creation_date = creation_date

        # Last time the collection was modified
        self.modification_date = modification_date

        # True = still maintained
        # False = no longer updated
        self.still_updated = still_updated

        # List that will contain BackupEntry objects
        self.backups = []