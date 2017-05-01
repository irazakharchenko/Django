# coding=utf-8
"""
Домашнее задание №2.
"""

TEST = True  # установите True, чтобы запустить проверку


"""
***********************************************
1. Нужно посчитать количество счастливых билетов.
Билет состоит из парного количества цифр от 2 до 6.
Билет не может состоять только из нулей.
Счастливым билетом считается тот, у которого сумма первой половины цифр равна сумме второй половины.
Например: 22, 1405, 001010, 184616, 119227 и т.д.
***********************************************
"""

def checker(a, len_n):
    r = a % (10**(len_n/2))

    l = a / (10**(len_n/2))
    if sum_num(r) == sum_num(l):
        return True
    return False

def sum_num(b):
    sum_b = 0
    while b > 0:


        sum_b += b % 10
        b /= 10
    return sum_b


def calc_happy_tickets(numbers_len):
    assert 2 <= numbers_len <= 20 and numbers_len % 2 == 0
    # писать решение сюда #
    dil =  10**(numbers_len/2)
    el = dil +1
    fin = 10**(numbers_len)
    k = 0
    pr =dil+1
    while fin > el:
        #print 'el = ' + str(el)
        if checker(el, numbers_len):
            k += 1
        el += 9
        if (pr/dil) != el/dil:
            el = el/dil * (dil)
            sum1 = sum_num(el/dil)
            i = 0
            while sum1>8:
                el += 9 * (10**i)
                i+=1
                sum1-=9
            el += sum1 * (10 ** i)
        pr = el
    return k



if TEST:
    assert calc_happy_tickets(2) == 9
    assert calc_happy_tickets(4) == 669
    print 'Task 1 OK'


"""
***********************************************
2. Написать класс, который считает количество созданных им инстансов.
Метод класса get_created_instances_count должен возвращать это число.
***********************************************
"""


class CreatedInstancesCounter(object):
    # писать решение сюда #
    counter = 0

    def __new__(cls, *args, **kwargs):
        cls.counter += 1

    @classmethod
    def get_created_instances_count(cls):
        return cls.counter


if TEST:
    for i in xrange(56):
        CreatedInstancesCounter()

    assert CreatedInstancesCounter.get_created_instances_count() == 56
    CreatedInstancesCounter()
    assert CreatedInstancesCounter.get_created_instances_count() == 57
    print 'Task 2 OK'


"""
***********************************************
3. Написать два класса: сотрудник и команда.
Сотрудник имеет имя, стоимость работы (долларов в час) и уровень квалификации (от 0 до 9).
Если сложить сотрудников (оператор +), то будет создана команда, которая будет иметь уровень
квалификации (максимальный уровень из всех сотрудников в команде), стоимость (сумма стоимости
всех сотрудников команды) и список всех сотрудников.
Объект команды можно итерировать.
К команде можно добавлять сотрудника с помощью оператора += или используя метод add.
Если до команды добавить сотрудника (+), то будет создана новая команда.
Также можно удалять сотрудника с помощью метода remove (который принимает объект сотрудника, как аргумент).
Если сделать вывод сотрудника (строковое представление), то должно выводится в следующем формате:
"Name (cost=10, level=5)"
Если сделать вывод команды (строковое представление), то должно выводится в следующем формате:
"Command (cost=25, level=8) [Name1 (cost=10, level=5), Name2 (cost=15, level=8)]"
Если попытатся сделать комманду с дублированным сотрудником, то должно вызыватся исключение (raise ValueError)
***********************************************
"""


class Employee(object):
    # писать решение сюда #
    def __init__(self, name,cost, level):
        self.name = name
        self.cost = cost
        self.level = level


    def __str__(self):
        return "{q.name} (cost={q.cost}, level={q.level})".format(q=self)

    def __add__(self, other):
        com = Command(self, other)
        return com


