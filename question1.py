'''Given an empty list and a stream of N numbers. Print min, max, sum, average and 
mode (optional and if there are multiple modes then print any) after insertion of each 
element from the stream to the list.
Example Input:
5
2 4 3 2 -3
Example output
▪ min, max, sum, average and mode after addition of 2 is 2, 2, 2, 2, 2.
▪ min, max, sum, average and mode after addition of 4 is 2, 4, 6, 3, 4.
▪ min, max, sum, average and mode after addition of 3 is 2, 4, 9, 3, 4.
▪ min, max, sum, average and mode after addition of 2 is 2, 4, 11, 2.75, 2.
▪ min, max, sum, average and mode after addition of -3 is -3, 3, 8, 1.6, 2.
'''

from collections import defaultdict

class StreamStatistics:
    def _init_(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')
        self.sum_val = 0
        self.count = 0
        self.mode = None
        self.mode_count = 0
        self.frequency = defaultdict(int)
    
    def add_number(self, num):
        # Update min and max
        self.min_val = min(self.min_val, num)
        self.max_val = max(self.max_val, num)
        # Update sum
        self.sum_val += num
        # Update count
        self.count += 1
        # Update mode
        self.frequency[num] += 1
        if self.frequency[num] > self.mode_count:
            self.mode_count = self.frequency[num]
            self.mode = num
    
    def get_statistics(self):
        average = self.sum_val / self.count if self.count > 0 else 0
        return self.min_val, self.max_val, self.sum_val, average, self.mode

def print_statistics(stream):
    stats = StreamStatistics()
    for num in stream:
        stats.add_number(num)
        min_val, max_val, sum_val, average, mode = stats.get_statistics()
        print(f"min, max, sum, average and mode after addition of {num} is {min_val}, {max_val}, {sum_val}, {average}, {mode}.")

# Example Input
stream = [2, 4, 3, 2, -3]
print_statistics(stream)

'''def min_val(lst):
    return min(lst)

def max_val(lst):
    return max(lst)

def sum_val(lst):
    return sum(lst)

def avg_val(lst):
    return sum(lst) / len(lst)

def mode_val(lst):
    counts = {}
    mode = lst[0]
    max_count = 1
    current_count = 1

    lst.sort()

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            mode = lst[i]

    return mode

if _name_ == "_main_":
    n = int(input())
    a = list(map(int, input().split()))

    v = []

    for i in range(n):
        v.append(a[i])
        print(f"min, max, sum, average and mode after addition of {a[i]} is {min_val(v)} {max_val(v)} {sum_val(v)} {avg_val(v):.2f} {mode_val(v)}")'''
    