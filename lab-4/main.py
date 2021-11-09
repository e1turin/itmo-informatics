import YAML
import XML


def main():
    struct: dict = dict()

    with open("./timetable.yaml", 'r', encoding="UTF-8") as source:

        struct = YAML.parse(source)

    # with open("./timetable.xml", 'w', encoding="UTF-8") as output:

        # output.write(XML.create(struct))

    print(struct)


if __name__ == '__main__':
    main()
