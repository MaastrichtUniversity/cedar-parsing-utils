import json

from cedarparsingutils.dto.ontology_value import OntologyValue


class Creator:
    """
    The DTO class parses a "2_Creator" element object from a DataHub general instance.
    """

    def __init__(
        self,
        identifier: str,
        identifier_scheme: OntologyValue,
        identifier_scheme_iri: OntologyValue,
        given_name: str,
        family_name: str,
        full_name: str,
        affiliation: OntologyValue,
    ):
        self.identifier: str = identifier
        self.identifier_scheme: OntologyValue = identifier_scheme
        self.identifier_scheme_iri: OntologyValue = identifier_scheme_iri
        self.given_name: str = given_name
        self.family_name: str = family_name
        self.full_name: str = full_name
        self.affiliation: OntologyValue = affiliation

    @classmethod
    def create_from_dict(cls, element: dict):
        identifier: str = element["creatorIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_dict(element["creatorIdentifierScheme"])
        identifier_scheme_iri: OntologyValue = OntologyValue.create_from_dict(element["creatorIdentifierSchemeIRI"])
        given_name: str = element["creatorGivenName"]["@value"]
        family_name: str = element["creatorFamilyName"]["@value"]
        full_name: str = element["creatorFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_dict(element["creatorAffiliation"])

        return cls(
            identifier, identifier_scheme, identifier_scheme_iri, given_name, family_name, full_name, affiliation
        )

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Creator.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "creatorIdentifier": {
            "@value": "foobar"
        },
        "creatorIdentifierSchemeIRI": {
            "rdfs:label": "ORCiD",
            "@id": "https://orcid.org/"
        },
        "creatorGivenName": {
            "@value": "Jonathan"
        },
        "creatorAffiliation": {
            "rdfs:label": "Maastricht University",
            "@id": "http://purl.org/zonmw/generic/10045"
        },
        "creatorIdentifierScheme": {
            "rdfs:label": "ORCiD",
            "@id": "https://orcid.org/"
        },
        "creatorFamilyName": {
            "@value": "M\u00e9lius"
        },
        "creatorFullName": {
            "@value": "Jonathan M\u00e9lius"
        },
        "@context": {
            "creatorIdentifier": "https://schema.metadatacenter.org/properties/18e308f9-0286-4d53-9acf-45b64cf13409",
            "creatorIdentifierScheme": "https://schema.metadatacenter.org/properties/2a4230e0-9dc4-4477-bea8-a718e32106af",
            "creatorIdentifierSchemeIRI": "https://schema.metadatacenter.org/properties/47dbf3ad-a626-47f9-814c-df36df9959bc",
            "creatorGivenName": "https://schema.metadatacenter.org/properties/70630a4c-d76f-46b2-902c-916203a981a1",
            "creatorFamilyName": "https://schema.metadatacenter.org/properties/356309ef-b052-41ad-97b6-a30f76ba6df4",
            "creatorFullName": "https://schema.metadatacenter.org/properties/34cd0986-098c-4c76-830c-300966ad422a",
            "creatorAffiliation": "https://schema.metadatacenter.org/properties/11ea34dd-138e-4901-8565-c56e8cf980ca"
        }
    }
    """
