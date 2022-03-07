import json


class OntologyValue:
    """
    The DTO class parses an ontology object from a Cedar element.
    """

    def __init__(self, uri: str, label: str):
        self.uri: str = uri
        self.label: str = label

    @classmethod
    def create_from_dict(cls, value: dict):
        if not value:
            return cls("", "")

        uri = value["@id"]
        label = value["rdfs:label"]

        return cls(uri, label)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return OntologyValue.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """    
    {
        "rdfs:label": "Submitted",
        "@id": "http://vocab.fairdatacollective.org/gdmt/Submitted"
    }
    """
