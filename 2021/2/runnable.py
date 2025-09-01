import inspect

# SOLUTION TO THE FIRST PART
# def doit(input_array):
#     up_total = 0
#     down_total = 0
#     forward_total = 0
#     for i in input_array:
#         if i[0]=='u':
#             up_total+=int(i[-2])
#         elif i[0]=='d':
#             down_total+=int(i[-2])
#         elif i[0]=='f':
#             forward_total+= int(i[-2])
#     depth = down_total-up_total
#     return depth*forward_total

def doit(input_array):
    aim = 0
    depth = 0
    forward_total = 0
    for i in input_array:
        if i[0]=='u':
            aim -= int(i[-2])
        elif i[0]=='d':
            aim += int(i[-2])
        elif i[0]=='f':
            forward_total += int(i[-2])
            depth += aim*int(i[-2])
    return depth*forward_total