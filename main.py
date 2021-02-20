import json

with open('ptt_dump_20210218_1141.json', 'r') as f:
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
    
    print('Articles')
    print('Alisasa')
    print('PUIPUI')
    
    request = input("Enter one of above:")
    
    ans = searchStr(request)
    
    print(ans)
    