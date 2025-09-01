import inspect

#THE FIRST SOLUTION
# def doit(input_array):
#     gamma = ""
#     epsilon = ""
#     for i in range(0,len(input_array[0])-1): #the -1 is for the \n at the end of each element
#         zero_count = 0
#         one_count = 0
#         for j in range(0,len(input_array)):
#             if input_array[j][i] == '1':
#                 one_count += 1
#             else:
#                 zero_count += 1
#         if(one_count>zero_count):
#             gamma += '1'
#             epsilon += '0'
#         else:
#             gamma += '0'
#             epsilon += '1'
#     return int(gamma, base=2)*int(epsilon, base=2)


def doit(input_array):
    true_bucket = input_array
    one_bucket = []
    zero_bucket = []
    oxy = ""
    co2 = ""
    i = 0
    while(len(true_bucket)>1):
        for j in range(0,len(true_bucket)):
            if true_bucket[j][i]=='0':
                zero_bucket.append(true_bucket[j])
            else:
                one_bucket.append(true_bucket[j])
        if(len(zero_bucket)>len(one_bucket)):
            true_bucket = zero_bucket
        else:
            true_bucket = one_bucket
        zero_bucket = []
        one_bucket = []
        i += 1
    oxy = true_bucket[0]
    true_bucket = input_array
    i = 0
    while(len(true_bucket)>1):
        for j in range(0,len(true_bucket)):
            if true_bucket[j][i]=='0':
                zero_bucket.append(true_bucket[j])
            else:
                one_bucket.append(true_bucket[j])
        if(len(one_bucket)<len(zero_bucket)):
            true_bucket = one_bucket
        else:
            true_bucket = zero_bucket
        zero_bucket = []
        one_bucket = []
        i += 1
    co2 = true_bucket[0]
    return int(oxy, base=2)*int(co2, base=2)