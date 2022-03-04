from cedarparsingutils.dto.ontology_value import OntologyValue


class Identifier:
    """
    "1_Identifier": {
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
    },
    """

    def __init__(self, pid: str, type: OntologyValue):
        self.pid: str = pid
        self.type: OntologyValue = type

    @classmethod
    def create_from_element(cls, element: dict):
        pid = element["datasetIdentifier"]["@value"]
        type = OntologyValue.create_from_element(element["datasetIdentifierType"])

        return cls(pid, type)
