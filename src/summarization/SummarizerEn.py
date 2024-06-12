from transformers import pipeline


class SummarizerEn:
    def __init__(self):
        self.internalSummarizerModel = pipeline("summarization", model="Samir001/ResumeSummary-t5-Wang-Arora")


    def summarize(self, text):
        return self.internalSummarizerModel(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']


summarizerEn = SummarizerEn()
