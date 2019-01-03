import xml.etree.ElementTree as ET


def part_search(part, depth, posNN):


    role = part.get("role")
    haveToSearch = False

    if posNN:
        if role == "trg":
            haveToSearch = True



    wordText = False
    chunkText = False


    wordPosType = 0
    sentenceType = 0

    for word in part.findall("word"):
        wordText = True
        wordPos = word.get("pos")

        if wordPos =='nn':
            wordPosType = 1

        if haveToSearch:
            temp = word.text
            if temp == ' to ':
                sentenceType = 1



    for chunk in part.findall("chunk"):
        chunkText = True
        if wordText:
            wordText = False
            if wordPosType == 1:
                wordPosType = 0;
                chunk_search(chunk, depth, wordPosType)

        chunkPos = chunk.get("pos")


    return sentenceType


# ---------------------------------------------
def searching(node):

    result = False

    for part in node.findall("part"):
        role = part.get("role")
        result = part_search(part, 1, 0)

    return result


# ---------------------------------------------
def chunk_search(chunk, depth, SentenceType):

    for part in chunk.findall("part"):
        part_search(part, depth+1, SentenceType)



path = "/Users/deborah/Desktop/dJangoXMLParser/example/Example_Sentences_181216.xml"
global count
global totalCount
totalCount = 0


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
            string = ""
            count += 1
            if searching(root):
                print(root)

            isline = False

    f.close()
    return count


for i in range(1, 13):
    print(i)
    totalCount += Load_XML("/Users/deborah/Desktop/Sentence_Scoring/xml/" + str(i) + ".xml")

    print(totalCount)

#totalCount += Load_XML("/Users/deborah/Desktop/Sentence_Scoring/sentences/1.xml")