import json


class Description:
    """
    The DTO class parses a "17_Description" element object from a DataHub general instance.
    """

    def __init__(self, description: str, type: str):
        self.description: str = description
        self.type: str = type

    @classmethod
    def create_from_dict(cls, element: dict):
        description = element["Description"]["@value"]
        type = element["descriptionType"]["@value"]

        return cls(description, type)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Description.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "descriptionType": {
            "@value": "Abstract"
        },
        "@id": "https://repo.metadatacenter.org/template-elements/1595a50e-f0c0-47c6-804e-fff5ac7a7531",
        "Description": {
            "@value": "Test, test, test - mock mock"
        },
        "@context": {
            "descriptionType": "http://purl.org/spar/datacite/hasDescriptionType",
            "Description": "http://purl.org/dc/terms/description"
        }
    }
    """
