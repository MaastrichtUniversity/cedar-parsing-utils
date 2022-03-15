from cedarparsingutils.dto.ontology_value import OntologyValue


class RelatedResource:
    """
    The DTO class parses one "12_RelatedIdentifier" element object from a DataHub general instance.
    """

    def __init__(self, identifier: str, identifier_type: OntologyValue, relation_type: OntologyValue):
        self.identifier: str = identifier
        self.identifier_type: OntologyValue = identifier_type
        self.relation_type: OntologyValue = relation_type

    @classmethod
    def create_from_dict(cls, element: dict):
        identifier = element["relatedResourceIdentifier"]["@value"]
        identifier_type = OntologyValue.create_from_dict(element["relatedResourceIdentifierType"])
        relation_type = OntologyValue.create_from_dict(element["relationType"])

        return cls(identifier, identifier_type, relation_type)
