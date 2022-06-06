# mplement a function that removes all the even elements from a given list. Name it remove_even(lst).

def remove_even(lst):

    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            del lst[i]
        else:
            i += 1

    print(lst)


my_list = [1, 2, 4, 5, 10, 6, 3]
remove_even(my_list)
