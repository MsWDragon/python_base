import time


class TrafficLight:
    
    __color = ['red', 'yellow', 'green']
    def running(self):
        color_time = {'red': 4, 'yellow': 2, 'green': 3}
        for color in TrafficLight.__color:
            print(f'{color} {color_time[color]} сек')
            time.sleep(color_time[color])

if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()