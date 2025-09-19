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

def chunk_text(paragraph: str) -> list[str]:
    """
    Split a paragraph into smaller chunks based on word count.

    - If the paragraph has fewer than 400 words, it is divided into 3 equal chunks.  
    - If the paragraph has 400 words or more, it is split into chunks of ~200 words.  

    Args:
        paragraph (str): The input paragraph as a string.

    Returns:
        list[str]: A list of text chunks
    """

# todo: upgrade chunking methode
# <400 words: split into 3 chunks
# >=400 words: 200 words per chunks
    
    words = paragraph.split()

    if (len(words) < 400):
        chunk_size = len(words) // 3
    else:
        chunk_size = 200

    chunks, current = [], []
    for word in words:
            current.append(word)
            if len(current) >= chunk_size:
                chunks.append(' '.join(current))
                current = []

    if current:
        if len(current) >= 30:
            chunks.append(' '.join(current))
    return chunks