from flask import Flask, request

from transformers import pipeline
from InstructorEmbedding import INSTRUCTOR

from Embedder import embedder
from Summarizer import summarizer
from src.MathcingVacanciesService import matchingVacanciesService

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/resumes', methods=['POST'])
def load_resume():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        tgt_description = request.json['description']

        return str(matchingVacanciesService.add_vacancy(tgt_description))
    else:
        return 'Content-Type not supported!'


@app.route('/resumes/matching', methods=['POST'])
def find_resumes_matching_vacancy():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        tgt_description = request.json['description']

        return matchingVacanciesService.find_matching_for_resume(tgt_description)
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
    app.run()
