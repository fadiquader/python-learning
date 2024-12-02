import os.path
from pathlib import Path
import json

path = Path('pi_digits.text')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError as e:
    print(f"File not found: {path}")
    # pass
    exit(1)
else:
    print(f"File found: {path}")

lines = contents.splitlines()
words = contents.split()
num_words = len(words)
print(f"Number of words: {num_words}")
# for line in lines:
#     print(line)
#
# path.write_text(contents.format() + '\nI Love Programming!')

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
path_n = Path('numbers.json')
contents_n = json.dumps({
    'numbers': numbers
})
path_n.write_text(contents_n)

print(f"Number in json: {json.loads(path_n.read_text())}")

# file exists?
path_u = Path('username.json')
if not path_u.exists():
    path_u.touch() # create the file

# check isFile
if os.path.isfile('username.json'):
    print("Username file exists: username.json")
else:
    outfile = open('username.json', 'w')
    outfile.write(json.dumps({}))
    outfile.close()

# count word occurrence in a file
def count_words(filename):
    # try:
    #     with open(filename, 'r', encoding='utf-8') as infile:

    try:
        infile = open(filename, 'r')
    except IOError as e:
        print(f"Filname doesn't exist: {e}")

    dict1 = dict()
    for line in infile:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
    for key in list(dict1.keys()):
        print(f"{key}: {dict1[key]}")

    return dict1

# Assigment expression
def matching_lines_from_file(path, pattern):
    with open(path) as handle:
        while (line := handle.readline()) != '':
            print(line)

# generator
def lines_from_file(path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')
