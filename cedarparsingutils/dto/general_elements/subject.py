from cedarparsingutils.dto.ontology_value import OntologyValue


class Subject:
    """
     {
        "@context": {
            "subjectSchemeIRI": "http://vocab.fairdatacollective.org/gdmt/hasSubjectSchemeIRI",
            "valueURI": "https://schema.metadatacenter.org/properties/af9c45ec-d971-4056-a6c2-5ce930b9b181",
            "Subject": "https://schema.metadatacenter.org/properties/71f1a80c-d59e-4d92-a084-4f22f219cb6e"
        },
        "subjectSchemeIRI": {
            "@value": "http://purl.obolibrary.org/obo"
        },
        "valueURI": {
            "rdfs:label": "Schizosaccharomyces japonicus",
            "@id": "http://purl.obolibrary.org/obo/NCBITaxon_4897"
        },
        "Subject": {
            "@value": "Schizosaccharomyces japonicus"
        }
    }
    """

    def __init__(self, keyword: str, scheme_iri: str, value_uri: OntologyValue):
        self.keyword: str = keyword
        self.scheme_iri: str = scheme_iri
        self.value_uri: OntologyValue = value_uri

    @classmethod
    def create_from_element(cls, element: dict):
        keyword = element["Subject"]["@value"]
        scheme_iri = element["subjectSchemeIRI"]["@value"]
        value_uri = OntologyValue.create_from_element(element["valueURI"])

        return cls(keyword, scheme_iri, value_uri)
