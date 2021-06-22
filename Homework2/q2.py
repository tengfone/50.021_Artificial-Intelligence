"""
Phang Teng Fone 1003296 A.I Coding Hw1 Question 2
"""
from search import Problem, breadth_first_search

"""
Part 1:
Current City And Current Time
"""


class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time

    def __str__(self):
        return str((self.start_city, self.start_time))+' -> ' + str((self.end_city, self.end_time))

    def match(self, city, time) -> bool:
        """
        Part 2:
        This question is so unclear.
        """
        for eachFlight in flightDB:
            if eachFlight.start_city == city:
                if eachFlight.start_time >= time:
                    return True
        return False

    __repr__ = __str__


class FlightProblem(Problem):
    """A fight is specied with a starting city and
    time and an ending city and time. Cities are represented as strings and times
    as integers.
    We want to be able to answer queries that are specied with a starting city,
    starting time, nal destination city and deadline time. The objective is to nd
    a sequence of fights, starting in the starting city, leaving sometime at or after the
    starting time, and arriving at the nal destination before (or at) the deadline.
    """

    def __init__(self, initial, goal):
        """
        City is 0, Time is 1
        """
        super().__init__(initial, goal=goal)

    def actions(self, state):
        "Check neighboring flight to flight db if it meets constraint"
        flightList = []
        for eachFlight in flightDB:
            if state[0] == eachFlight.start_city:
                if eachFlight.start_time >= state[1]:
                    flightList.append(eachFlight)
        return flightList

    def result(self, state, action):
        "Place the action into a new state"
        return action.end_city, action.end_time

    def goal_test(self, state):
        "Check if reach city and time is equal or less than goal"
        if state[0] == self.goal[0] and state[1] <= self.goal[1]:
            return True


flightDB = [Flight('Rome', 1, 'Paris', 4),
            Flight('Rome', 3, 'Madrid', 5),
            Flight('Rome', 5, 'Istanbul', 10),
            Flight('Paris', 2, 'London', 4),
            Flight('Paris', 5, 'Oslo', 7),
            Flight('Paris', 5, 'Istanbul', 9),
            Flight('Madrid', 7, 'Rabat', 10),
            Flight('Madrid', 8, 'London', 10),
            Flight('Istanbul', 10, 'Constantinople', 10)]


def main():

    def find_itinerary(start_city, start_time, end_city, deadline):
        """
        Part 3:
        Returns a plan, in the form of a se-quence of (city, time) pairs, that represents a legal sequence of 
        ights (found in FlightDB) from start city to end city before a specied deadline.
        """
        try:
            return breadth_first_search(FlightProblem(
                initial=(start_city, start_time), goal=(end_city, deadline)))
        except AttributeError:
            print("Cannot Find Flight Iternary, try using a Teleporter Instead")

    def find_shortest_itinerary(start_city, end_city):
        """
        Part 4:
        Return a list of (location,time) tuples representing
        the shortest path between the two locations.
        """
        deadline = 1
        shortest = None
        while shortest is None:
            shortest = find_itinerary(start_city, 1, end_city, deadline)
            deadline += 1
        return shortest, deadline

    def challenge_find_shortest_itinerary(start_city, end_city):
        """
        Done in O(logn).
        Inspired by Binary Search 
        """
        interval = 1
        flag = True
        deadline = 1
        while flag:
            short = find_itinerary(start_city, 1, end_city, deadline)
            if short:
                flag = False
            else:
                deadline += interval

        upperBound = deadline
        lowerBound = short.state[1]

        while lowerBound < upperBound:
            mid = (upperBound + lowerBound) // 2
            shortest = find_itinerary(start_city, 1, end_city, mid)
            if shortest:
                upperBound = shortest.state[1]
            else:
                lowerBound = mid + 1

        return find_itinerary(start_city, 1, end_city, upperBound)

    # Part 2:
    flight = Flight('Rome', 1, 'Paris', 4)
    p2 = flight.match('Rome', 8)
    print(f'Part 2\nFor Flight: Rome at Hour 8 returns: {p2}')

    # Part 3:
    print("\nPart 3")
    p3StartCity = 'Rome'
    p3StartTime = 1
    p3EndCity = 'Istanbul'
    p3deadline = 9
    try:
        p3 = find_itinerary(p3StartCity, p3StartTime,
                            p3EndCity, p3deadline).solution()
        if p3:
            print(
                f'Starting From {p3StartCity} at {p3StartTime} hour(s) with a deadline of {p3deadline} hour(s) to {p3EndCity}, your travese route is/are\n{p3}')
    except:
        print("Cannot Find Flight Iternary, try using a Teleporter Instead")

    # Part 4:
    """
    This strategy will find the shortest time for the deadline. However, if there is no solution, the loop will not stop.
    If the shortest path is length 200, if N = 100 takes n number of steps, N = 200 will gives 2n steps.
    """
    print("\nPart 4")
    p4StartCity = 'Rome'
    p4EndCity = 'Istanbul'
    p4, p4d = find_shortest_itinerary(p4StartCity, p4EndCity)
    if p4:
        print(
            f'Starting From {p4StartCity} and calculated deadline {p4d}, your travese route is/are\n{p4.solution()}')

    # Challenge:
    """
    Try to minimize the number of times your procedure calls find itinerary!
    """
    print("\nAdditional Challenge:")
    pcStartCity = 'Rome'
    pcEndCity = 'Istanbul'
    pcOut = challenge_find_shortest_itinerary(pcStartCity, pcEndCity).solution()
    print(pcOut)


if __name__ == '__main__':
    main()
