import inspect

def doit(input_array):
    # extracting the way the numbers are gonna be called out into a list
    draw_array = [int(x) for x in input_array[0].split(',') if x not in ('\n')]

    # Mapping out the matrices
    numXcord_map = [[] for _ in range(100)]
    num_of_matrices = 0
    mat_start = 2 #to reach the start of the next matrix just add 6
    i = 0
    while(mat_start < len(input_array)):
        for i in range(mat_start, mat_start+5):
            temp_row = [int(x) for x in input_array[i].replace('\n', '').split(' ') if x not in ('\n')]
            print(temp_row)
            print('-------\n')
            for x_cord in range(len(temp_row)):
                numXcord_map[temp_row[x_cord]].append((int((mat_start-2)/6), x_cord, i-mat_start, temp_row[x_cord])) #the map values are of the format: (matrix_number, x-cord, y-cord)
        mat_start += 6
    print(numXcord_map)
    return 0