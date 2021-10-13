import yaml

def load_yaml(yaml_file):
    with open(yaml_file, 'r') as stream:
        config = yaml.safe_load(stream)
    return config
