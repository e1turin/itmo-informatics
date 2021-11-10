import PrankFriends


# TODO дописать тесты
lists = {1:
        """
        Серафимов А.А. P3110
        Кокорин И.Д. P3110
        Курочкин Д.Д. N2134
        Веселов К.К. P3110
        """,
         2: """
         
         
            """,
         3: """
         
         
            """,
         4: """
         
         
            """,
         5: """
         
         
            """,
         }

# TODO дописать тесты
groups = {1: "P3110",
          2: "",
          3: "",
          4: "",
          5: ""
          }

for i in range(1, len(lists)+1):
    print("group: ", groups[i])
    print("List was: ", lists[i])
    print("List now: ")
    PrankFriends.listprank(groups[i], lists[i])
    print("---------")


