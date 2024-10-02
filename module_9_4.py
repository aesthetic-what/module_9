import random


first = 'Мама мыла раму'
second = 'Рамена мало было'

first_res = list(map(lambda x, y: x.split() == y.split(), first, second))
print(first_res)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(str(data_set))
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall():
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        choise = random.choice(self.words)
        return choise
    

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())