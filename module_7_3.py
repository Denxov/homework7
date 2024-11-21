class WordsFinder():

    def __init__(self, *files):
        self.file_names=[]
        for i in files:
            self.file_names.append(i)

    def get_words(self, strIn):
        words = []
        word = ''
        azbook = list("абвгдежзийклмнопрстуфхцчшщьыЪэюя-")
        alfabet = list("'abcdefghijklmnopqrstuvwxyz")
        i = 0
        while i < len(strIn):
            if strIn[i] in azbook:
                word = word + strIn[i]
            elif strIn[i] in alfabet:
                word = word + strIn[i]
            else:
                if not word in ["", "-","'"]:
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
                    break
        return words_dict

    def count(self, word):
        words_dict = {}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            count=0
            for i in range(0, len(v)):
                if word.lower() == v[i]: count += 1
            if count>0:words_dict[k]=count
        return words_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

