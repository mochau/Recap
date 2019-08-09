flag = 0
text = ''
with open("C:/Users/t-micha/Desktop/test_2.vtt", 'r') as f:
    for line in f:
        flag = flag + 1
        if "NOTE Confidence" in line:
            flag = 0
        if flag == 3:
            print(line)
            line = line.replace('\n', ' ')
            text = text + line
#        if flag == 5:
#            print(line)
#            line = line.replace('\n', ' ')
#            text = text + line
print(text)

from aylienapiclient import textapi
client = textapi.Client("bc2a2b88", "5bdd0298de5f05b4275e5309a7ed892c")
summary = client.Summarize({'text': text, 'title': 'west US calamity'})
print (summary)
print (summary.get('sentences'))

#made with love from Microsoft
