import json

import pytest

from cedarparsingutils.dto.general_elements.contacts import Contacts
from cedarparsingutils.dto.general_elements.contributors import Contributors
from cedarparsingutils.dto.general_elements.creator import Creator
from cedarparsingutils.dto.general_elements.date import Date
from cedarparsingutils.dto.general_elements.description import Description
from cedarparsingutils.dto.general_elements.identifier import Identifier
from cedarparsingutils.dto.general_elements.publisher import Publisher
from cedarparsingutils.dto.general_elements.related_resources import RelatedResources
from cedarparsingutils.dto.general_elements.resource_type import ResourceType
from cedarparsingutils.dto.general_elements.subjects import Subjects
from cedarparsingutils.dto.general_elements.title import Title
from cedarparsingutils.dto.general_instance import GeneralInstance


def test_instance():
    general_instance = GeneralInstance.create_from_mock_result()
    # "1_Identifier"
    assert general_instance.identifier.pid == "https://hdl.handle.net/21.12109/P000000001C000000024.2"
    assert general_instance.identifier.type.uri == "http://vocab.fairdatacollective.org/gdmt/Handle"

    # "4_Publisher"
    assert general_instance.publisher.publisher == "DataHub"

    # "8_Date"
    assert general_instance.date.date == "2022-03-03"
    assert general_instance.date.type.uri == "http://vocab.fairdatacollective.org/gdmt/Submitted"
    assert general_instance.date.type.label == "Submitted"

    # "2_Creator"
    assert general_instance.creator.identifier == "0000-0000-0000-0000"
    assert general_instance.creator.identifier_scheme_iri.uri == "https://orcid.org/"
    assert general_instance.creator.identifier_scheme.label == "ORCiD"
    assert general_instance.creator.given_name == "Jonathan"
    assert general_instance.creator.family_name == "M\u00e9lius"
    assert general_instance.creator.full_name == "Jonathan M\u00e9lius"
    assert general_instance.creator.affiliation.label == ""

    # "7_ContactPerson"
    assert general_instance.contacts.contacts[0].identifier == "foobar"
    assert general_instance.contacts.contacts[0].identifier_scheme.label == ""
    assert general_instance.contacts.contacts[0].given_name == "Jonathan"
    assert general_instance.contacts.contacts[0].family_name == "M\u00e9lius"
    assert general_instance.contacts.contacts[0].full_name == "Jonathan M\u00e9lius"
    assert general_instance.contacts.contacts[0].affiliation.label == ""
    assert general_instance.contacts.contacts[0].type.label == "contact person"
    assert general_instance.contacts.contacts[0].type.uri == "http://purl.org/zonmw/generic/10089"
    assert general_instance.contacts.contacts[0].email == "jonathan.melius@maastrichtuniversity.nl"

    # "7_Contributor"
    assert general_instance.contributors.contributors[1].identifier is None
    assert general_instance.contributors.contributors[1].identifier_scheme.label == "ORCiD"
    assert general_instance.contributors.contributors[1].given_name == "Olav"
    assert general_instance.contributors.contributors[1].family_name == "Palmen"
    assert general_instance.contributors.contributors[1].full_name == "Olav Palmen"
    assert general_instance.contributors.contributors[1].affiliation.label == ""
    assert general_instance.contributors.contributors[1].type.label == "data manager"
    assert general_instance.contributors.contributors[1].type.uri == "http://purl.org/zonmw/generic/10077"
    assert general_instance.contributors.contributors[1].email == "o.palmen@maastrichtuniversity.nl"

    # "3_Title"
    assert general_instance.title.title == "Customizable metadata QA"

    # "17_Description"
    assert general_instance.description.description == "Test, test, testEdit post ingest"
    assert general_instance.description.type == "Abstract"

    # "6_Subject"
    assert general_instance.subjects.subjects[0].keyword == "Schizosaccharomyces japonicus"
    assert general_instance.subjects.subjects[0].scheme_iri == "http://purl.obolibrary.org/obo"
    assert general_instance.subjects.subjects[0].value_uri.uri == "http://purl.obolibrary.org/obo/NCBITaxon_4897"

    # "10_ResourceType"
    assert general_instance.resource_type.type_detail == "Collection"
    assert general_instance.resource_type.type_general.uri == "http://vocab.fairdatacollective.org/gdmt/Collection"

    # "12_RelatedIdentifier"
    assert general_instance.related_resources.related_resources[0].identifier == "123456789"
    assert general_instance.related_resources.related_resources[0].identifier_type.label == "EISSN"
    assert (
        general_instance.related_resources.related_resources[0].relation_type.uri
        == "http://vocab.fairdatacollective.org/gdmt/Requires"
    )


