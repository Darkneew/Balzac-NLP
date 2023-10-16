from sys import argv

s = ""
for i in range(2, len(argv)):
    f = open("./sources/" + argv[1] + "/" + argv[i] + ".txt", "r")
    c = f.read()
    f.close()
    s += c + "\n\n"
totf = open("./sources/" + argv[1] + ".txt", "w")
totf.write(s)
totf.close()