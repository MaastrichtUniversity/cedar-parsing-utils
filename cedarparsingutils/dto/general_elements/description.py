class Description:
    """
    "17_Description": {
        "descriptionType": {
            "@value": "Abstract"
        },
        "@id": "https://repo.metadatacenter.org/template-elements/1595a50e-f0c0-47c6-804e-fff5ac7a7531",
        "Description": {
            "@value": "Test, test, test\r\nEdit post ingest"
        },
        "@context": {
            "descriptionType": "http://purl.org/spar/datacite/hasDescriptionType",
            "Description": "http://purl.org/dc/terms/description"
        }
    },
    """

    def __init__(self, description: str, type: str):
        self.description: str = description
        self.type: str = type

    @classmethod
    def create_from_element(cls, element: dict):
        description = element["Description"]["@value"]
        type = element["descriptionType"]["@value"]

        return cls(description, type)
