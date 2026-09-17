from data_collection import DataCollection


class CollectionManager:
    """
    Manages all data collections.
    """

    def __init__(self):
        """
        Creates an empty collection list.
        """

        # Stores all DataCollection objects
        self.collections = []

    def add_collection(
        self,
        name,
        description,
        creation_date,
        modification_date,
        updated
    ):
        """
        Creates and adds a new collection.
        """

        collection = DataCollection(
            name,
            description,
            creation_date,
            modification_date,
            updated
        )

        self.collections.append(collection)

    def get(self, collection_name):
        """
        Returns a collection by name.
        """

        for collection in self.collections:
            if collection.name == collection_name:
                return collection

        return None

    def overview(self):
        """
        Returns a simple overview of all collections.
        """

        result = []

        for collection in self.collections:
            result.append(collection.name)

        return result

    def detailed_overview(self):
        """
        Returns detailed information for all collections.
        """

        result = []

        for collection in self.collections:
            result.append([
                collection.name,
                collection.description,
                collection.creation_date,
                collection.modification_date,
                collection.still_updated
            ])

        return result

    def info(self, collection_name):
        """
        Returns detailed information about one collection.
        """

        collection = self.get(collection_name)

        if collection is None:
            return None

        return [
            collection.name,
            collection.description,
            collection.creation_date,
            collection.modification_date,
            collection.still_updated
        ]