import datetime,random, time

class Bus:
    '''

    the bus class would be instantiated with the name, destination and expected time of arrival( this would be received by a tuple in this strict order.
    it would have attributes to tell the program if it is due or not the $self.isDue attribute.
    the $self.is available attribute would tell the program if the bus is still available , if true the programme displays it.

    it has 2 methods. the output methods would modify the self.isDue and self.isAvailable and the displayBus functions would determine the data to be display

    '''

    def __init__(self, *args):
        self.name, self.destination, self.arrival_time = args
        self.available = True
        self.isDue = False

    def output(self):
        now = datetime.datetime.now()
        self.timeLeft = (self.arrival_time - now).total_seconds()
        self.timeLeftMin = self.timeLeft//60

        if self.timeLeft <= 59:
            self.isDue = True
            if self.timeLeft <= -60: # buses would appear to be due for more than 1 minute before it is unavailable
                self.available = False

    def displayBus(self):
        global data
        data = ''
        self.output()

        if self.available is True:
            if self.isDue:
                data += f'Bus {self.name} arriving at {self.destination} is due'

            else:
                data += f'Bus {self.name} would be arriving at {self.destination} in {int((self.timeLeftMin))} min at {self.arrival_time.hour}:'
                if self.arrival_time.minute < 10:
                    data += f'0{self.arrival_time.minute}'
                else:
                    data += f'{self.arrival_time.minute}'
        if data != '' or not None:
            return data
        else:
            return None



#Array of buses and their times

buses = {
    319: 'Sloanne Square',
         250: 'West Croydon',
         255: 'Croydon Town Centre',
         678: 'White City',
         109: 'Streatham Station',
         501: 'East Croydon',
         345: 'South Kesignthon Station',
         702: 'Angel',
         325: 'Lewisham',
         462: 'Moorgate'}

# To instantiate the base time on which bus times would be created at the start of the programe
now = datetime.datetime.now()

# generates a list of timestamps from 0 to 10 mins using list comprehensions
times = [now + datetime.timedelta(seconds=random.randint(0, 600)) for i in buses]

maxTime = (max(times))

#allocate times to the buses by merging the bus dictionaries and the times created randomly

busesAndTimes = zip(buses.items(), times)

listOfBusTimes = () #a tuple to group single buses to their times.

for busTime in busesAndTimes:
    busName, busDestination = busTime[0]
    busTime = busTime[1]
    listOfBusTimes += (busName, busDestination, busTime),

# sorts the array of the list of buses with their times
listOfBusTimes_timeSorted = sorted(listOfBusTimes, key=lambda x: x[2])

# a dictionary for all the bus objects

busObjectArray = {}

#create all the bus objects using the tuple and the class Bus.

for buses in listOfBusTimes_timeSorted:
    busObjectArray[buses[1]] = Bus(buses[0], buses[1], buses[2])


#a recursive funcitons to display buses available and their times.
def displayPanel(buses):
    for name in buses:
        time.sleep(0.7)
        data = buses[name].displayBus()
        if data:
            print(data)

    print('\n-------------------------\n')
    time.sleep(60)

    #a terminator for the recursive function if last bus avaiable is due
    if maxTime >= datetime.datetime.now():
        displayPanel(buses)
    else:
        print("No available bus through this route.\nCheck on your app for alternative routes")


displayPanel(busObjectArray)
