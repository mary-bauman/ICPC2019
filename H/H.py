lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
print(lines)

changes = 0

#check for /\
for line in lines[1:]:
    if "/\\" in line:
        print(line)
        i = 0
        while i < len(line)-1:
            if line[i] == "\\" and line[i+1] == "/":
                #// check
                if i < len(line)-2:
                    print(f"i = {i}")

                #\\ check
                    
                #/\

            i+=1


print(changes)