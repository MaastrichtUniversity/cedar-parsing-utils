import json

from cedarparsingutils.dto.general_elements.subject import Subject


class Subjects:
    """
    The DTO class parses a "6_Subject" element array from a DataHub general instance.
    """

    def __init__(self, subjects: list[Subject]):
        self.subjects: list[Subject] = subjects

    @classmethod
    def create_from_dict(cls, element: dict):
        output: list[Subject] = []
        for item in element:
            subject = Subject.create_from_dict(item)
            output.append(subject)

        return cls(output)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Subjects.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    [
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
            "@id": "https://repo.metadatacenter.org/template-elements/fc4e957d-637c-4a00-b371-d9e981ce3af4",
            "Subject": {
                "@value": "Schizosaccharomyces japonicus"
            }
        },
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
                "rdfs:label": "Schizosaccharomyces pombe",
                "@id": "http://purl.obolibrary.org/obo/NCBITaxon_4896"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/fc4e957d-637c-4a00-b371-d9e981ce3af4",
            "Subject": {
                "@value": "Schizosaccharomyces pombe"
            }
        }
    ]
    """
