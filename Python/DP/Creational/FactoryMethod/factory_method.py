import json
from xml.etree import ElementTree as ET

from faker import Faker

OutputType = int
OUTPUT_TYPE_JSON: OutputType = 1
OUTPUT_TYPE_XML: OutputType = 2


def get_samples():
    n = 5
    data = [{}] * n
    faker = Faker()
    for i in range(n):
        data[i] = {
            'name': faker.name(),
            'address': faker.address(),
        }

    return data


class JSONOutput:
    def to_file(self, data, filename):
        f = open(filename, 'w+')
        json.dump(data, f, indent=2)
        f.close()


class XMLOutput:
    def to_file(self, data, filename):
        root = ET.Element('consumers')
        for item in data:
            ET.SubElement(root, 'person', item)
        tree = ET.ElementTree(root)

        with open(filename, 'wb+') as f:
            tree.write(f)


def create_output(tpy: OutputType):
    if tpy == OUTPUT_TYPE_JSON:
        return JSONOutput()
    if tpy == OUTPUT_TYPE_XML:
        return XMLOutput()
    raise TypeError('output type not allowed')


if __name__ == '__main__':
    samples = get_samples()
    json_output = create_output(OUTPUT_TYPE_JSON)
    json_output.to_file(samples, 'samples.json')

    xml_output = create_output(OUTPUT_TYPE_XML)
    xml_output.to_file(samples, 'samples.xml')
