from src import YAML_REGEX as YAML, XML


def main():
    struct: dict = dict()

    with open("assets/timetable.yaml", 'r', encoding="UTF-8") as source:
        struct = YAML.parse(source)
    with open("assets/timetable.xml", 'w', encoding="UTF-8") as output:
        # print(struct)
        XML.create(elements=struct, root="", file=output)  # , singlestring=True))


if __name__ == '__main__':
    main()
