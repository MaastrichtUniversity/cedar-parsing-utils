from cedarparsingutils.dto.ontology_value import OntologyValue


class ResourceType:
    """
    "10_ResourceType": {
        "@context": {
            "resourceTypeDetail": "https://schema.metadatacenter.org/properties/26faf602-2fd3-4e22-818b-32949c82b746",
            "resourceTypeGeneral": "https://schema.metadatacenter.org/properties/42039c05-9fe3-4e8a-b9f6-f97affc62d3c"
        },
        "resourceTypeDetail": {
            "@value": "Collection"
        },
        "resourceTypeGeneral": {
            "rdfs:label": "Collection",
            "@id": "http://vocab.fairdatacollective.org/gdmt/Collection"
        }
    },
    """

    def __init__(self, type_detail: str, type_general: OntologyValue):
        self.type_detail: str = type_detail
        self.type_general: OntologyValue = type_general

    @classmethod
    def create_from_element(cls, element: dict):
        type_detail = element["resourceTypeDetail"]["@value"]
        type_general = OntologyValue.create_from_element(element["resourceTypeGeneral"])

        return cls(type_detail, type_general)
