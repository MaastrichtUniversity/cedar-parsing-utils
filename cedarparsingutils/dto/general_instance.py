from cedarparsingutils.dto.general_elements.date import Date
from cedarparsingutils.dto.general_elements.description import Description
from cedarparsingutils.dto.general_elements.identifier import Identifier
from cedarparsingutils.dto.general_elements.publisher import Publisher
from cedarparsingutils.dto.general_elements.related_resources import RelatedResources
from cedarparsingutils.dto.general_elements.resource_type import ResourceType
from cedarparsingutils.dto.general_elements.subjects import Subjects
from cedarparsingutils.dto.general_elements.title import Title


class GeneralInstance:
    """ """

    def __init__(
        self,
        identifier: Identifier,
        publisher: Publisher,
        date: Date,
        creator,
        contacts,
        contributors,
        title: Title,
        description: Description,
        subjects: Subjects,
        resource_type: ResourceType,
        related_resources: RelatedResources,
    ):
        self.identifier: Identifier = identifier
        self.publisher: Publisher = publisher
        self.date: Date = date
        self.creator = creator
        self.contacts = contacts
        self.contributors = contributors
        self.title: Title = title
        self.description: Description = description
        self.subjects: Subjects = subjects
        self.resource_type: ResourceType = resource_type
        self.related_resources: RelatedResources = related_resources

    @classmethod
    def create_from_dict(cls, metadata):
        identifier = Identifier.create_from_element(metadata["1_Identifier"])
        publisher = Publisher.create_from_element(metadata["4_Publisher"])
        date = Date.create_from_element(metadata["8_Date"])
        creator = metadata["2_Creator"]
        contacts = metadata["7_ContactPerson"]
        contributors = metadata["7_Contributor"]
        title = Title.create_from_element(metadata["3_Title"])
        description = Description.create_from_element(metadata["17_Description"])
        subjects = Subjects.create_from_element(metadata["6_Subject"])
        resource_type = ResourceType.create_from_element(metadata["10_ResourceType"])
        related_resources = RelatedResources.create_from_element(metadata["12_RelatedIdentifier"])

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
