def doit(input):
    input_array = input[0].split(",")
    ranges = []
    for i in input_array:
        ranges.append(tuple(i.split("-")))
    print(ranges)