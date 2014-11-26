"""
Utilities used in the resources
"""


def standardize_json(json):
    for key, value in json.iteritems():
        json[key] = str(value)
    return json