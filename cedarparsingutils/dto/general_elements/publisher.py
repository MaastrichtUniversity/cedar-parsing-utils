class Publisher:
    """
    "4_Publisher": {
        "Publisher": {
            "@value": "DataHub"
        },
        "@context": {
            "Publisher": "https://schema.metadatacenter.org/properties/2c80f739-e2c4-425e-9bf0-fa20fffe29ba"
        }
    },
    """

    def __init__(self, publisher: str):
        self.publisher: str = publisher

    @classmethod
    def create_from_element(cls, element):
        publisher = element["Publisher"]["@value"]

        return cls(publisher)
