# -*- coding: utf-8 -*-
# @Time : 2020/7/1 14:23
# @Author : Mamamooo
# @Site :
# @File : odd5_lru.py
# @Software: PyCharm
"""

"""

import pylru
import re

class LRUCache(object):
    def __init__(self,size=32):
        self.cache = pylru.lrucache(size)

    def has(self,key):
        return key in self.cache

    def get(self,key):
        return self.cache[key]

    def set(self,key,value):
        self.cache[key] = value


class SearchEngineBase(object):
    def __init__(self):
        print("SearchEngineBase")
        pass
    def add_corpus(self,file_path):
        with open(file_path,'r') as fin:
            text = fin.read()
            print(text)
        self.process_corpus(file_path,text)

    def process_corpus(self,id,text):
        raise Exception('process_corpus not implemented.')

    def search(self,query):
        raise Exception('search not implemented.')


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine,self).__init__()
        self.inverted_index = {}
    def process_corpus(self,id,text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self,query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()

        for query_word in query_words:
            query_words_index.append(0)

        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        result = []
        while True:
            current_ids = []
            for idx,query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w]',' ',text)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None,word_list)
        return set(word_list)


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine,LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache,self).__init__()
        LRUCache.__init__(self)

    def search(self,query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)

        result = super(BOWInvertedIndexEngineWithCache,self).search(query)

        self.set(query,result)
        return result


def main(search_engine):
    for file_path in ['1.txt','2.txt','3.txt','4.txt','5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

search_engine = BOWInvertedIndexEngineWithCache()
main(search_engine)
