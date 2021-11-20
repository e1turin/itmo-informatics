import YAML
import XML
import exeptions


def main():
    struct: dict = dict()

    with open("./timetable.yaml", 'r', encoding="UTF-8") as source:
        struct = YAML.parse(source)

    with open("./timetable.xml", 'w', encoding="UTF-8") as output:
        # print(struct)
        XML.create(elements=struct, root="", file=output)  # , singlestring=True))


if __name__ == '__main__':
    main()
