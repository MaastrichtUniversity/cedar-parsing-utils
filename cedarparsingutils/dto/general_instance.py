import json

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


class GeneralInstance:
    """The DTO class of a DataHub general instance"""

    def __init__(
        self,
        identifier: Identifier,
        publisher: Publisher,
        date: Date,
        creator: Creator,
        contacts: Contacts,
        contributors: Contributors,
        title: Title,
        description: Description,
        subjects: Subjects,
        resource_type: ResourceType,
        related_resources: RelatedResources,
    ):
        self.identifier: Identifier = identifier
        self.publisher: Publisher = publisher
        self.date: Date = date
        self.creator: Creator = creator
        self.contacts: Contacts = contacts
        self.contributors: Contributors = contributors
        self.title: Title = title
        self.description: Description = description
        self.subjects: Subjects = subjects
        self.resource_type: ResourceType = resource_type
        self.related_resources: RelatedResources = related_resources

    @classmethod
    def create_from_dict(cls, metadata):
        identifier = Identifier.create_from_dict(metadata["1_Identifier"])
        publisher = Publisher.create_from_dict(metadata["4_Publisher"])
        date = Date.create_from_dict(metadata["8_Date"])
        creator = Creator.create_from_dict(metadata["2_Creator"])
        contacts = Contacts.create_from_dict(metadata["7_ContactPerson"])
        contributors = Contributors.create_from_dict(metadata["7_Contributor"])
        title = Title.create_from_dict(metadata["3_Title"])
        description = Description.create_from_dict(metadata["17_Description"])
        subjects = Subjects.create_from_dict(metadata["6_Subject"])
        resource_type = ResourceType.create_from_dict(metadata["10_ResourceType"])
        related_resources = RelatedResources.create_from_dict(metadata["12_RelatedIdentifier"])

        return cls(
            identifier,
            publisher,
            date,
            creator,
            contacts,
            contributors,
            title,
            description,
            subjects,
            resource_type,
            related_resources,
        )

    @classmethod
    def create_from_mock_result(cls, mock_json=None):
        if mock_json is None:
            mock_json = cls.MOCK_JSON
        return GeneralInstance.create_from_dict(json.loads(mock_json))

    MOCK_JSON = """
    {
        "7_Contributor": [
            {
                "contributorIdentifierScheme": {
                    "rdfs:label": "ORCiD",
                    "@id": "https://orcid.org/"
                },
                "contributorAffiliation": {},
                "contributorFullName": {
                    "@value": "Pascal Suppers"
                },
                "contributorIdentifier": {
                    "@value": null
                },
                "contributorFamilyName": {
                    "@value": "Suppers"
                },
                "@context": {
                    "contributorIdentifierScheme": "https://schema.metadatacenter.org/properties/264bff35-9c7e-4a84-a722-712217dfa232",
                    "contributorAffiliation": "https://schema.metadatacenter.org/properties/73214405-3002-4fde-8f6c-b012faf907ec",
                    "contributorFullName": "https://schema.metadatacenter.org/properties/272d6c5e-467c-4c01-a513-23b8df92585d",
                    "contributorIdentifier": "https://schema.metadatacenter.org/properties/4636604a-6a42-4257-8a34-b8c68627cf32",
                    "contributorFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                    "contributorType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb",
                    "contributorGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                    "contributorEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4"
                },
                "contributorType": {
                    "rdfs:label": "project manager",
                    "@id": "http://purl.org/zonmw/generic/10082"
                },
                "contributorGivenName": {
                    "@value": "Pascal"
                },
                "contributorEmail": {
                    "@value": "p.suppers@maastrichtuniversity.nl"
                },
                "@id": "https://repo.metadatacenter.org/template-elements/1d979a88-1028-421d-a124-11b5011f278a"
            },
            {
                "contributorIdentifierScheme": {
                    "rdfs:label": "ORCiD",
                    "@id": "https://orcid.org/"
                },
                "contributorAffiliation": {},
                "contributorFullName": {
                    "@value": "Olav Palmen"
                },
                "contributorIdentifier": {
                    "@value": null
                },
                "contributorFamilyName": {
                    "@value": "Palmen"
                },
                "@context": {
                    "contributorIdentifierScheme": "https://schema.metadatacenter.org/properties/264bff35-9c7e-4a84-a722-712217dfa232",
                    "contributorAffiliation": "https://schema.metadatacenter.org/properties/73214405-3002-4fde-8f6c-b012faf907ec",
                    "contributorFullName": "https://schema.metadatacenter.org/properties/272d6c5e-467c-4c01-a513-23b8df92585d",
                    "contributorIdentifier": "https://schema.metadatacenter.org/properties/4636604a-6a42-4257-8a34-b8c68627cf32",
                    "contributorFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                    "contributorType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb",
                    "contributorGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                    "contributorEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4"
                },
                "contributorType": {
                    "rdfs:label": "data manager",
                    "@id": "http://purl.org/zonmw/generic/10077"
                },
                "contributorGivenName": {
                    "@value": "Olav"
                },
                "contributorEmail": {
                    "@value": "o.palmen@maastrichtuniversity.nl"
                },
                "@id": "https://repo.metadatacenter.org/template-elements/1d979a88-1028-421d-a124-11b5011f278a"
            }
        ],
        "schema:isBasedOn": "https://hdl.handle.net/21.12109/P000000001C000000024schema.2",
        "2_Creator": {
            "creatorIdentifier": {
                "@value": "0000-0000-0000-0000"
            },
            "creatorIdentifierSchemeIRI": {
                "rdfs:label": "ORCiD",
                "@id": "https://orcid.org/"
            },
            "creatorGivenName": {
                "@value": "Jonathan"
            },
            "creatorAffiliation": {},
            "creatorIdentifierScheme": {
                "rdfs:label": "ORCiD",
                "@id": "https://orcid.org/"
            },
            "creatorFamilyName": {
                "@value": "M\u00e9lius"
            },
            "@context": {
                "creatorIdentifier": "https://schema.metadatacenter.org/properties/18e308f9-0286-4d53-9acf-45b64cf13409",
                "creatorIdentifierSchemeIRI": "https://schema.metadatacenter.org/properties/47dbf3ad-a626-47f9-814c-df36df9959bc",
                "creatorGivenName": "https://schema.metadatacenter.org/properties/70630a4c-d76f-46b2-902c-916203a981a1",
                "creatorAffiliation": "https://schema.metadatacenter.org/properties/11ea34dd-138e-4901-8565-c56e8cf980ca",
                "creatorIdentifierScheme": "https://schema.metadatacenter.org/properties/2a4230e0-9dc4-4477-bea8-a718e32106af",
                "creatorFamilyName": "https://schema.metadatacenter.org/properties/356309ef-b052-41ad-97b6-a30f76ba6df4",
                "creatorFullName": "https://schema.metadatacenter.org/properties/34cd0986-098c-4c76-830c-300966ad422a"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/d2e97c7c-90b7-44c4-8d4b-2c43d46c98a9",
            "creatorFullName": {
                "@value": "Jonathan M\u00e9lius"
            }
        },
        "schema:name": "DataHub General Schema",
        "10_ResourceType": {
            "@context": {
                "resourceTypeDetail": "https://schema.metadatacenter.org/properties/26faf602-2fd3-4e22-818b-32949c82b746",
                "resourceTypeGeneral": "https://schema.metadatacenter.org/properties/42039c05-9fe3-4e8a-b9f6-f97affc62d3c"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/34e8196b-c93f-4a04-a691-42d50da0aebf",
            "resourceTypeDetail": {
                "@value": "Collection"
            },
            "resourceTypeGeneral": {
                "rdfs:label": "Collection",
                "@id": "http://vocab.fairdatacollective.org/gdmt/Collection"
            }
        },
        "1_Identifier": {
            "datasetIdentifier": {
                "@value": "https://hdl.handle.net/21.12109/P000000001C000000024.2"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/1a0ab675-8fc9-40bf-a3eb-a6e39d626e5a",
            "datasetIdentifierType": {
                "rdfs:label": "Handle",
                "@id": "http://vocab.fairdatacollective.org/gdmt/Handle"
            },
            "@context": {
                "datasetIdentifier": "http://purl.org/dc/terms/identifier",
                "datasetIdentifierType": "http://purl.org/spar/datacite/usesIdentifierScheme"
            }
        },
        "12_RelatedIdentifier": [
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
            }
        ],
        "pav:lastUpdatedOn": "2022-03-04T10:03:06",
        "4_Publisher": {
            "Publisher": {
                "@value": "DataHub"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/331f86b7-17c5-4c1c-8be1-41d1c9e084a0",
            "@context": {
                "Publisher": "https://schema.metadatacenter.org/properties/2c80f739-e2c4-425e-9bf0-fa20fffe29ba"
            }
        },
        "3_Title": {
            "@context": {
                "title": "https://schema.metadatacenter.org/properties/4ffd7c46-1df8-4885-ade4-50d542d5b81e"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/83367232-64e2-4117-9797-98f0d2694698",
            "title": {
                "@value": "Customizable metadata QA"
            }
        },
        "7_ContactPerson": [
            {
                "contactFullName": {
                    "@value": "Jonathan M\u00e9lius"
                },
                "contactAffiliation": {},
                "contactNameIdentifier": {
                    "@value": "foobar"
                },
                "contactEmail": {
                    "@value": "jonathan.melius@maastrichtuniversity.nl"
                },
                "contactNameIdentifierScheme": {},
                "contactFamilyName": {
                    "@value": "M\u00e9lius"
                },
                "contactGivenName": {
                    "@value": "Jonathan"
                },
                "contactType": {
                    "rdfs:label": "contact person",
                    "@id": "http://purl.org/zonmw/generic/10089"
                },
                "@context": {
                    "contactFullName": "https://schema.metadatacenter.org/properties/9cc96e17-345e-43c1-955d-9777ef8136aa",
                    "contactAffiliation": "https://schema.metadatacenter.org/properties/488e6114-b24f-4bf6-83b0-45a33abdabf6",
                    "contactNameIdentifier": "https://schema.metadatacenter.org/properties/953598f5-f9f7-4276-899f-09851b9501d1",
                    "contactEmail": "https://schema.metadatacenter.org/properties/72eb0553-76b7-4ef2-898f-694aa015cdd4",
                    "contactNameIdentifierScheme": "https://schema.metadatacenter.org/properties/d680d7f5-ac6d-4fac-a245-37ca8e41a2f9",
                    "contactFamilyName": "https://schema.metadatacenter.org/properties/510d9317-3658-429b-b773-8f9c0d288668",
                    "contactGivenName": "https://schema.metadatacenter.org/properties/1b2e719d-c7cc-4db0-b6f8-22ccdf43a387",
                    "contactType": "https://schema.metadatacenter.org/properties/4d0bd488-6d4a-4388-bfa9-3cbb1d941afb"
                },
                "@id": "https://repo.metadatacenter.org/template-elements/a5b4ede8-f284-4991-b2c0-2273b925b2ca"
            }
        ],
        "schema:description": "This is the basic DataHub General Schema",
        "17_Description": {
            "descriptionType": {
                "@value": "Abstract"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/1595a50e-f0c0-47c6-804e-fff5ac7a7531",
            "Description": {
                "@value": "Test, test, testEdit post ingest"
            },
            "@context": {
                "descriptionType": "http://purl.org/spar/datacite/hasDescriptionType",
                "Description": "http://purl.org/dc/terms/description"
            }
        },
        "pav:createdOn": "2022-03-03T15:29:04",
        "datasetPagebreak": {},
        "pav:createdBy": "https://mdr.datahubmaastricht.nl/user/jmelius",
        "oslc:modifiedBy": "https://mdr.datahubmaastricht.nl/user/jmelius",
        "@context": {
            "rdfs:label": {
                "@type": "xsd:string"
            },
            "1_Identifier": "https://schema.metadatacenter.org/properties/b260286d-3da0-4f53-a40d-eb769c24da8f",
            "oslc:modifiedBy": {
                "@type": "@id"
            },
            "pav:derivedFrom": {
                "@type": "@id"
            },
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "6_Subject": "https://schema.metadatacenter.org/properties/d8dc1860-b3a5-4547-ad22-0e003dc2e5fc",
            "7_Contributor": "https://schema.metadatacenter.org/properties/45bffde9-fe61-4479-a70d-953e3aa4a9c9",
            "2_Creator": "https://schema.metadatacenter.org/properties/6297f721-5a92-4014-9a7d-2eeb9afbe11b",
            "oslc": "http://open-services.net/ns/core#",
            "pav": "http://purl.org/pav/",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "4_Publisher": "https://schema.metadatacenter.org/properties/68a521c1-69af-49e5-95a0-9890642da26d",
            "pav:createdBy": {
                "@type": "@id"
            },
            "8_Date": "https://schema.metadatacenter.org/properties/29cd27ea-b7b6-47b7-a82d-ab48ae34396d",
            "schema:isBasedOn": {
                "@type": "@id"
            },
            "schema:name": {
                "@type": "xsd:string"
            },
            "3_Title": "http://purl.org/dc/terms/title",
            "7_ContactPerson": "https://schema.metadatacenter.org/properties/9ae72767-4449-4018-9cf0-6da73604d0cc",
            "schema:description": {
                "@type": "xsd:string"
            },
            "skos:notation": {
                "@type": "xsd:string"
            },
            "pav:createdOn": {
                "@type": "xsd:dateTime"
            },
            "12_RelatedIdentifier": "https://schema.metadatacenter.org/properties/65f55a39-f020-45d6-a071-c8388a12a25f",
            "17_Description": "https://schema.metadatacenter.org/properties/28d418d7-bfe7-44fb-968f-6e3ae9b68501",
            "10_ResourceType": "https://schema.metadatacenter.org/properties/8f154e9c-501a-4b80-b148-a74f250edc69",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "schema": "http://schema.org/",
            "pav:lastUpdatedOn": {
                "@type": "xsd:dateTime"
            }
        },
        "@id": "https://hdl.handle.net/21.12109/P000000001C000000024instance.2",
        "6_Subject": [
            {
                "@context": {
                    "subjectSchemeIRI": "http://vocab.fairdatacollective.org/gdmt/hasSubjectSchemeIRI",
                    "valueURI": "https://schema.metadatacenter.org/properties/af9c45ec-d971-4056-a6c2-5ce930b9b181",
                    "Subject": "https://schema.metadatacenter.org/properties/71f1a80c-d59e-4d92-a084-4f22f219cb6e"
                },
                "subjectSchemeIRI": {
                    "@value": "http://purl.obolibrary.org/obo"
                },
                "valueURI": {
                    "rdfs:label": "Schizosaccharomyces japonicus",
                    "@id": "http://purl.obolibrary.org/obo/NCBITaxon_4897"
                },
                "@id": "https://repo.metadatacenter.org/template-elements/fc4e957d-637c-4a00-b371-d9e981ce3af4",
                "Subject": {
                    "@value": "Schizosaccharomyces japonicus"
                }
            },
            {
                "@context": {
                    "subjectSchemeIRI": "http://vocab.fairdatacollective.org/gdmt/hasSubjectSchemeIRI",
                    "valueURI": "https://schema.metadatacenter.org/properties/af9c45ec-d971-4056-a6c2-5ce930b9b181",
                    "Subject": "https://schema.metadatacenter.org/properties/71f1a80c-d59e-4d92-a084-4f22f219cb6e"
                },
                "subjectSchemeIRI": {
                    "@value": null
                },
                "valueURI": {},
                "@id": "https://repo.metadatacenter.org/template-elements/fc4e957d-637c-4a00-b371-d9e981ce3af4",
                "Subject": {
                    "@value": "toto"
                }
            },
            {
                "@context": {
                    "subjectSchemeIRI": "http://vocab.fairdatacollective.org/gdmt/hasSubjectSchemeIRI",
                    "valueURI": "https://schema.metadatacenter.org/properties/af9c45ec-d971-4056-a6c2-5ce930b9b181",
                    "Subject": "https://schema.metadatacenter.org/properties/71f1a80c-d59e-4d92-a084-4f22f219cb6e"
                },
                "subjectSchemeIRI": {
                    "@value": "http://purl.obolibrary.org/obo"
                },
                "valueURI": {
                    "rdfs:label": "response to haloperidol",
                    "@id": "http://purl.obolibrary.org/obo/GO_1905119"
                },
                "@id": "https://repo.metadatacenter.org/template-elements/fc4e957d-637c-4a00-b371-d9e981ce3af4",
                "Subject": {
                    "@value": "response to haloperidol"
                }
            }
        ],
        "8_Date": {
            "@context": {
                "datasetDateType": "http://vocab.fairdatacollective.org/gdmt/hasDatasetDateType",
                "datasetDate": "http://vocab.fairdatacollective.org/gdmt/hasDatasetDate"
            },
            "datasetDateType": {
                "rdfs:label": "Submitted",
                "@id": "http://vocab.fairdatacollective.org/gdmt/Submitted"
            },
            "@id": "https://repo.metadatacenter.org/template-elements/1bf3e3d6-c05e-43c6-b39d-c60080365268",
            "datasetDate": {
                "@value": "2022-03-03",
                "@type": "xsd:date"
            }
        }
    }
    """