def test_parse_minimal_instance_from_file():
    f = open("assets/minimal.json", "r")
    data = json.load(f)
    GeneralInstance.create_from_dict(data)


def test_parse_full_instance_from_file():
    f = open("assets/full.json", "r")
    data = json.load(f)
    GeneralInstance.create_from_dict(data)


def test_parse_wrong_instance_from_file():
    with pytest.raises(KeyError, match="creatorGivenName"):
        # Creator given name is missing
        f = open("assets/wrong.json", "r")
        data = json.load(f)
        GeneralInstance.create_from_dict(data)


def test_identifier():
    result = Identifier.create_from_mock_result()
    assert result.pid == "https://hdl.handle.net/21.12109/P000000001C000000024.2"
    assert result.type.label == "Handle"
    assert result.type.uri == "http://vocab.fairdatacollective.org/gdmt/Handle"


def test_publisher():
    result = Publisher.create_from_mock_result()
    assert result.publisher == "DataHub"


def test_date():
    result = Date.create_from_mock_result()
    assert result.date == "2022-03-03"
    assert result.type.label == "Submitted"
    assert result.type.uri == "http://vocab.fairdatacollective.org/gdmt/Submitted"


def test_creator():
    result = Creator.create_from_mock_result()
    assert result.identifier == "foobar"
    assert result.identifier_scheme_iri.uri == "https://orcid.org/"
    assert result.identifier_scheme.label == "ORCiD"
    assert result.given_name == "Jonathan"
    assert result.family_name == "M\u00e9lius"
    assert result.full_name == "Jonathan M\u00e9lius"
    assert result.affiliation.label == "Maastricht University"
    assert result.affiliation.uri == "http://purl.org/zonmw/generic/10045"


def test_contacts():
    result = Contacts.create_from_mock_result()
    assert result.contacts[0].identifier == "foobar"
    assert result.contacts[0].identifier_scheme.label == ""
    assert result.contacts[0].given_name == "Jonathan"
    assert result.contacts[0].family_name == "M\u00e9lius"
    assert result.contacts[0].full_name == "Jonathan M\u00e9lius"
    assert result.contacts[0].affiliation.label == ""
    assert result.contacts[0].type.label == "contact person"
    assert result.contacts[0].type.uri == "http://purl.org/zonmw/generic/10089"
    assert result.contacts[0].email == "jonathan.melius@maastrichtuniversity.nl"


def test_contributors():
    result = Contributors.create_from_mock_result()
    assert result.contributors[0].identifier is None
    assert result.contributors[0].identifier_scheme.label == "ORCiD"
    assert result.contributors[0].given_name == "Pascal"
    assert result.contributors[0].family_name == "Suppers"
    assert result.contributors[0].full_name == "Pascal Suppers"
    assert result.contributors[0].affiliation.label == ""
    assert result.contributors[0].type.label == "project manager"
    assert result.contributors[0].type.uri == "http://purl.org/zonmw/generic/10082"
    assert result.contributors[0].email == "p.suppers@maastrichtuniversity.nl"


def test_title():
    result = Title.create_from_mock_result()
    assert result.title == "Mock title - Test"


def test_description():
    result = Description.create_from_mock_result()
    assert result.description == "Test, test, test - mock mock"
    assert result.type == "Abstract"


def test_subjects():
    result = Subjects.create_from_mock_result()
    assert result.subjects[0].keyword == "Schizosaccharomyces japonicus"
    assert result.subjects[1].scheme_iri == "http://purl.obolibrary.org/obo"
    assert result.subjects[1].value_uri.uri == "http://purl.obolibrary.org/obo/NCBITaxon_4896"


def test_resource_type():
    result = ResourceType.create_from_mock_result()
    assert result.type_detail == "Collection - Mock"
    assert result.type_general.label == "Collection"
    assert result.type_general.uri == "http://vocab.fairdatacollective.org/gdmt/Collection"


def test_related_resources():
    result = RelatedResources.create_from_mock_result()
    assert result.related_resources[1].identifier == "https://doi.org/10.1016/j.cell.2022.01.026"
    assert result.related_resources[1].relation_type.label == "DocumentedBy"
    assert result.related_resources[1].relation_type.uri == "http://vocab.fairdatacollective.org/gdmt/DocumentedBy"
    assert result.related_resources[1].identifier_type.label == "DOI"
    assert result.related_resources[1].identifier_type.uri == "http://vocab.fairdatacollective.org/gdmt/DOI"
