from sys import argv

f = open("./sources/" + argv[1] + ".txt", "r")
s = f.read()
f.close()
l = s.split("\n")
_l = []
for line in l:
    if len(line) > 3:
        if line[-1].isnumeric():
            added = False
            for i in range(3):
                if not line[-2-i].isnumeric():
                    _l.append(line[:-1-i])
                    added = True
                    break
            if not added:
                _l.append(line)
        else: _l.append(line)
f = open("./sources/" + argv[1] + ".txt", "w")
f.write("\n".join(_l))
f.close()