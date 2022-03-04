class Title:
    """
    "3_Title": {
        "@context": {
            "title": "https://schema.metadatacenter.org/properties/4ffd7c46-1df8-4885-ade4-50d542d5b81e"
        },
        "title": {
            "@value": "Customizable metadata QA"
        }
    },
    """

    def __init__(self, title: str):
        self.title: str = title

    @classmethod
    def create_from_element(cls, element: dict):
        title = element["title"]["@value"]

        return cls(title)
