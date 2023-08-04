import json


_INDENT = 4


def formating(diffs):
    return json.dumps(diffs, _INDENT)
