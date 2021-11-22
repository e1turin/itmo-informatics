import yaml
from xml.dom.minidom import parseString
import xmltodict


def main():
    with open("assets/timetable.yaml", "r", encoding="UTF-8") as inputstream:
        data = yaml.load(inputstream, Loader=yaml.Loader)

    xmldata = parseString(xmltodict.unparse(data))

    with open("assets/timetable-main1.xml", "w", encoding="UTF-8") as outputstream:
        print(xmldata.toprettyxml(), file=outputstream)

if __name__ == "__main__":
    main()