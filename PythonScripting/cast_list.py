def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as cast:
        """ Reads a file and goes over the amount specified in the parenthesis """
        for cst in cast:
            cast_list.append(cst.split(",")[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
