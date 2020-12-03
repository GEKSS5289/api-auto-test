import json


def json_to_rep(rep,data):
    return json.loads(rep.text)[data]