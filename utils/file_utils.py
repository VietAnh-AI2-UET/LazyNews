import json

def save_to_txt(paragraph: str) -> None:
    '''
    Save the input paragraph into .txt file

    Args:
        paragraph (list[str]): A list of text
        
    Returns:
        None

    Notes:
        This function will create a .txt file contain the input paragraph
    '''

    with open('prgs.txt', 'w', encoding='utf-8') as f:
        f.write(paragraph)

def save_to_json(file_name: str, data: dict) -> None:
    '''
    Save the input dictionary to .json file

    Args:
        data (dict): Dictionary to be saved

    Returns:
        None
    '''

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)