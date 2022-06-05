if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        a_list = my_list.copy()
        a_list[idx] = element
        return a_list
