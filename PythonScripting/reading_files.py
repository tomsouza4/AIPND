""" Uses open to open a file and then attributes its value to a variable(f)  """
#f = open('/Users/tomsouza4/GoogleDrive/code/ai-programming-with-python/my_file.txt', 'r')
""" The content read from the file goes on and it's added to a second variable using *.read() method """
#file_data = f.read()
#print(file_data)
""" Once it's done, closes it out """
#f.close()

""" Example when opening up too many files without closing """
#files = []
#for i in range(10000):
#    files.append(open('/Users/tomsouza4/GoogleDrive/code/ai-programming-with-python/my_file.txt', 'r'))
#    print(i)

#with open('/Users/tomsouza4/GoogleDrive/code/ai-programming-with-python/my_file.txt', 'r') as f:
#    file_data = f.read()
#    print(file_data)

with open("camelot.txt") as song:
    """ Reads a file and goes over the amount specified in the parenthesis """
    print(song.read(2))
    print(song.read(8))
    print(song.read())

"""
OUTPUT:
We
're the
knights of the round table
We dance whenever we're able
"""
