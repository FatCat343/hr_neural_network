import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, MBartTokenizer, MBartForConditionalGeneration


class SummarizerRu:
    def __init__(self):
        self.model_name = "IlyaGusev/mbart_ru_sum_gazeta"
        self.tokenizer = MBartTokenizer.from_pretrained(self.model_name)
        self.model = MBartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize(self, text):
        input_ids = self.tokenizer(
            [text],
            truncation=True,
            return_tensors="pt",
        )["input_ids"]
        output_ids = self.model.generate(
            input_ids=input_ids,
            no_repeat_ngram_size=5
        )[0]
        return self.tokenizer.decode(output_ids, skip_special_tokens=True)


summarizerRu = SummarizerRu()

