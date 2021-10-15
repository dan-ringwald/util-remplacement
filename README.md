# util-remplacement
replace patterns in text based on modular configuration files

## Actions

### Build a replacement map

1. Create a ReplacementMap object (Optionally with an initial YAML file). `mapper = ReplacementMap(some_replacements.yaml)`
2. Append rules to the replacement map. Rules' order is preserved inside files and between files. `mapper = ReplacementMap.add_yaml_file(other_replacements.yaml)`

### Apply a replacement map

Applies replacement map on a text: `mapper.process_text('some text to be processed')`

### Test the package

`python -m unittest tests/test_replacement_map.py`
