class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


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
