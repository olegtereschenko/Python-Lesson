from time import sleep
class TrafficLight:
    __color = 'черный'
    def running(self):
        while True:
            print('TrafficLight красный свет')
            sleep(7)
            print('TrafficLight желтый свет')
            sleep(2)
            print('TrafficLight зеленый свет')
            sleep(7)
            print('TrafficLight желтый свет')
            sleep(2)
trafficlight = TrafficLight()
trafficlight.running()