from bs4 import BeautifulSoup
import json
import uuid

def html_to_json(html):
    soup = BeautifulSoup(html, 'lxml')
    return parse_element(soup)

def parse_element(element):
    json_dict = {}
    for child in element.find_all("p"):
        for x in range(50):
            id_ = uuid.uuid4().hex
            txt = child.get_text()
            json_dict[id_] = txt
    return json_dict

with open('a', 'r') as html:
    json_data = html_to_json(html.read())
    print(json.dumps(json_data, indent=4))
