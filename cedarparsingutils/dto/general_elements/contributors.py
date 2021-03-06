import json

from cedarparsingutils.dto.general_elements.contributor import Contributor


class Contributors:
    """
    The DTO class parses a "7_Contributor" element array from a DataHub general instance.
    """

    def __init__(self, contributors: list[Contributor]):
        self.contributors: list[Contributor] = contributors

    @classmethod
    def create_from_dict(cls, element: dict):
        output: list[Contributor] = []
        for item in element:
            contributor = Contributor.create_from_dict(item)
            output.append(contributor)

        return cls(output)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Contributors.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    [
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
            "@context": {
                "contributorIdentifierScheme": "https://schema.metadatacenter.org/properties/264bff35-9c7e-4a84-a722-712217dfa232",
                "contributorAffiliation": "https://schema.metadatacenter.org/properties/73214405-3002-4fde-8f6c-b012faf907ec",
                "contributorFullName": "https://schema.metadatacenter.org/properties/272d6c5e-467c-4c01-a513-23b8df92585d",
                "contributorIdentifier": "https://schema.metadatacenter.org/properties/4636604a-6a42-4257-8a34-b8c68627cf32",
                "contributorFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                "contributorType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb",
                "contributorGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                "contributorEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4"
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
            "@id": "https://repo.metadatacenter.org/template-elements/1d979a88-1028-421d-a124-11b5011f278a"
        }
    ]
    """
