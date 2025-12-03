import time

# def doit(input_array):
#     returnee = 0
#     initial = 50
#     for i in input_array:
#         if i[0]=="L":
#             initial -= int(i[1:])
#         else:
#             initial += int(i[1:])
#         while initial>99:
#             initial = initial - 100
#         while initial<0:
#             initial = initial + 100
#         if initial==0:
#             returnee+=1
#     return returnee

#5861

def doit(input_array):
    hits = 0
    initial = 50
    prev = 50
    for i in input_array:
        (full_rot, rot) = divmod(int(i[1:]), 100)
        hits+=full_rot
        if i[0]=="L":
            rot*=-1
        # print(hits)
        # print(initial)
        # print(rot)
        # print("=======")
        if initial+rot<0:
            if initial>0:
                hits+=1
            initial = initial+rot+100
        elif initial+rot>100:
            hits+=1
            initial= initial+rot-100
        elif initial+rot==0:
            hits+=1
            initial=0
        elif initial+rot==100:
            hits+=1
            initial=0
        else:
            initial = initial+rot

    return hits