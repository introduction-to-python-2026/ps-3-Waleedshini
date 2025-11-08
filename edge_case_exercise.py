def move(my_list, direction):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        # Check if moving right is possible (not at the right edge)
        if index_of_one < len(my_list) - 1:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1
        # If at the right edge and trying to move right, do nothing
        else:
            pass # The list remains unchanged

    elif direction == 'left':
        # Check if moving left is possible (not at the left edge)
        if index_of_one > 0:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1
        # If at the left edge and trying to move left, do nothing
        else:
            pass # The list remains unchanged

    return my_list
