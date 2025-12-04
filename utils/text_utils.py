def is_clean_text(paragraph: str) -> bool:
    '''
    Checking validation of input paragraph,
    return False if any word is in noise_keyword

    Args:
        paragraph (str): A paragraph of text
    
    Returns:
        bool: True if input paragraph is valid. Otherwise, False
    '''

    noise_keywords = ["xem thêm", "ảnh:", "tác giả", "nguồn:", "copyright"]

    min_len = 30    # minimum length of each paragraph
    if len(paragraph) >= min_len and not any(kw in paragraph.lower() for kw in noise_keywords):
            return True
    return False

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