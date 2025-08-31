#CODE FOR FIRST PART:
# def doit(input_array):
#     int_input_array = []
#     for i in input_array:
#         int_input_array.append(int(i))
#     prev = int_input_array[0]
#     count = 0
#     for i in range(1, len(input_array)):
# #        print(input_array[i] + " compared to " + str(prev))
#         if(int_input_array[i]>prev):
# #            print("increased\n")
#             count +=1
# #        else:
# #            print("decreased\n")
#         prev = int_input_array[i]
#     return count

def doit(input_array):
    three_int_input_array = []
    for i in range(2, len(input_array)):
        three_int_input_array.append((int(input_array[i-2])+int(input_array[i-1])+int(input_array[i])))
    prev = three_int_input_array[0]
    count = 0
    for i in range(1, len(three_int_input_array)):
#        print(input_array[i] + " compared to " + str(prev))
        if(three_int_input_array[i]>prev):
#            print("increased\n")
            count +=1
#        else:
#            print("decreased\n")
        prev = three_int_input_array[i]
    return count