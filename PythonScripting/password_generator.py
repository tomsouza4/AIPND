# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    word_len = len(word_list) - 1
    password = ""
    for i in range(0,3):
        password += word_list[random.randint(0,word_len)]
    return password


# test your function
print(generate_password())

"""
To create random passwords we used import random. The function definition was simply:
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
Alternatively, you could use the random.sample function and .join method for strings:

def generate_password():
    return ''.join(random.sample(word_list,3))

"""
