def save_to_txt(paragraph: str):
    '''
    Save the paragraph into .txt file

    Arguments:
        paragraph (list[str]): A list of text
    Return:
        .txt file contain the input paragraph
    '''

    with open('prgs.txt', 'w', encoding='utf-8') as f:
        f.write(paragraph)

#todo: implement save to json