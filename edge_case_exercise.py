def move(my_list, direction):
    index_of_one = my_list.index(1)
    if direction == 'right':
        if index_of_one < 3:
          my_list[index_of_one] = 0
          my_list[index_of_one + 1] = 1
        else:
            pass
    elif direction == 'left':
        if index_of_one > 0:
           my_list[index_of_one] = 0
           my_list[index_of_one - 1] = 1
        else:
            pass
    return my_list
