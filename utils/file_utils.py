import json

def save_to_txt(paragraph: str):
    '''
    Save the input paragraph into .txt file

    Args:
        paragraph (list[str]): A list of text
        
    Notes:
        This function will create a .txt file contain the input paragraph
    '''

    with open('prgs.txt', 'w', encoding='utf-8') as f:
        f.write(paragraph)

def save_to_json(data: dict):
    '''
    Save the input dictionary to .json file

    Args:
        data (dict): Dictionary to be saved
    '''

    with open('today_news.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)