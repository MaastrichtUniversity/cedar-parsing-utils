from cedarparsingutils.dto.general_elements.subject import Subject


class Subjects:
    """
    "6_Subject": [
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
        }
    ]
    """

    def __init__(self, data_stewards: list[Subject]):
        self.subjects: list[Subject] = data_stewards

    @classmethod
    def create_from_element(cls, element: dict):
        output: list[Subject] = []
        for item in element:
            subject = Subject.create_from_element(item)
            output.append(subject)
        subjects = cls(output)
        return subjects
