#!/usr/bin/env python3

import glob
import json
import chardet


def get_most_used_words(text, top=10, length=6):
    all_words = list(filter(lambda x: len(x) >= length, text.split()))
    used_words = [(i, all_words.count(i)) for i in set(all_words)]
    used_words.sort(key=lambda x: x[1], reverse=True)
    return used_words[:top]


def get_encoding(data):
    return chardet.detect(data)['encoding']


for filename in glob.glob('data/*.json'):
    with open(filename, 'rb') as f:
        data = f.read()
        rss_feed = json.loads(data.decode(get_encoding(data)))
        news = []
        for item in rss_feed['rss']['channel']['items']:
            news.append(item['description'])
        most_used_words = get_most_used_words(' '.join(news))
        print('Имя файла - {}'.format(filename))
        print('10 наиболее часто встречающихся слов:')
        for item in most_used_words:
            print('{} – {} раз'.format(item[0], item[1]))
        print('---')
