import json

with open('ptt_dump_20210218_1132.json', 'r') as f:
    file = json.load(f)


def searchStr(input_str):
    to_output = []
    for article in file['articles']:
        if input_str in article['article_title']:
            to_output.append(article)
        elif input_str in article['content']:
            to_output.append(article)
        elif input_str in article['messages']:
            to_output.append(article)
            
    return to_output


if __name__ == '__main__':
    
    print('All_Articles')
    print('愛莉莎莎')
    print('天竺鼠車車')
    
    request = input("Enter one of above:")
    
    if request == 'All_Articles':
        ans = file
    else:
        ans = searchStr(request)
    
    print(ans)
    