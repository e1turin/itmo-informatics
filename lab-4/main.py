import YAML


def main():
    with open("./timetable.yaml", 'r', encoding="UTF-8") as source:
        #elementTree: dict[str, str | int] = YAML.parse(source)
        YAML.parse(source)



if __name__ == '__main__':
    main()
