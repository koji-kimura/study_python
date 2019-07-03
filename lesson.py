# この記述で抽象クラスにできる
import abc


class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # この記述で継承クラスにdriveメソッドを強要できる
    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')


baby = Baby()
adult = Adult()

# baby.drive()
adult.drive()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model="Model S",
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        # アンダースコア2こならクラス内でしかいじれない
        self.__enable_auto_run = enable_auto_run
        # 初期値に設定する必要あり
        self.passwd = passwd
    # この記述で読み込み専用になる
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # setterで書き換えできるようになる
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


print("#"*10)

tesla_car = TeslaCar('Lexus', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
