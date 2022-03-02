# cedar-parsing-utils
This repository hosts all of the parsing utilities for CEDAR schemas

### Installing
Required Python 3.6+ to install with pip from the GitHub repository
```
# From the default branch
pip3 install git+https://github.com/MaastrichtUniversity/cedar-parsing-utils.git

# With ssh
pip3 install git+ssh://github.com/MaastrichtUniversity/cedar-parsing-utils.git

# Or dev-branch
pip install -e git+https://github.com/MaastrichtUniversity/cedar-parsing-utils.git@develop#egg=cedar-parsing-utils
```

### Uninstalling

```
pip3 uninstall cedar-parsing-utils
```

### How to use it

```
from cedarparsingutils.schema_parser import SchemaParser
from cedarparsingutils.utils import CedarSchemaName


class Validator(SchemaParser):
    # override the abstract method
    def parse_unknown_schema_name(self, node_schema_name=None, node_id=None):
        self.utils.log_message(Severities.ERROR, node_id, f"schema_name '{node_schema_name}' is not allowed for node")

    # override the abstract method
    def parse_child_node(self, node, node_id, parent=None) -> CedarSchemaName:
        self.cedar_validator.check_duplicate_node_id(node_id)

        schema_name = super().parse_child_node(node, node_id, parent)

        self.cedar_validator.handle_field_specific_validation(schema_name, node, node_id)
        return schema_name
```
