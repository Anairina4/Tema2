import csv
import json

if __name__ == '__main__':
    with open("cars.csv") as f:
        dict_reader = csv.DictReader(f)
        cars_list = list(dict_reader)

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]

        for car in cars_list:
            car['ID'] = id(car)
            if(int(car['Horse Power']) < 120):
                list1.append(car)
            elif(120 <= (int(car['Horse Power'])) < 180):
                list2.append(car)
            elif(int(car['Horse Power']) >= 180):
                list3.append(car)

            if (int(car['Price']) < 1000):
                list4.append(car)
            elif (1000 <= (int(car['Price'])) < 5000):
                list5.append(car)
            elif (int(car['Price']) >= 5000):
                list6.append(car)

        with open("slow_cars.json","w") as f:
            json.dump(list1,f)
        with open("fast_cars.json","w") as f:
            json.dump(list2,f)
        with open("sport_cars.json","w") as f:
            json.dump(list3,f)

        with open("cheap_cars.json", "w") as f:
            json.dump(list4, f)
        with open("medium_cars.json", "w") as f:
            json.dump(list5, f)
        with open("expensive_cars.json", "w") as f:
            json.dump(list6, f)

