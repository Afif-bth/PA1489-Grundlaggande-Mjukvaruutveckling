class BackupEntry:
    """
    Represents one backup entry.
    """

    def __init__(self, name, date, location):
        """
        Creates a new backup entry.

        Args:
            name: Backup name.
            date: Backup date.
            location: Where the backup is stored.
        """

        # Name of the backup
        self.name = name

        # Date when backup was created
        self.date = date

        # Backup location
        self.location = location