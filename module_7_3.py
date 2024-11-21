class WordsFinder():
    file_names = []

    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)

    def get_words(self, strIn):
        words = []
        word = ''
        azbook = list("абвгдежзийклмнопрстуфхцчшщьыЪэюя-")
        alfabet = list("'abcdefghijklmnopqrstuvwxyz")
        i = 0
        while i < len(strIn):
            while strIn[i] in azbook:
                word = word + strIn[i]
                i += 1
            while strIn[i] in alfabet:
                word = word + strIn[i]
                i += 1
            if not word in ['', '-']:
                words.append(word)
                word = ''
            i += 1
        return words

    def get_all_words(self):
        words_dict = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                string = file.read().lower()
                words_dict[i] = self.get_words(string)
        return words_dict

    def find(self, word):
        words_dict = {}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            for i in range(0, len(v)):
                if word.lower() == v[i]:
                    words_dict[k] = i + 1
                    return words_dict

    def count(self, word):
        all_words = self.get_all_words()
        count = 0
        for k, v in all_words.items():
            for i in range(0, len(v)):
                if word.lower() == v[i]: count += 1
        return {k: count}




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
