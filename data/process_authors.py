import json
import string
import re

names = []
with open("authors.json", "r") as f:
    names = json.load(f)

filtered = []
for n in names:
    new = ''.join(x for x in n if x in string.printable)
    if n != new:
        print n + "\t" + new
    else:
        if re.search("[0-9]+", n) is not None:
            print n
        else:
            filtered.append(n)
output = [" ".join(filtered)]
print output

with open("data.json", "w") as f:
    json.dump(output, f, indent=4)

