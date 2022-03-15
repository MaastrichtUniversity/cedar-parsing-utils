from cedarparsingutils.dto.ontology_value import OntologyValue


def test_ontology_value():
    result = OntologyValue.create_from_mock_result()
    assert result.uri == "http://vocab.fairdatacollective.org/gdmt/Submitted"
    assert result.label == "Submitted"
