from collections import defaultdict
import inspect

def groups_all_configs(test_config):
    grouped_configs = defaultdict(list)

    # Get all class attributes
    for name, value in inspect.getmembers(test_config):
        # Ensure it's a dictionary and has 'group_id'
        if isinstance(value, dict) and 'group_id' in value:
            grouped_configs[value['group_id']].append(value)

    # Convert to list of lists
    return list(grouped_configs.values())
