#!/usr/bin/python3
"""Defines function that converts csv to json"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Function writes data to data.json
    Args:
        csv_filename: csv file to convert
        data.json: json file to write to
    """


    data_list = []
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

    except FileNotFoundError:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4)
    except Exception:
        return False
    return True
