from backup_entry import BackupEntry


class BackupManager:
    """
    Manages backups for collections.
    """

    def add_backup(
        self,
        collection_object,
        backup_name,
        backup_date,
        backup_location
    ):
        """
        Adds a backup to a collection.
        """

        backup = BackupEntry(
            backup_name,
            backup_date,
            backup_location
        )

        collection_object.backups.append(backup)