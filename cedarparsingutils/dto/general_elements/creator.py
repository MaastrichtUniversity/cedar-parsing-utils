from cedarparsingutils.dto.ontology_value import OntologyValue
from cedarparsingutils.dto.person import Person


class Creator(Person):
    """
    "2_Creator": {
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
    },
    """

    @classmethod
    def create_from_element(cls, element: dict):
        identifier: str = element["creatorIdentifier"]["@value"]
        identifier_scheme: OntologyValue = OntologyValue.create_from_element(element["creatorIdentifierScheme"])
        identifier_scheme_iri: OntologyValue = OntologyValue.create_from_element(element["creatorIdentifierSchemeIRI"])
        given_name: str = element["creatorGivenName"]["@value"]
        family_name: str = element["creatorFamilyName"]["@value"]
        full_name: str = element["creatorFullName"]["@value"]
        affiliation: OntologyValue = OntologyValue.create_from_element(element["creatorAffiliation"])

        return cls(
            identifier, identifier_scheme, identifier_scheme_iri, given_name, family_name, full_name, affiliation
        )
