from abc import abstractmethod
import json

from cedarparsingutils.utils import CedarSchemaName


class SchemaParser:
    """This class contains the logic to open, load and parse a CEDAR schema json file."""
    @staticmethod
    def open_and_load(schema_content: str) -> dict:
        """
        Open the string variable provided by the user and parse the JSON out of it.

        Parameters
        ----------
        schema_content: str
            The content of the schema as a string

        Returns
        -------
        schema: dict
            The parsed JSON
        """
        schema = json.loads(schema_content)
        return schema

    def parse_root_node(self, schema: dict) -> None:
        """
        Loop over the nodes at the root level and call parse_child_node() for each of them.

        Parameters
        ----------
        schema: dict
            The json schema as a variable
        """
        nodes = schema["_ui"]["order"]
        for node_id in nodes:
            node = schema["properties"][node_id]
            self.parse_child_node(node, node_id, "root")

    def parse_child_node(self, node, node_id, parent=None) -> CedarSchemaName:
        """
        Parse the input node and then return its field type annotation (=CedarSchemaName).
        While parsing, this method:
         * does recursive call if the node contains children
         * calls the corresponding abstract parsing method

        The abstract parsing methods must be overwritten by the inheriting class of SchemaParser:
         * parse_single_object_field
         * parse_nested_object_field
         * parse_single_array_field
         * parse_nested_array_field

        Parameters
        ----------
        node: dict
            The input node to parse
        node_id: str
            The node ID
        parent: str
            The parent's id of the current node

        Returns
        -------
        CedarSchemaName
            The cedar field type annotation, e.g "textfield", "checkbox", "temporal"
        """
        schema_name = None
        if node["type"] == "object" and "inputType" in node["_ui"]:
            schema_name = self.parse_single_object_field(node, node_id, parent)
        elif node["type"] == "object" and "order" in node["_ui"]:
            self.parse_nested_object_field(node, node_id, parent)
        elif node["type"] == "array" and "inputType" in node["items"]["_ui"]:
            schema_name = self.parse_single_array_field(node, node_id, parent)
        elif node["type"] == "array" and "order" in node["items"]["_ui"]:
            self.parse_nested_array_field(node, node_id, parent)

        return schema_name

    def parse_schema_name(self, node_schema_name: str, node_id: str) -> CedarSchemaName:
        """
        Parses a string schema name into a CedarSchemaName enum.
        If the schema name is not supported, this method calls parse_unknown_schema_name().

        Parameters
        ----------
        node_schema_name: str
            The schema name in a string variant
        node_id: str
            The id of the node

        Returns
        -------
        The schema name as CedarSchemaName
        """
        schema_name = None

        if node_schema_name == "textfield":
            schema_name = CedarSchemaName.TEXTFIELD
        elif node_schema_name == "temporal":
            schema_name = CedarSchemaName.TEMPORAL
        elif node_schema_name == "email":
            schema_name = CedarSchemaName.EMAIL
        elif node_schema_name == "numeric":
            schema_name = CedarSchemaName.NUMERIC
        elif node_schema_name == "link":
            schema_name = CedarSchemaName.LINK
        elif node_schema_name == "textarea":
            schema_name = CedarSchemaName.TEXTAREA
        elif node_schema_name == "radio":
            schema_name = CedarSchemaName.RADIO
        elif node_schema_name == "checkbox":
            schema_name = CedarSchemaName.CHECKBOX
        elif node_schema_name == "page-break":
            schema_name = CedarSchemaName.PAGE_BREAK
        elif node_schema_name == "section-break":
            schema_name = CedarSchemaName.SECTION_BREAK
        else:
            self.parse_unknown_schema_name(node_schema_name, node_id)
        return schema_name

    @abstractmethod
    def parse_unknown_schema_name(self, node_schema_name=None, node_id=None):
        """
        This method is meant to be overwritten to put the logic for unsupported schema name.

        Parameters
        ----------
        node_schema_name: str
            The schema name in a string variant
        node_id: str
            The id of the node
        """

    def parse_single_object_field(self, node, node_id=None, parent=None):
        """
        This method returns its cedar field type annotation.

        Parameters
        ----------
        node: dict
            The input node to parse
        node_id: str
            The node ID
        parent: str
            The parent's id of the current node

        Returns
        -------
        CedarSchemaName
            The cedar field type annotation, e.g "textfield", "checkbox", "temporal"
        """
        return self.parse_schema_name(node["_ui"]["inputType"], node_id)

    @abstractmethod
    def parse_nested_object_field(self, node, node_id=None, parent=None):
        """
        This method is meant to be overwritten and put the logic about how to parse nested object field.
        E.g:
        Creator{
            CreatorName: {}
            CreatorAffiliation: {}
        }

        Parameters
        ----------
        node: dict
            The input node to parse
        node_id: str
            The node ID
        parent: str
            The parent's id of the current node

        Returns
        -------
        CedarSchemaName
            The cedar field type annotation, e.g "textfield", "checkbox", "temporal"
        """

    def parse_single_array_field(self, node, node_id=None, parent=None):
        """
        This method returns its cedar field type annotation.

        Parameters
        ----------
        node: dict
            The input node to parse
        node_id: str
            The node ID
        parent: str
            The parent's id of the current node

        Returns
        -------
        CedarSchemaName
            The cedar field type annotation, e.g "textfield", "checkbox", "temporal"
        """

        return self.parse_schema_name(node["items"]["_ui"]["inputType"], node_id)

    @abstractmethod
    def parse_nested_array_field(self, node, node_id=None, parent=None):
        """
        This method is meant to be overwritten and put the logic about how to parse nested array field.
        E.g:
        Creator[
            {
                CreatorName: {}
                CreatorAffiliation: {}
            },
            {
                CreatorName: {}
                CreatorAffiliation: {}
            },
        ]

        Parameters
        ----------
        node: dict
            The input node to parse
        node_id: str
            The node ID
        parent: str
            The parent's id of the current node

        Returns
        -------
        CedarSchemaName
            The cedar field type annotation, e.g "textfield", "checkbox", "temporal"
        """
