class OntologyValue:
    """
    "datasetDateType": {
        "rdfs:label": "Submitted",
        "@id": "http://vocab.fairdatacollective.org/gdmt/Submitted"
    },
    """

    def __init__(self, uri: str, label: str):
        self.uri: str = uri
        self.label: str = label

    @classmethod
    def create_from_element(cls, value: dict):
        uri = value["@id"]
        label = value["rdfs:label"]

        return cls(uri, label)
