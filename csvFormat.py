import unicodecsv as csv
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
        content = content.replace('"', '')
    for x in range(len(content)):
        if x == 0:
            content[x] = content[x].replace('"', '')
            content[x+1] = content[x].replace('\n', '') + content[x+1]
            content[x] = ''
            print(content[x])
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
        locWords3 = content[x].split(' ')
        nameIter = 0;
        for iZ in range(len(locWords3)):
            nameIter += 1
            if(iZ > 0 and iZ < 5):
                if(is_number(locWords3[iZ])):
                    locWords3[iZ] = ';' + locWords3[iZ]
                    break
        for iX in range(len(locWords3)):
            if iX == 0:
                content[x] = locWords3[iX]
            elif (iX < nameIter):
                content[x] = content[x] + ' ' + locWords3[iX]
            else:
                content[x] = content[x] + ';' + locWords3[iX]
        print(content[x])

#append Data to a CSV file
with open('finalFormatted.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, encoding='utf-8')
    #dictW = csv.DictWriter(csv_file, encoding='utf-8')
    #dictW.writeheader([headers])
    for y in range(len(content)):
        writer.writerow([content[y]])
