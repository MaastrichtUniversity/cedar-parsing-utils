from cedarparsingutils.dto.ontology_value import OntologyValue


class Contributor:
    """
    The DTO class parses one "7_Contributor" element object from a DataHub general instance.
    """

    def __init__(
        self,
        identifier: str,
        identifier_scheme: OntologyValue,
        given_name: str,
        family_name: str,
        full_name: str,
        affiliation: OntologyValue,
        email: str,
        type: OntologyValue,
    ):
        self.identifier: str = identifier
        self.identifier_scheme: OntologyValue = identifier_scheme
        self.given_name: str = given_name
        self.family_name: str = family_name
        self.full_name: str = full_name
        self.affiliation: OntologyValue = affiliation
        self.email: str = email
        self.type: OntologyValue = type

    @classmethod
    def create_from_dict(cls, element: dict):
        identifier: str = element["contributorIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_dict(element["contributorIdentifierScheme"])
        given_name: str = element["contributorGivenName"]["@value"]
        family_name: str = element["contributorFamilyName"]["@value"]
        full_name: str = element["contributorFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_dict(element["contributorAffiliation"])
        email: str = element["contributorEmail"]["@value"]
        type: OntologyValue = OntologyValue.create_from_dict(element["contributorType"])

        return cls(identifier, identifier_scheme, given_name, family_name, full_name, affiliation, email, type)
