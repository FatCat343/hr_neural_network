# Прототип системы для автоматической оценки соответствия резюме соискателя требованиям вакансии

Система для автоматического отбора кандидатов, реализованная на основе метода машинного обучения для оценки 
соответствия резюме соискателя требованиям вакансии

## Установка

Для работы программы необходим Python версии 3.11+, менеджер пакетов pip. Так же необходимо установить библиотеки 
Flask, QDrant Client, Hugging Face Transformers и прочие, используя pip install.

## Конфигурация приложения

Конфигурация осуществляется с использованием `application.properties` файла. 

Для выбора языка работы приложения необходимо определить настройку `language`, указав значения 
`en` или `ru`.

В конфигурации также можно указать параметры векторной БД Qdrant. Указанные параметры настроены для работы с Qdrant, 
запущенной в docker-контейнере с использованием docker-compose файла из текущего проекта.

## Запуск приложения

1. Запустить векторную БД Qdrant. В проекте содержится `docker-compose.yml` файл, с помощью которого можно запустить
БД в Docker
2. Запустить систему посредством выполнения скрипта app.py.

## Список моделей

### На русском
- Суммаризация: https://huggingface.co/IlyaGusev/mbart_ru_sum_gazeta
- Векторизация: https://huggingface.co/cointegrated/rubert-tiny2

### На английском
- Суммаризация: https://huggingface.co/Samir001/ResumeSummary-t5-Wang-Arora
- Векторизация: https://huggingface.co/hkunlp/instructor-large

