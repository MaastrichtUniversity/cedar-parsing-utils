from cedarparsingutils.dto.ontology_value import OntologyValue


class Contact:
    """
    The DTO class parses one "7_ContactPerson" element object from a DataHub general instance.
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
        identifier: str = element["contactNameIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_dict(element["contactNameIdentifierScheme"])
        given_name: str = element["contactGivenName"]["@value"]
        family_name: str = element["contactFamilyName"]["@value"]
        full_name: str = element["contactFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_dict(element["contactAffiliation"])
        email: str = element["contactEmail"]["@value"]
        type: OntologyValue = OntologyValue.create_from_dict(element["contactType"])

        return cls(identifier, identifier_scheme, given_name, family_name, full_name, affiliation, email, type)
