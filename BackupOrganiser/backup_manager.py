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

        collection_object.backups.append({
            "name": backup_name,
            "date": backup_date,
            "location": backup_location
        })

    def unbackup(self, collection_object, backup_name):
            """
            Removes a backup from a collection.
            """

            for backup in collection_object.backups:

                if backup["name"] == backup_name:
                    collection_object.backups.remove(backup)
                    return True

            return False