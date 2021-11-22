import yaml
import bson


def main():
    with open("assets/timetable.yaml", "r", encoding="UTF-8") as inputstream:
        data = yaml.load(inputstream, Loader=yaml.Loader)

    print("real data: ", data)

    bsondata = bson.dumps(data)
    print("binary data: ", bsondata)


    with open('assets/timetable.bson', 'wb') as outputstream:  # You will need 'wb' mode in Python 2.x
        outputstream.write(bsondata)

    with open('assets/timetable.bson', "br") as inputstream:
        data = bson.loads(inputstream.readline())

    print("decoded data: ", data)


if __name__ == "__main__":
    main()
