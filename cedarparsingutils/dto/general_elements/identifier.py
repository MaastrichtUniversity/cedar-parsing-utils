import json

from cedarparsingutils.dto.ontology_value import OntologyValue


class Identifier:
    """
    The DTO class parses a "1_Identifier" element object from a DataHub general instance.
    """

    def __init__(self, pid: str, type: OntologyValue):
        self.pid: str = pid
        self.type: OntologyValue = type

    @classmethod
    def create_from_dict(cls, element: dict):
        pid = element["datasetIdentifier"]["@value"]
        type = OntologyValue.create_from_dict(element["datasetIdentifierType"])

        return cls(pid, type)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Identifier.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "datasetIdentifier": {
            "@value": "https://hdl.handle.net/21.12109/P000000001C000000024.2"
        },
        "datasetIdentifierType": {
            "rdfs:label": "Handle",
            "@id": "http://vocab.fairdatacollective.org/gdmt/Handle"
        },
        "@context": {
            "datasetIdentifier": "http://purl.org/dc/terms/identifier",
            "datasetIdentifierType": "http://purl.org/spar/datacite/usesIdentifierScheme"
        }
    }
    """
