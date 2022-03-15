import json

from cedarparsingutils.dto.general_elements.related_resource import RelatedResource


class RelatedResources:
    """
    The DTO class parses a "12_RelatedIdentifier" element array from a DataHub general instance.
    """

    def __init__(self, related_resources: list[RelatedResource]):
        self.related_resources: list[RelatedResource] = related_resources

    @classmethod
    def create_from_dict(cls, element: dict):
        output: list[RelatedResource] = []
        for item in element:
            resource = RelatedResource.create_from_dict(item)
            output.append(resource)

        return cls(output)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return RelatedResources.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    [
        {
            "relationType": {
                "rdfs:label": "Requires",
                "@id": "http://vocab.fairdatacollective.org/gdmt/Requires"
            },
            "relatedResourceIdentifierType": {
                "rdfs:label": "EISSN",
                "@id": "http://vocab.fairdatacollective.org/gdmt/EISSN"
            },
            "relatedResourceIdentifier": {
                "@value": "123456789"
            },
            "@context": {
                "relationType": "http://rs.tdwg.org/dwc/terms/relationshipOfResource",
                "relatedResourceIdentifierType": "http://schema.org/propertyID",
                "relatedResourceIdentifier": "http://purl.org/dc/terms/identifier"
            }
        },
        {
            "relationType": {
                "rdfs:label": "DocumentedBy",
                "@id": "http://vocab.fairdatacollective.org/gdmt/DocumentedBy"
            },
            "relatedResourceIdentifierType": {
                "rdfs:label": "DOI",
                "@id": "http://vocab.fairdatacollective.org/gdmt/DOI"
            },
            "relatedResourceIdentifier": {
                "@value": "https://doi.org/10.1016/j.cell.2022.01.026"
            },
            "@context": {
                "relationType": "http://rs.tdwg.org/dwc/terms/relationshipOfResource",
                "relatedResourceIdentifierType": "http://schema.org/propertyID",
                "relatedResourceIdentifier": "http://purl.org/dc/terms/identifier"
            }
        }
    ]
    """