class Command(object):
    # писать решение сюда #
    def __init__(self, pers1, pers2):

        if isinstance(pers1, self.__class__) or isinstance(pers2, self.__class__):
            if isinstance(pers2, self.__class__):
                pers1, pers2 = pers2, pers1
            self.com = pers1.com + [pers2]
            self.com_names = pers1.com_names + [pers2.name]
            self.com_cost = pers1.com_cost + pers2.cost
            self.com_level = max(pers1.com_level, pers2.level)
            self.info_list = pers1.info_list[:-1] + ', ' + str(pers2) + ']'
        else:
            if pers1 != pers2:
                self.com = [pers1]+[pers2]

                self.com_names = [pers1.name] + [pers2.name]
                self.com_cost = pers2.cost + pers1.cost
                self.com_level = max(pers2.level, pers1.level)
                self.info_list = '['
                for el in [str(pers1), str(pers2)]:
                    self.info_list += el + ', '
                self.info_list = self.info_list[:-2] + ']'
            else:
                raise ValueError
        self.index_reset()


    def __str__(self):
        #print self.com_level, self.com_names
        return 'Command (cost={u.com_cost}, level={u.com_level}) {u.info_list}'.format(u = self)

    def __len__(self):
        return len(self.com)

    def __iter__(self):
        return self

    def index_reset(self):
        self.index = 0

    def next(self):

        if self.index == len(self.com):
            self.index_reset()
            raise StopIteration
        self.index += 1
        return self.com[self.index-1]

    def __add__(self, other):
        if isinstance(other, Employee):

            if other.name not in self.com_names:

                return self.__class__(other, self)
            else:

                raise ValueError

    def __iadd__(self, other):
        if other.name not in self.com_names:
            self.com += [other]
            self.com_names += [other.name]
            self.com_cost += other.cost
            self.com_level = max(self.com_level, other.level)
            self.info_list = self.info_list[:-1] + ', ' + str(other) + ']'
            return self
        else:
            raise ValueError

    def add(self, other):

        if isinstance(other, Employee):

            if other.name not in self.com_names:

                return self.__class__(other, self)
            else:
                raise ValueError




    def remove(self, per):
        if per in self.com:
            self.com.remove(per)
            self.com_names.remove(per.name)
            self.com_cost -= per.cost
            if self.com_level == per.level:
                self.com_level = max(x.level for x in self.com)
            self.info_list = '['
            for el in [str(x) for x in self.com]:
                self.info_list += el + ', '
            self.info_list = self.info_list[:-2] + ']'

if TEST:
    # создание объектов сотрудников
    emp1 = Employee('Ivan', 12, 4)
    emp2 = Employee('Sidor', 15, 6)
    emp3 = Employee('Joe', 26, 8)
    # проверка строкового представления объектов сотрудников
    assert str(emp1) == 'Ivan (cost=12, level=4)'
    assert str(emp2) == 'Sidor (cost=15, level=6)'
    assert str(emp3) == 'Joe (cost=26, level=8)'

    # создание команды из двух сотрудников
    com1 = emp1 + emp2
    # проверка строкового представления созданного объекта
    #print str(com1)
    assert str(com1) == 'Command (cost=27, level=6) [Ivan (cost=12, level=4), Sidor (cost=15, level=6)]'
    # проверка длины
    assert len(com1) == 2
    # проверка на итерабельность


    assert list(com1) == [emp1, emp2]
    assert [t for t in com1] == [emp1, emp2]

    # создание другой команды из команды com1 и сотрудника emp3
    com2 = com1 + emp3
    # проверка строкового представления созданного объекта
    i = 0

    assert str(com2) == 'Command (cost=53, level=8) [Ivan (cost=12, level=4), Sidor (cost=15, level=6), Joe (cost=26, level=8)]'

    # создание объекта нового сотрудника
    emp4 = Employee('Max', 35, 9)
    t = com1  # копирование ссылки на команду com1
    com1 += emp4  # добавление сотрудника emp4 в команду com1
    # не изменился ли объект в переменной com1
    assert t is com1
    # проверка строкового представления com1

    assert str(com1) == 'Command (cost=62, level=9) [Ivan (cost=12, level=4), Sidor (cost=15, level=6), Max (cost=35, level=9)]'

    # удаление сотрудника из команды
    com1.remove(emp1)
    # проверка строкового представления com1
    assert str(com1) == 'Command (cost=50, level=9) [Sidor (cost=15, level=6), Max (cost=35, level=9)]'

    # создание новой команды из сотрудника emp1 и команды com1 (другой порядок операндов)
    com3 = emp1 + com1
    # проверка строкового представления новой команды
    assert str(com3) == 'Command (cost=62, level=9) [Sidor (cost=15, level=6), Max (cost=35, level=9), Ivan (cost=12,' \
                        ' level=4)]'

    # попытка добавить в команду сотрудника, который там уже есть или создать команду из дублирующих сотрудников
    try:
        com3.add(emp1)
        t = False
    except ValueError:

        t = True  # если получили исключение, тогда все ок
    assert t
    try:
        com3 += emp1
        raise AssertionError
    except ValueError:
        pass
    try:
        com3 + emp1
        raise AssertionError
    except ValueError:
        pass
    try:
        emp1 + emp1
        raise AssertionError
    except ValueError:
        pass

    print 'Task 3 OK'
