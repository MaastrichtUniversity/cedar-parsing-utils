import json


class Title:
    """
    The DTO class parses a "3_Title" element object from a DataHub general instance.
    """

    def __init__(self, title: str):
        self.title: str = title

    @classmethod
    def create_from_dict(cls, element: dict):
        title = element["title"]["@value"]

        return cls(title)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Title.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "@context": {
            "title": "https://schema.metadatacenter.org/properties/4ffd7c46-1df8-4885-ade4-50d542d5b81e"
        },
        "title": {
            "@value": "Mock title - Test"
        }
    }
    """
