import math

class Car:
    def __init__(self, num):
        self.num = num
        self.accumulate = 0
        self.pay = 0
        self.state = 'IN'
        self.in_time = ''
        

def timeCalculator(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))
    
    total_in_minutes = in_hour * 60 + in_minute
    total_out_minutes = out_hour * 60 + out_minute

    parking_duration = total_out_minutes - total_in_minutes
    
    return parking_duration


def payCalculator(fees, total_time):
    init_time, init_pay, per_time, per_pay = fees
    
    if total_time <= init_time:
        return init_pay
    
    additional_time = total_time - init_time
    additional_pay = math.ceil(additional_time / per_time) * per_pay
    
    return init_pay + additional_pay
    

def solution(fees, records):
    car_dict = {}
    
    for record in records:
        time, num, event = record.split()
        
        if event == "IN":
            if num not in car_dict:
                car_dict[num] = Car(num)
            car_dict[num].in_time = time
            car_dict[num].state = "IN"
        
        elif event == "OUT":
            accumulate = timeCalculator(car_dict[num].in_time, time)
            car_dict[num].accumulate += accumulate
            car_dict[num].state = 'OUT'
    
    
    for car in car_dict.values():
        if car.state == "IN":
            accumulate = timeCalculator(car.in_time, '23:59')
            car.accumulate += accumulate
            car.state = 'OUT'
    
    for car in car_dict.values():
        car.pay = payCalculator(fees, car.accumulate)
    
    sorted_cars = sorted(car_dict.keys(), key=lambda x: int(x))
    result = [car_dict[num].pay for num in sorted_cars]
    
    return result    
