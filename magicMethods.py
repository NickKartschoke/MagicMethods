import csv

filename = r'C:\Users\nickk\repo\Astronaut\astronauts.csv'

astro_list = []

class Astronaut():
    def __init__(self,name,status,spaceflightHr):
        self.__name = name
        self.__status = status
        self.__spaceflightHr = spaceflightHr

    def __gt__(self,other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        return self.__spaceflightHr > other.__spaceflightHr

    def __ge__(self,other):
        print('__gt__ called - self: %s, other: %s' % (self,other))
        return self.__spaceflightHr >= other.__spaceflightHr

    def __eq__(self,other):
        print('__eq__ called')
        return self.__spaceflightHr == other.__spaceflightHr

    def __str__(self):
        return self.__name +", " + self.__status

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for r in reader:
        astro_list.append(Astronaut(r[0],r[3],r[13]))

astro_list.pop(0)

print(astro_list[0] < astro_list[1])