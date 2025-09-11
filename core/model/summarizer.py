from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Tải model và tokenizer
def get_model() -> tuple:
    '''
    Get the summarization model and tokenizer for the model

    Return:
        model (AutoMOdelForSeq2SeqLM): Summarizaion model
        tokenizer (AutoTokenizer): Tokenizer corresponding to the model
    '''

    model_name = "VietAI/vit5-base-vietnews-summarization"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

def get_summarize(input_text: list[str], model: AutoModelForSeq2SeqLM, tokenizer: AutoTokenizer) -> list[str]:
    '''
    Generate a summarization for a list of input paragraphs

    Argument:
        input_text (list[str]): A list of paragraphs
        model (AutoModelForSeq2SeqLM): Pretrained summarization model
        tokenizer (AutoTokenizer): Tokenizer corresponding to the model
    Return:
        summary (list[str]): A list of summarized paragraphs
    Notes:
        model_input['input_ids']: The tokenized representation of input paragraphs,
                                  shape=[batch_size, max_seq_len]
        summary_id: The tokenized representation of summarized paragraphs,
                    shape=[batch_size, max_seq_len]
    '''

    model_input = tokenizer(input_text,
                            return_tensors='pt',
                            max_length=512,
                            padding=True,
                            truncation=True)
    
    summary_ids = model.generate(
        model_input['input_ids'],
        max_length=200,      # Độ dài tối đa của summary
        min_length=50,      # Độ dài tối thiểu
        length_penalty=1.0,
        num_beams=6,
        early_stopping=True
    )
    summary = [tokenizer.decode(ids, skip_special_tokens=True) for ids in summary_ids]
    return summary