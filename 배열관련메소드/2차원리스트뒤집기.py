mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist))) # *꼭붙여줘야함.

# new_list == [[1,4,7],[2,5,8],[3,6,9]]