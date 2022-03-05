import yaml

"""
Interface to the yaml configuration files
* Reads and populates the respective variables from the config files.
"""

def get_api_info():
    with open("config.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            api_id = config['api_id']
            api_hash = config['api_hash']
            return api_id, api_hash
        except yaml.YAMLError as exc:
            print(exc)

