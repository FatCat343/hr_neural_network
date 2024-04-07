from transformers import pipeline


class Summarizer:
    def __init__(self):
        self.internalSummarizerModel = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize(self, text):
        return self.internalSummarizerModel(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']


summarizer = Summarizer()
