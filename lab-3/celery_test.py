tests = { 
        1: "Это не просто смешно смешно, это вправду смешно, потому что что люди очень часто ошибаются,  повторяя одни и  те же слова, совершенно не не вдумываясь в них и не понимая их смысла.", 
        2: "В детстве мы с друзьями  любили играть в такую такую игру 'Море волнуется раз, море море волнуется два два, море  волнуется три,  морская фигура  замри!'", 
        3: "Если я нервничал, то начинал  плакать плакать.  Она просто обнимала меня и  и успокаивала.  Потом  начинала баловаться, бегать за мной, хватать, щипать щипать, щекотать, чтобы я прекратил кричать.", 
        4: "Я сидел, смотрел в окно и тут  тут водитель резко тормозит, я подскакиваю, поворачиваюсь и вижу, что  эта девочка лежит на полу и не не шевелится.", 
        5: "На днях зашел к знакомому, сидит за компом компом, работает. А на коленях у него лежит кот кот и смотрит  в монитор.  Мне стало интересно, спросил, что он он там делает.  В ответ услышал, что мой кот помогает помогает ему искать работу."
        }

import celery

for i in range(1,6):
    print(f"Test №{i}:")
    print(tests[i])
    print("result:")
    print(celery.main(tests[i]))



