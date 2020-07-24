import shush as s
import time

m0 = s.Motor(0)
m1 = s.Motor(1)
m2 = s.Motor(2)
m3 = s.Motor(3)
m4 = s.Motor(4)
m5 = s.Motor(5)

while True:
    m0.move_velocity(0, 10000)
    m0.stop_motor()
    time.sleep(2)
    m1.move_velocity(0, 10000)
    m1.stop_motor()
    time.sleep(2)
    m2.move_velocity(0, 10000)
    m2.stop_motor()
    time.sleep(2)
    m3.move_velocity(0, 10000)
    m3.stop_motor()
    time.sleep(2)
    m4.move_velocity(0, 10000)
    m4.stop_motor()
    time.sleep(2)
    m5.move_velocity(0, 10000)
    m5.stop_motor()
    time.sleep(2)
