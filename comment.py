import os
import json


def read_all_record() -> dict:
    all_config = dict()
    if not os.path.exists('static'):
        os.mkdir("static")
    if not os.path.exists('static/config.json'):
        return dict()
    with open("static/config.json", 'r') as fp:
        json_str = fp.read()
        if json_str:
            all_config = json.loads(json_str)
        return all_config


def write_all_record(record: dict) -> bool:
    if not os.path.exists('static'):os.mkdir("static")
    try:
        with open("static/config.json", 'w') as fp:
            fp.write(json.dumps(record, ensure_ascii=False))
            return True
    except IOError:
        return False
