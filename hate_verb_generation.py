SYNSET = []
with open('Synset.txt') as f:
    for line in f:
        x = line.split()
        x[3] = x[3].split(':')
        SYNSET.append(x)

NegativePolarityWords = []
for line in SUBJCLUE:
    totalscore = int(line[2]) - int(line[3])
    if(totalscore < 0):
        NegativePolarityWords.append(line)

def Getsynset(word):
    syn = []
    flag=0
    syn.append(word)
    for line in SYNSET:
        if(line[1]=="03"):
            for verb in line[3]:
                if(word == verb):
                    flag = 1
                    break
            if(flag):
                syn = line[3]
                break
    return syn
s = []
slist = ["लड़ना" , "मारना" , "लूटना" , "पीटना" , "कूटना" , "तोडना" , "भेदभाव" ]
hlex = []
for word in slist:
    s = Getsynset(word)
    for verb1 in s:
        if verb1 in verbs_content:
            hlex.append(verb1)