# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.cal:
            if start <= startTime < end or start < endTime <= end or (startTime < start and endTime > end):
                return False
        self.cal.append([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)