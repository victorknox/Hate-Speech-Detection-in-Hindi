import stanza
import csv
from inltk.inltk import tokenize

filename = "valid.csv"
  
# initializing the titles and rows list
fields = []
rows = []
  
# reading csv file
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
      
#     # extracting field names through first row
#     fields = next(csvreader)
  
#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
  
#     # get total number of rows
#     print("Total no. of rows: %d"%(csvreader.line_num))
  
# # printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
  
#  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     # for col in row:
#     #     print(col),
#     # print('\n')
#     print(row[1])

dataset = "" # didn't know thus was a thing lol

for row in rows:
    dataset+=row[1] #this???

# print(dataset)
hin_tok = tokenize(dataset,'hi')
# print(hin_tok)

# gotcha

verbs_content = []
nlp = stanza.Pipeline('hi',processors='tokenize,pos,lemma')
pos = open('hindi_pos.txt','w')
doc = nlp(dataset)
for sentence in doc.sentences:
     for word in sentence.words:
        #  print(word)
         # + "{:8s}".format(word.upos),file=pos)
         if word.upos == 'VERB':
             verbs_content.append(word.text)
# print(verbs_content)

# open themenouns.txt in read
themed_nouns = open('themenouns.txt','r')
themenouns = []
for line in themed_nouns:
    themenouns.append(line.rstrip('\n'))
# print(themenouns)