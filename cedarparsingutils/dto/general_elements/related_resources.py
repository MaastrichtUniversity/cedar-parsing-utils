from cedarparsingutils.dto.general_elements.related_resource import RelatedResource


class RelatedResources:
    """
    "12_RelatedIdentifier": [
        {
            "relationType": {},
            "relatedResourceIdentifierType": {},
            "@id": "https://repo.metadatacenter.org/template-elements/c13bdf4e-46a5-4364-925a-c33d33c13256",
            "relatedResourceIdentifier": {
                "@value": null
            },
            "@context": {
                "relationType": "http://rs.tdwg.org/dwc/terms/relationshipOfResource",
                "relatedResourceIdentifierType": "http://schema.org/propertyID",
                "relatedResourceIdentifier": "http://purl.org/dc/terms/identifier"
            }
        }
    ],
    """

    def __init__(self, related_resources: list[RelatedResource]):
        self.related_resources: list[RelatedResource] = related_resources

    @classmethod
    def create_from_element(cls, element: dict):
        output: list[RelatedResource] = []
        for item in element:
            resource = RelatedResource.create_from_element(item)
            output.append(resource)

        return cls(output)
