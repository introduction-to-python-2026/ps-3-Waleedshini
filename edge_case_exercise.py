def move(my_list, direction):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
      if my_list[-1] == 1 :
       new_list = my_list
      else:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
        new_list = my_list
    elif direction == 'left':
       if my_list[0]== 1:
        new_list = my_list
       else:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
        new_list = my_list

    return new_list
