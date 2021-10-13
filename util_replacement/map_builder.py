import re
import yaml

class ReplacementMap:
    """
    Read replacement rules in a yaml and compiles them.
    Can apply them to a text.
    """

    def __init__(self, yaml_file):
        with open(yaml_file, 'r') as stream:
            config = yaml.safe_load(stream)
        self.map = []
        self._add_replacement_rules(config)

    def _add_replacement_rules(self, replacement_dict):
        """
        Recursive private method walking through replacement config.
        Recursively append replacement rules to the replacement map
        """
        keys = replacement_dict.keys()
        if "from" in keys and "to" in keys:
            self.map.append((re.compile(replacement_dict['from']), replacement_dict['to']))
        else:
            for k in keys:
                self._add_replacement_rules(replacement_dict[k])

    def process_text(self, text, normalize_spaces=True):
        """
        Apply replacement map to a text.
        normalize_spaces param removes duplicated and trailing whitespaces.
        """
        for reg, repl in self.map:
            text = re.sub(reg, repl, text)
        if normalize_spaces:
            text = re.sub(' +', ' ', text).strip()
        return text
