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

def chunk_text(paragraph: str, chunk_size=50) -> list[str]:
    """
    Split a paragraph into smaller text chunks based on word count.

    The paragraph is tokenized into words using whitespace. Then, words are grouped
    sequentially into chunks of up to `chunk_size` words. The last chunk may contain
    fewer words if the total is not divisible by `chunk_size`.

    Args:
        paragraph (str): The input paragraph to be split.
        chunk_size (int, optional): Maximum number of words in each chunk. Defaults to 400.

    Returns:
        list[str]: A list of text chunks.
    """
    
    words = paragraph.split()
    chunks, current = [], []
    for word in words:
        current.append(word)
        if len(current) >= chunk_size:
            chunks.append(' '.join(current))
            current = []
    if current:
        chunks.append(' '.join(current))
    return chunks