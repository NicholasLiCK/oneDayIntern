import json

with open('ptt_dump_20210218_1141.json', 'r') as f:
    file = json.load(f)


# def searchStr(input_str, all_post):
    
    
#     return


to_output = []
for article in file['articles']:
    if 'Re' in article['article_title']:
        to_output.append(article)
    elif 'Re' in article['content']:
        to_output.append(article)
    elif 'Re' in article['']

print(to_output)
    
    