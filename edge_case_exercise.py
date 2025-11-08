def move(my_list, direction):
    # Make a copy of the list so we don't modify the original
    new_list = my_list[:]

    # Finds the index of the one in the list
    index_of_one = new_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        # check the position of the 1, not just the last element
        if index_of_one == len(new_list) - 1:
            return new_list
        else:
            new_list[index_of_one] = 0
            new_list[index_of_one + 1] = 1

    elif direction == 'left':
        if index_of_one == 0:
            return new_list
        else:
            new_list[index_of_one] = 0
            new_list[index_of_one - 1] = 1

    return new_list
