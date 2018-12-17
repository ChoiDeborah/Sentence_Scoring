from xml.etree.ElementTree import parse

#---------------------------------------------
def depth_weight(depth):
    return pow(1.2, depth)
#1.2^depth
#파트스코어 함수안에서만 호출한다
#---------------------------------------------
def part_score(part, depth): #파트는 청크로나뉨
    
    score = 0
    
    wordext = False;
    #파트안의 워드유무 변수
    
    #word in part
    for word in part.findall("word"):
        score += 1.2      #1.2 point per word
        wordext = True  #word exists
     # 워드 존재시 wordext true
    
    score -= 0.2 # Last word has 1 point
    #마지막 워드는 1점을 부여하므로 0.2를 뺀다.
    #마지막 워드에 1점을 부여하고 앞의 워드는 1.2 example ) a cup of/ water
    
    #chunk in part
    for chunk in part.findall("chunk"):
        score += chunk_score(chunk, depth) * (1.2 if wordext else 1) #0.2
        #만약 워드 존재시 청크스코어에 1.2를 곱한다

    return score * depth_weight(depth) * (1.2 if part.get("role") == "sbj" else 1) #long subject -> high difficulty

#파트가 주어일때 1.2를 곱함

    
#---------------------------------------------
def chunk_score(chunk, depth): 
    
    score = 0
    
    #part in chunk    
    for part in chunk.findall("part"):
        score += part_score(part, depth+1)
    # 청크는 파트로만 나뉘기 때문에 파트점수만 더해준다.

    pos = chunk.get("pos") #pos(part of speech) of chunk


    if  (pos == "nn"): score *= 1.4 #noun
    elif(pos == "aj"): score *= 1.2 #adjective
    elif(pos == "av"): score *= 1   #adverb
    
    return score
    
#---------------------------------------------    
def scoring(node): #score of sentence #
    score = 0
    
    for part in node.findall("part"):
        score += part_score(part, 1)
    
    return score
# 점수 확인
for i in range(1, 8):
    tree = parse(str(i)+".xml") #read a xml file
    root = tree.getroot()       #get the sentence
    print(i)
    print(scoring(root)/18)     #print the score of sentence  #1-5 사이로 출력되도록하기위해 나눔
