from flask import Flask, request

from src.MathcingVacanciesService import matchingVacanciesService
from src.testing.TestService import testService

app = Flask(__name__)


@app.route('/resumes', methods=['POST'])
def load_resume():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        tgt_description = request.json['description']
        return str(matchingVacanciesService.add_candidate(tgt_description))
    else:
        return 'Content-Type not supported!'


@app.route('/resumes/matching', methods=['POST'])
def find_resumes_matching_vacancy():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        tgt_description = request.json['description']
        count = resolve_count(request)

        return matchingVacanciesService.find_matching_for_resume(tgt_description, count)
    else:
        return 'Content-Type not supported!'


def resolve_count(request):
    if 'count' in request.json.keys():
        return request.json['count']
    else:
        return 5


# testing
@app.route('/test-en', methods=['POST'])
def test_en():
    testService.test_en()


@app.route('/test-ru', methods=['POST'])
def test_ru():
    testService.test_ru()


if __name__ == '__main__':
    app.run()
