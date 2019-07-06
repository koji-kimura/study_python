class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')


class Car(object):
    def run(self):
        print('run')

# 左手に買いたものが優先される


class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


porson_car_robot = PersonCarRobot()
porson_car_robot.talk()
porson_car_robot.run()
porson_car_robot.fly()
