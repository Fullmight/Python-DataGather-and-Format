
with open("index.csv", encoding='utf-8') as f:
    content = f.readlines()

    #content = [content.rstrip('\n') for content in f]

    #print(content)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    for x in range(len(content)):
        internalIter = content[x]
        if x > 0:
            locWords = content[x].split(';')
            #print(locWords)
            if len(locWords) > 1:
                content[x+1] = locWords[1].strip('\n') + " " + content[x+1]
                #print(content[x+1])
                #print(locWords[0])
                content[x] = locWords[0]
            locWord2 = content[x].split(' ')
            content[x] = ''
            tmpIgnore1 = ''
            tmpIgnore2 = ''
            for z in range(len(locWord2)):
                #print(content[x])
                if ((z + 8) == len(locWord2)):
                    aAdder = z
                    if is_number(locWord2[z]):
                        content[x] = content[x] + locWord2[z] + locWord2[z+1]
                        tmpIgnore1 = locWord2[z+1]
                        aAdder += 2
                    elif is_number(locWord2[z+1]):
                        content[x] = content[x] + locWord2[z] + ' ' + locWord2[z+1]
                        tmpIgnore1 = locWord2[z+1]
                    else:
                        content[x] = content[x] + locWord2[z] + ' '
                    if is_number(locWord2[z+2]):
                        content[x] = content[x] + locWord2[z+2] + ' '
                        tmpIgnore2 = locWord2[z+2]
                        aAdder += 1
                    else:
                        content[x] = content[x] + ' '
                    z = aAdder
                else:
                    if locWord2[z] != tmpIgnore1 and locWord2[z] != tmpIgnore2:
                        if locWord2[z+1] != "%":
                            content[x] = content[x] + locWord2[z] + ' '
                        else:
                            content[x] = content[x] + locWord2[z]
                if (z + 3) == len(locWord2):
                    content[x] = content[x] + locWord2[(z+1)] + locWord2[z+2]
                    #print(content[x])
                    break
        print(content[x])


