# -*- coding: utf-8 -*- 
import xml.etree.ElementTree as ET

def Load_XML(pathName):
    count = 0
    
    f = open(pathName, 'r')                 # 읽는 모드로 파일을 열고
    string = ""                             # isline, string 초기화
    isline = False
   

    while True:
        line = f.readline()                 # 파일에서 한 라인을 읽어 라인에 저장
        
        if not line and not isline:         # 만약 라인이 NULL 값이면서 이전 라인 존재시 브래이크
            break

        if isLine(line):                    # 라인이 줄바꿈, 주석, 공백에 해당하지 않으면
            string += line                  # string에 라인을 더해주고
            isline = True                   # 라인상태 변수는 참
           
        else:                               # 줄바꿈, 주석, 공백에 해당하면 
            if isline:                      # 만약 라인이냐가 트루일 때 만
                isline = False              # 라인상태변수는 거짓이 된다
                                       
        if not isline and not string == "": # XML 파싱이 끝난지점인지 체크                                                 
            count = parse_String_To_XML(string, count)
            isline = False                  
            string = ""
            
    f.close()

    return count

# ----------------------------------------

def parse_String_To_XML(string , count):    # string -> XML
    
    root = ET.fromstring(string)            # string을 root에 넣고 파싱한다
    count += 1                              # 문장 수 + 1 
    if searching(root, "BE-110"):
        print(string)
    else :
        print("False\n")    
    return count

# ----------------------------------------

def isLine(line):                           # 줄바꿈 주석 공백 인지 체크 하는 함수
    if not line == '\n' and not line[:4] == '<!--' and not line == '':
        return True
    else:
        return False    

# ----------------------------------------

def searching(node , type):
    result = False

    role = ""
    pos = ""

    if type == "BE-110":
        for part in node.findall("part"):
    
            if not result :                                 #result 가 False 일 때
                role = "prd"
                pos = "be" 
                result = part_search(part, role, pos, 1)
              
            else:                                           #result가 True 가 되면 
                result = False
                role = "cpm"
                pos = "nn"
                result = part_search(part, role, pos, 1)
                if result:
                    return True
                    

    #elif type == "BE-120":
    #    for part in node.findall("part"):
    #        result = part_search(part, "cpm","nn", 1)

    #elif type == "VB-100":
    #   for part in node.findall("part"):
    #        result = part_search(part, "prd", "vb", 1)
                

    #for part in node.findall("part"):
    #    result = part_search(part,1)

    return False

# ----------------------------------------

def part_search(part, role_keyword, pos_keyword, depth):
    result = False

    role = part.get("role")
    #if 파트의 롤과 매개변수로 받은 롤을 비교
    if(role == role_keyword):
        for word in part.findall("word"):
            pos = word.get("pos")
            if pos == pos_keyword:
                return True
        # 같으면 word의 pos 비교


    #for word in part.findall("word"):
    
    #for chunk in part.findall("chunk"):


    return result
# ----------------------------------------

def chunk_search(chunk, role_keyword, pos_keyword, depth):
    result = False

    for part in chunk.findall("part"):
        result = part_search(part, role_keyword, pos_keyword, depth+1)

    return result

# ----------------------------------------

sum = 0

for i in range(1, 13):                      # 1 - 12 까지의 XML 불러오기
    count = 0
    sum += Load_XML("/Users/deborah/Desktop/Sentence_Scoring/xml/" + str(i) + ".xml")   #Load_XML에 file Path를 인자로 전달 호출

print(sum)