import requests
from bs4 import BeautifulSoup

import pprint

#미드 대본 수집
url = 'https://fangj.github.io/friends/season/0101.html'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

sentence_list = doc.select('p > font')
for i, sentence in enumerate(sentence_list):
    print('============================================')
    sentence_txt = sentence.get_text().strip()
    start_idx = sentence_txt.find(':')
    clean_sentence = sentence_txt[start_idx+2:]
    pprint.pprint('1 >> {}'.format(clean_sentence))


#단어만 추출(전처리)
#빈도수 순으로 나열 및 시각화
#다음 영어사전 단어정보 수집 및 매칭
#Excel로 저장
#Wordcloud로 시각화import requests
from bs4 import BeautifulSoup

import pprint

#미드 대본 수집
url = 'https://fangj.github.io/friends/season/0101.html'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

sentence_list = doc.select('p > font')
for i, sentence in enumerate(sentence_list):
    print('============================================')
    sentence_txt = sentence.get_text().strip()
    start_idx = sentence_txt.find(':')
    clean_sentence = sentence_txt[start_idx+2:]
    pprint.pprint('1 >> {}'.format(clean_sentence))


#단어만 추출(전처리)
#빈도수 순으로 나열 및 시각화
#다음 영어사전 단어정보 수집 및 매칭
#Excel로 저장
#Wordcloud로 시각화