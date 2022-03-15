import json

from cedarparsingutils.dto.ontology_value import OntologyValue


class ResourceType:
    """
    The DTO class parses a "10_ResourceType" element object from a DataHub general instance.
    """

    def __init__(self, type_detail: str, type_general: OntologyValue):
        self.type_detail: str = type_detail
        self.type_general: OntologyValue = type_general

    @classmethod
    def create_from_dict(cls, element: dict):
        type_detail = element["resourceTypeDetail"]["@value"]
        type_general = OntologyValue.create_from_dict(element["resourceTypeGeneral"])

        return cls(type_detail, type_general)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return ResourceType.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "@context": {
            "resourceTypeDetail": "https://schema.metadatacenter.org/properties/26faf602-2fd3-4e22-818b-32949c82b746",
            "resourceTypeGeneral": "https://schema.metadatacenter.org/properties/42039c05-9fe3-4e8a-b9f6-f97affc62d3c"
        },
        "resourceTypeDetail": {
            "@value": "Collection - Mock"
        },
        "resourceTypeGeneral": {
            "rdfs:label": "Collection",
            "@id": "http://vocab.fairdatacollective.org/gdmt/Collection"
        }
    }
    """
