import json


class Publisher:
    """
    The DTO class parses a "4_Publisher" element object from a DataHub general instance.
    """

    def __init__(self, publisher: str):
        self.publisher: str = publisher

    @classmethod
    def create_from_dict(cls, element: dict):
        publisher = element["Publisher"]["@value"]

        return cls(publisher)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Publisher.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "Publisher": {
            "@value": "DataHub"
        },
        "@context": {
            "Publisher": "https://schema.metadatacenter.org/properties/2c80f739-e2c4-425e-9bf0-fa20fffe29ba"
        }
    }
    """
