def clean_text(paragraphs: list[str]) -> list[str]:
    '''
    Remove unnecessary elements in input list of paragraphs,
    keep only the main content of the website

    Args:
        paragraphs (list[str]): A list of text
    
    Returns:
        clean_paragraphs (list[str]): A cleaned version of input paragraphs,
                                      removed paragraphs that contain text in noise_keywords
    '''

    noise_keywords = ["xem thêm", "ảnh:", "tác giả", "nguồn:", "copyright"]

    clean_paragraphs = []
    min_len = 30    # minimum length of each paragraph
    for p in paragraphs:
        if len(p) >= min_len and not any(kw in p.lower() for kw in noise_keywords):
            clean_paragraphs.append(p)
    return clean_paragraphs

#todo: implement chunking methode