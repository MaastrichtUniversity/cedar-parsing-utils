from cedarparsingutils.dto.ontology_value import OntologyValue


class Contact:
    """
    "7_ContactPerson": [
        {
            "contactFullName": {
                "@value": "Jonathan M\u00e9lius"
            },
            "contactAffiliation": {},
            "contactNameIdentifier": {
                "@value": "foobar"
            },
            "contactEmail": {
                "@value": "jonathan.melius@maastrichtuniversity.nl"
            },
            "contactNameIdentifierScheme": {},
            "contactFamilyName": {
                "@value": "M\u00e9lius"
            },
            "contactGivenName": {
                "@value": "Jonathan"
            },
            "contactType": {
                "rdfs:label": "contact person",
                "@id": "http://purl.org/zonmw/generic/10089"
            },
            "@context": {
                "contactNameIdentifier": "https://schema.metadatacenter.org/properties/953598f5-f9f7-4276-899f-09851b9501d1",
                "contactNameIdentifierScheme": "https://schema.metadatacenter.org/properties/d680d7f5-ac6d-4fac-a245-37ca8e41a2f9",
                "contactGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                "contactFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                "contactFullName": "https://schema.metadatacenter.org/properties/9cc96e17-345e-43c1-955d-9777ef8136aa",
                "contactEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4",
                "contactAffiliation": "https://schema.metadatacenter.org/properties/488e6114-b24f-4bf6-83b0-45a33abdabf6",
                "contactType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/a5b4ede8-f284-4991-b2c0-2273b925b2ca"
        }
    ]
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
    def create_from_element(cls, element: dict):
        identifier: str = element["contactNameIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_element(element["contactNameIdentifierScheme"])
        given_name: str = element["contactGivenName"]["@value"]
        family_name: str = element["contactFamilyName"]["@value"]
        full_name: str = element["contactFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_element(element["contactAffiliation"])
        email: str = element["contactEmail"]["@value"]
        type: OntologyValue = OntologyValue.create_from_element(element["contactType"])

        return cls(identifier, identifier_scheme, given_name, family_name, full_name, affiliation, email, type)
