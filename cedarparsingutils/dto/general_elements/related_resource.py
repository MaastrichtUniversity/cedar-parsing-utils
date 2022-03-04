from cedarparsingutils.dto.ontology_value import OntologyValue


class RelatedResource:
    """
    {
        "relationType": {
            "rdfs:label": "Requires",
            "@id": "http://vocab.fairdatacollective.org/gdmt/Requires"
        },
        "relatedResourceIdentifierType": {
            "rdfs:label": "EISSN",
            "@id": "http://vocab.fairdatacollective.org/gdmt/EISSN"
        },
        "relatedResourceIdentifier": {
            "@value": "123456789"
        },
        "@context": {
            "relationType": "http://rs.tdwg.org/dwc/terms/relationshipOfResource",
            "relatedResourceIdentifierType": "http://schema.org/propertyID",
            "relatedResourceIdentifier": "http://purl.org/dc/terms/identifier"
        }
    }
    """

    def __init__(self, identifier: str, identifier_type: OntologyValue, relation_type: OntologyValue):
        self.identifier: str = identifier
        self.identifier_type: OntologyValue = identifier_type
        self.relation_type: OntologyValue = relation_type

    @classmethod
    def create_from_element(cls, element: dict):
        identifier = element["relatedResourceIdentifier"]["@value"]
        identifier_type = OntologyValue.create_from_element(element["relatedResourceIdentifierType"])
        relation_type = OntologyValue.create_from_element(element["relationType"])

        return cls(identifier, identifier_type, relation_type)
