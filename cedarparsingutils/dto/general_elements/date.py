import json

from cedarparsingutils.dto.ontology_value import OntologyValue


class Date:
    """
    The DTO class parses a "8_Date" element object from a DataHub general instance.
    """

    def __init__(self, date: str, type: OntologyValue):
        self.date: str = date
        self.type: OntologyValue = type

    @classmethod
    def create_from_dict(cls, element: dict):
        date = element["datasetDate"]["@value"]
        type = OntologyValue.create_from_dict(element["datasetDateType"])

        return cls(date, type)

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return Date.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "@context": {
            "datasetDateType": "http://vocab.fairdatacollective.org/gdmt/hasDatasetDateType",
            "datasetDate": "http://vocab.fairdatacollective.org/gdmt/hasDatasetDate"
        },
        "datasetDateType": {
            "rdfs:label": "Submitted",
            "@id": "http://vocab.fairdatacollective.org/gdmt/Submitted"
        },
        "datasetDate": {
            "@value": "2022-03-03",
            "@type": "xsd:date"
        }
    }
    """
