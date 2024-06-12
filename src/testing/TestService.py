import os

import pandas as pd

from src.MathcingVacanciesService import matchingVacanciesService


class TestService:

    def test_en(self):
        self.test('resumes-vacancies-en.xlsx')

    def test_ru(self):
        self.test('resumes-vacancies-ru.xlsx')

    def test(self, filename):
        resumes = self.read_excel_sheet(filename, 'resumes')
        resumes['ext_id'] = resumes['description'].map(self.add_resume)
        print(resumes)
        vacancies = self.read_excel_sheet(filename, 'vacancies')
        vacancies['resumes'] = vacancies['resumes'].apply(lambda x: x.split(','))
        vacancies['resumes'] = vacancies['resumes'].apply(lambda x: [int(y) for y in x])
        vacancies['ext-resumes'] = vacancies.resumes.apply(lambda x: self.map_resume_ids_to_ext_ids(resumes, x))
        print(vacancies)
        for count in range(3, 13):
            vacancies['ids-{}'.format(count)] = vacancies['job_description'].map(self.find_matching_func(count))
            vacancies['acc-{}'.format(count)] = vacancies.apply(lambda row: self.accuracy(row, count), axis=1)
        print(vacancies)

    def map_resume_ids_to_ext_ids(self, resumes, resume_ids):
        tgt_rows = resumes.loc[resumes['id'].isin(resume_ids)]
        uuids = tgt_rows['ext_id'].values
        return [str(x) for x in uuids]

    def accuracy_func(self, count):
        return lambda df: self.accuracy(df, count)

    def accuracy(self, vacancies, count):
        matching_count = len(intersection(vacancies['ids-{}'.format(count)], vacancies['ext-resumes']))
        total_count = len(vacancies['ext-resumes'])
        total = min(count, total_count)
        return matching_count / total * 100

    def add_resume(self, resume_description):
        return matchingVacanciesService.add_candidate(resume_description)

    def find_matching_func(self, count):
        return lambda x: matchingVacanciesService.find_matching_for_resume(x, count)

    def read_excel_sheet(self, file, sheet):
        return pd.read_excel(os.path.join(os.path.dirname(__file__), file), sheet_name=sheet)



def intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


testService = TestService()
