import csv
import json
import xml.etree.ElementTree as ET

def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def csv_to_xml(csv_file, xml_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        root = ET.Element("WeatherData")

        for row in reader:
            entry = ET.SubElement(root, "Record")
            for key, value in row.items():
                child = ET.SubElement(entry, key)
                child.text = value

        tree = ET.ElementTree(root)
        tree.write(xml_file, encoding='utf-8', xml_declaration=True)

csv_file = 'basel_weather.csv'
json_file = 'basel_weather.json'
xml_file = 'basel_weather.xml'

csv_to_json(csv_file, json_file)
csv_to_xml(csv_file, xml_file)