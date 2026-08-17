# import re
# import inspect

# def doit(input):
#     input_array = input[0].split(",")
#     ranges = []
#     for i in input_array:
#         ranges.append(tuple(i.split("-")))

#     hits = 0
#     for i in ranges:
#         start, end = i
#         for n in range(int(start), int(end)+1):
#             num = str(n)
#             l = len(num)
#             if l%2==0:
#                 temp = num[:l//2]
#                 temp = re.search(temp*2, num)
#                 if temp:
#                     hits+=int(temp.group(0))
    
#     return hits

import re
import inspect

def doit(input):
    input_array = input[0].split(",")
    ranges = []
    for i in input_array:
        ranges.append(tuple(i.split("-")))

    hits = 0
    for i in ranges:
        start, end = i
        for n in range(int(start), int(end)+1):
            num = str(n)
            l = len(num)
            for i in range(1,l):
                temp = num[:i]
                if num==temp*(l//i):
                    # print(num)
                    hits+=int(num)
                    break
    
    return hits