import json
import os
from pathlib import Path
from ._constants import RULE_CONFIG_FILE, RULE_GROUPS_CONFIG_FILE, COLLECTION_CONFIG_FILE

def _get_rule_config(rule_name):
    rule_config = None
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + RULE_CONFIG_FILE

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if rule_name in configs:
                rule_config = configs[rule_name]
    return rule_config

def _get_rule_list(framework, type):
    rules_list = []
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + RULE_GROUPS_CONFIG_FILE
    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            if framework in configs:
                if type in configs[framework]:
                    rules_list = configs[framework][type]
    return rules_list

def _get_config_for_group(rules):
    rules_config = []
    config_file_path = str(Path(__file__).parent.absolute()) + "/" + RULE_CONFIG_FILE

    if os.path.exists(config_file_path):
        with open(config_file_path) as json_data:
            configs = json.load(json_data)
            for rule_name in rules:
                if rule_name in configs:
                    rules_config.append(configs[rule_name])
    return rules_config

