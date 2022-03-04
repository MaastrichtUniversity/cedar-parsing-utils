from cedarparsingutils.dto.ontology_value import OntologyValue


class Date:
    """
    "8_Date": {
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

    def __init__(self, date: str, type: OntologyValue):
        self.date: str = date
        self.type: OntologyValue = type

    @classmethod
    def create_from_element(cls, element: dict):
        date = element["datasetDate"]["@value"]
        type = OntologyValue.create_from_element(element["datasetDateType"])

        return cls(date, type)
