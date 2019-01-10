import xml.etree.ElementTree as ET


def part_search(part, depth, tempRole):

    wordText    = False
    chunkText   = False

    isWordPos = False
    isChunkPos = False

    role = part.get("role")


    wordPosType = 0
    sentenceType = 0

    if (tempRole == 'sbj'):
        for word in part.findall("word"):
            wordText = True
            wordPos = word.get("pos")
            if (wordPos == 'nn'):
                isWordPos = True
                break

        for chunk in part.findall("chunk"):

            chunkText = True

            chunkPos = chunk.get("pos")
            if (chunkPos == 'aj'):
                isChunkPos = True
                if chunk_search(chunk, depth, "trg"):
                    return True

    if(tempRole == 'trg'):
        for word in part.findall("word"):
            wordPos = word.get("pos")
            if (wordPos == 'pp'):
                return True





    return sentenceType


# ---------------------------------------------
def searching(node, type):

    result = False
    role = ''

    if type == 0:
        role = 'sbj'

    for part in node.findall("part"):
        if(result):return True
        result = part_search(part, 1, role)

    return result


# ---------------------------------------------
def chunk_search(chunk, depth, role):
    result = 0

    for part in chunk.findall("part"):
        if(result):
            return True
        tempRole = part.get("role")
        if(tempRole == role ):
            result = part_search(part, depth+1, role)

    return result

# ---------------------------------------------

path = "/Users/deborah/Desktop/dJangoXMLParser/example/Example_Sentences_181216.xml"
global count
global totalCount
totalCount = 0

TypeOfSentence = 0

def Load_XML(pathName):
    f = open(pathName, 'r')
    string = ""
    isline = False

    count = 0

    while True:
        line = f.readline()
        if not line:
            if not isline:
                break

        if not line == '\n' and not line[:4] == '<!--' and not line == '':
            string += line
            isline = True
        else:
            if isline:
                isline = False

        if not isline and not string == "":
            root = ET.fromstring(string)
            print(count + 1)
            count += 1

            if searching(root, 0):
                #printXMLString(root)
                print(string)

            else:
                print("FALSE")

            isline = False
            string = ""
    f.close()
    return count


for i in range(1, 13):
    print(i)
    totalCount += Load_XML("/Users/deborah/Desktop/Sentence_Scoring/xml/" + str(i) + ".xml")

    print(totalCount)

#totalCount += Load_XML("/Users/deborah/Desktop/Sentence_Scoring/sentences/1.xml")


def printXMLString(root):
    reslist = list(root.iter())
    result = ' '.join([element.text for element in reslist])
    print(result)