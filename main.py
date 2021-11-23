import pprint
import nltk
import requests
from bs4 import BeautifulSoup

#nltk.download('punkt')
#nltk.download('stopwords')

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

words = [] #영단어장
for i, sentence in enumerate(sentence_list):
    print('============================================')
    sentence_txt = sentence.get_text().strip()
    start_idx = sentence_txt.find(':')
    clean_sentence = sentence_txt[start_idx+2:]
    pprint.pprint('1 >> {}'.format(clean_sentence))


    #단어만 추출(전처리)
    #conda install -c anaconda nltk
    #자연어 처리 -> NLTK
    #1.토큰화
    token_list = nltk.word_tokenize(clean_sentence)
    print('2 >> {}'.format(token_list))

    #2.불용어(stopword) 거르기
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append(',') #불용어 추가
    stopwords.append('?')
    stopwords.append('.')
    stopwords.append('..')
    stopwords.append('...')
    stopwords.append('.....')
    stopwords.append('!')
    stopwords.append('``')
    stopwords.append('--')

    clean_list = []
    for token in token_list:
        if token not in stopwords:
            clean_list.append(token)
    print('3 >>> {}'.format(clean_list))

    #3. 1개짜리 토큰 제거
    #len_filer_list = []
    #for token in clean_list:
    #    if len(token) > 1:
    #        len_filer_list.append(token)

    #lambda식 활용
    len_filer_list = list(filter(lambda x: len(x) > 1, clean_list))
    print('4 >>>> {}'.format(len_filer_list))

    #4. ' 포함된 토큰 제거
    clean_filter_list = list(filter(lambda x: "'" not in x, len_filer_list))
    print('5 >>>>> {}'.format(clean_filter_list))
    words.extend(clean_filter_list) #모든 list 총합해서 하나로
    #cf. append= 모든 list 나열만 함

    #5. '-' 포함 토큰 제거
    clean_list = list(filter(lambda x: "-" not in x, clean_filter_list))
    print('6 >>>>>> {}'.format(clean_list))
    words.extend(clean_list)

print(words)

#빈도수 순으로 나열 및 시각화
#다음 영어사전 단어정보 수집 및 매칭
#Excel로 저장
#Wordcloud로 시각화