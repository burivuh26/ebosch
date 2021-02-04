from time import sleep


class TrafficLight:
    __color = 'цвет'

    def running(self):
        while True:
            print('\033[41m')
            sleep(7)
            print('\033[43m')
            sleep(2)
            print('\033[42m')
            sleep(10)
            print('\033[43m')
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
