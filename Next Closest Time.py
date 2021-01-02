# https://leetcode.com/problems/next-closest-time/

"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")

        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        two_digit_values = []
        for a in nums:
            for b in nums:
                two_digit_values.append(a + b)

        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i + 1] < "60":
            return hour + ":" + two_digit_values[i + 1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i + 1] < "24":
            return two_digit_values[i + 1] + ":" + two_digit_values[0]

        # Return the earliest time of the next day
        return two_digit_values[0] + ":" + two_digit_values[0]


# Same logic with use of functions and binary search
def nextClosestTime(self, time):
    """
    :type time: str
    :rtype: str
    """
    # Extract the given hour and given minute from the time, split on :, and the 0 would be hour
    # and 1 would be minute
    given_hour, given_minute = time.split(":")[0], time.split(":")[1]
    # we are interested in the time digits, so remove the :
    time_digits = time.replace(":", "")

    # sort the digits in a set.
    digits_set = set(x for x in time_digits)
    digits_set = sorted(digits_set)

    # permutate between the digits to create what all available times exist.
    available_times = self.getAvailableTimes(digits_set)

    # get the next largest minute if possible.
    next_largest_minute = self.getNextLargestMinute(given_minute, available_times)

    # if there is indeed a next largest minute, you are all set, combine it with given hour.
    if next_largest_minute != -1:
        return given_hour + ":" + next_largest_minute

    # if there is not a next largest minute -
    #  1] find the next smallest minute. Possible to attach it to the next largest hour, and thats the time.
    else:
        smallest_minute = self.getSmallest(available_times)

        # get the next largest hour if possible.
        next_largest_hour = self.getNextLargestHour(given_hour, available_times)

        # if there is a next largest hour, you can attach the next largest hour to the smallest minute and
        # thats the next time.
        if next_largest_hour != -1:
            return next_largest_hour + ":" + smallest_minute
        # if there is no next largest hour for the day, then -
        #    we are into the next day.
        #    for the next day, we are looking for the smallest time, therfore it would be the combination of smallest.
        else:
            return smallest_minute + ":" + smallest_minute


def getAvailableTimes(self, digits):
    times = []

    for outer_digit in digits:
        for inner_digit in digits:
            times.append(outer_digit + inner_digit)

    return times


def getNextLargestMinute(self, minute, times):
    index_of_minute = self.getIndex(minute, times)

    if index_of_minute + 1 < len(times):
        if int(times[index_of_minute + 1]) in range(0, 60):
            return times[index_of_minute + 1]

    return -1


def getNextLargestHour(self, hour, times):
    index_of_hour = self.getIndex(hour, times)

    if index_of_hour + 1 < len(times):
        if int(times[index_of_hour + 1]) in range(0, 24):
            return times[index_of_hour + 1]

    return -1


def getSmallest(self, times):
    return times[0]


def getIndex(self, element, times):
    low, high = 0, len(times) - 1

    while low <= high:
        middle = (low + high) // 2

        if element == times[middle]:
            return middle
        elif element > times[middle]:
            low = middle + 1
        elif element < times[middle]:
            high = middle - 1

    return len(times)
