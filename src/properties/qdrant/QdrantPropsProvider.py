from src.properties.PropertiesReader import propertiesReader


class QdrantPropsProvider:
    def __init__(self):
        self.host_prop_name = "host"
        self.port_prop_name = "port"
        self.collection_prop_name = "collection"

    def get_host(self):
        return propertiesReader.read_property(self.host_prop_name)

    def get_port(self):
        return propertiesReader.read_property(self.port_prop_name)

    def get_collection_name(self):
        return propertiesReader.read_property(self.collection_prop_name)


qdrantPropsProvider = QdrantPropsProvider()
