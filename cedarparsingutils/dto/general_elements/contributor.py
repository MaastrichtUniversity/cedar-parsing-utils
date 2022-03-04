from cedarparsingutils.dto.ontology_value import OntologyValue


class Contributor:
    """
    "7_Contributor": [
        {
            "contributorIdentifierScheme": {
                "rdfs:label": "ORCiD",
                "@id": "https://orcid.org/"
            },
            "contributorAffiliation": {},
            "contributorFullName": {
                "@value": "Pascal Suppers"
            },
            "contributorIdentifier": {
                "@value": null
            },
            "contributorFamilyName": {
                "@value": "Suppers"
            },
            "contributorType": {
                "rdfs:label": "project manager",
                "@id": "http://purl.org/zonmw/generic/10082"
            },
            "contributorGivenName": {
                "@value": "Pascal"
            },
            "contributorEmail": {
                "@value": "p.suppers@maastrichtuniversity.nl"
            },
            "@context": {
                "contributorIdentifier": "https://schema.metadatacenter.org/properties/4636604a-6a42-4257-8a34-b8c68627cf32",
                "contributorIdentifierScheme": "https://schema.metadatacenter.org/properties/264bff35-9c7e-4a84-a722-712217dfa232",
                "contributorGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                "contributorFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                "contributorFullName": "https://schema.metadatacenter.org/properties/272d6c5e-467c-4c01-a513-23b8df92585d",
                "contributorAffiliation": "https://schema.metadatacenter.org/properties/73214405-3002-4fde-8f6c-b012faf907ec",
                "contributorEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4",
                "contributorType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb",
            }
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
        identifier: str = element["contributorIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_element(element["contributorIdentifierScheme"])
        given_name: str = element["contributorGivenName"]["@value"]
        family_name: str = element["contributorFamilyName"]["@value"]
        full_name: str = element["contributorFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_element(element["contributorAffiliation"])
        email: str = element["contributorEmail"]["@value"]
        type: OntologyValue = OntologyValue.create_from_element(element["contributorType"])

        return cls(identifier, identifier_scheme, given_name, family_name, full_name, affiliation, email, type)
