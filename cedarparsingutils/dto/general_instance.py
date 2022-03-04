from cedarparsingutils.dto.general_elements.date import Date
from cedarparsingutils.dto.general_elements.identifier import Identifier
from cedarparsingutils.dto.general_elements.publisher import Publisher


class GeneralInstance:
    """ """

    def __init__(
        self,
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
        related_resource,
    ):
        self.identifier = identifier
        self.publisher = publisher
        self.date = date
        self.creator = creator
        self.contacts = contacts
        self.contributors = contributors
        self.title = title
        self.description = description
        self.subjects = subjects
        self.resource_type = resource_type
        self.related_resource = related_resource

    @classmethod
    def create_from_dict(cls, metadata):
        identifier = Identifier.create_from_element(metadata["1_Identifier"])
        publisher = Publisher.create_from_element(metadata["4_Publisher"])
        date = Date.create_from_element(metadata["8_Date"])
        creator = metadata["2_Creator"]
        contacts = metadata["7_ContactPerson"]
        contributors = metadata["7_Contributor"]
        title = metadata["3_Title"]
        description = metadata["17_Description"]
        subjects = metadata["6_Subject"]
        resource_type = metadata["10_ResourceType"]
        related_resource = metadata["12_RelatedIdentifier"]

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
            related_resource,
        )
