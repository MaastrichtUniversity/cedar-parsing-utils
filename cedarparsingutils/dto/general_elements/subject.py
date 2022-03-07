from cedarparsingutils.dto.ontology_value import OntologyValue


class Subject:
    """
    The DTO class parses one "6_Subject" element object from a DataHub general instance.
    """

    def __init__(self, keyword: str, scheme_iri: str, value_uri: OntologyValue):
        self.keyword: str = keyword
        self.scheme_iri: str = scheme_iri
        self.value_uri: OntologyValue = value_uri

    @classmethod
    def create_from_dict(cls, element: dict):
        keyword = element["Subject"]["@value"]
        scheme_iri = element["subjectSchemeIRI"]["@value"]
        value_uri = OntologyValue.create_from_dict(element["valueURI"])

        return cls(keyword, scheme_iri, value_uri)
