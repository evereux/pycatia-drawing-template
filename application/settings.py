#! /usr/bin/python3.8

import json
from pathlib import Path


def read_json(f: Path):
    with open(f) as file:
        data = json.load(file)

    return data


json_settings = Path('settings.json')
json_data = read_json(json_settings)

border_offset = json_data['border_offset']
company_details = json_data['company_details']
parameters = json_data['parameters']
sheet_sizes = json_data['sheet_sizes']
sheet_names = json_data['sheet_names']
template_name = json_data['template_name']
logo = Path(json_data['logo'])
units = json_data['units']
tolerances = json_data['tolerances']