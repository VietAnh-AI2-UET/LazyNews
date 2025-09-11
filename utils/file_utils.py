def save_to_txt(paragraphs: list[str]):
    '''
    Save the input list of paragraphs into .txt file

    Arguments:
        paragraphs (list[str]): A list of text
    Return:
        .txt file concatenated all text in paragraphs with seperator
    '''

    seperator = '\n'
    with open('prgs.txt', 'w', encoding='utf-8') as f:
        for paragraph in paragraphs:
            f.write(paragraph + seperator)

#todo: implement save to json