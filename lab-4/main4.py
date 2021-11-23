import yaml
import bson
import toml


def main():
    with open("assets/timetable.yaml", "r", encoding="UTF-8") as inputstream:
        data = yaml.load(inputstream, Loader=yaml.Loader)

    print("real data: ", data)

    print("\n-----------\n")

    bsondata = bson.dumps(data)
    print("binary data: ", bsondata)

    print("\n-----------\n")

    tomldata = toml.dumps(data)
    print("toml data:\n\n", tomldata.strip())


    with open('assets/timetable.bson', 'wb') as outputstream:  # You will need 'wb' mode in Python 2.x
        outputstream.write(bsondata)

    with open('assets/timetable.bson', "br") as inputstream:
        data = bson.loads(inputstream.readline())

    print("\n-----------\n")

    print("decoded BSON data: ", data)

    with open('assets/timetable.toml', 'w', encoding="UTF-8") as outputstream:  # You will need 'wb' mode in Python 2.x
        outputstream.write(tomldata)

    with open('assets/timetable.toml', "r", encoding="UTF-8") as inputstream:
        inputstring = ''.join(inputstream.readlines())

    print("\n-----------\n")

    data = toml.loads(inputstring)
    print("decoded TOML data: ", data)
    # # same resalt:
    # data = toml.load('./assets/timetable.toml')
    # print("decoded TOML data from path: ", data)




if __name__ == "__main__":
    main()
