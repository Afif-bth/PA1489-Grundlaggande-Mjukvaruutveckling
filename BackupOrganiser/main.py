from collection_manager import CollectionManager
from backup_manager import BackupManager


def main():

    # Create managers
    collection_manager = CollectionManager()
    backup_manager = BackupManager()

    # Add collection
    collection_manager.add_collection(
        "Photos",
        "Family photos",
        "2026-09-01",
        "2026-09-10",
        True
    )

    # Get collection
    photos = collection_manager.get("Photos")

    # Add backup
    backup_manager.add_backup(
        photos,
        "USB Backup",
        "2026-09-15",
        "USB Drive"
    )

    # Test methods
    print("Overview:")
    print(collection_manager.overview())

    print("\nDetailed overview:")
    print(collection_manager.detailed_overview())

    print("\nInfo:")
    print(collection_manager.info("Photos"))


if __name__ == "__main__":
    main()