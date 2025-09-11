from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Summarizer:
    def __init__(self):
        '''
        Initiate summarization model and tokenizer
        '''

        model_name = "VietAI/vit5-base-vietnews-summarization"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def get_summarize(self, input_text: list[str]) -> list[str]:
        '''
        Generate a summarization for a list of input paragraphs

        Arguments:
            input_text (list[str]): A list of paragraphs
        Return:
            summary (list[str]): A list of summarized paragraphs
        Notes:
            model_input['input_ids']: The tokenized representation of input paragraphs,
                                    shape=[batch_size, max_seq_len]
            summary_id: The tokenized representation of summarized paragraphs,
                        shape=[batch_size, max_seq_len]
        '''

        model_input = self.tokenizer(input_text,
                                return_tensors='pt',
                                max_length=512,
                                padding=True,
                                truncation=True)
        
        summary_ids = self.model.generate(
            model_input['input_ids'],
            max_length=200,      # Độ dài tối đa của summary
            min_length=50,      # Độ dài tối thiểu
            length_penalty=1.0,
            num_beams=6,
            early_stopping=True
        )
        summary = [self.tokenizer.decode(ids, skip_special_tokens=True) for ids in summary_ids]
        return summary

# todo: implement chunking methode for class Summarizer
# def get_chunking_prgs(text: str) -> list[str]: