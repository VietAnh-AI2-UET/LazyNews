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

def save_to_json(title: str, paragraph: str):
    '''
    Save the input paragraph corresponding to its title into .json file

    Args:
        title (str): The title of the paragraph
        paragraph (str): A paragraph

    Notes:
        This function will create a .json file
        contain the input paragraph with its title
    '''

    content = {
        title: paragraph
    }
    with open('prgs.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)