def move(my_list, direction):
    # Make a copy of the list so we don't modify the original
    new_list = my_list[:]

    # Finds the index of the one in the list
    index_of_one = new_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        if new_list[-1] == 1:
            new_list = new_list
        else:
            new_list[index_of_one] = 0
            new_list[index_of_one + 1] = 1

    elif direction == 'left':
        if new_list[0] == 1:
            new_list = new_list
        else:
            new_list[index_of_one] = 0
            new_list[index_of_one - 1] = 1

    return new_list
