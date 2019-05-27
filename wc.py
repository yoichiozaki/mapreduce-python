from mapreduce import MapReduce
import sys

class WordCount(MapReduce):
    def __init__(self, input_dir, output_dir, n_mappers, n_reducers):
        MapReduce.__init__(self, input_dir, output_dir, n_mappers, n_reducers)

    def mapper(self, key, value):
        results = []
        defautl_count = 1
        for word in value.split():
            if self.is_valid_word(word):
                results.append((word.lower(), defautl_count))
        return results

    def is_valid_word(self, word):
        return all(64 < ord(character) < 128 for character in word)

    def reducer(self, key, values):
        wordcount = sum(value for value in values)
        return key, wordcount

if __name__ == '__main__':
    if (len(sys.argv) != 5):
        print("Please provide the following arguments: input directory, output directory")
        print("Default arguments used: 'input_dir' 'output_dir' 4 4")
        import settings
        input_dir, output_dir, n_mappers, n_reducers \
            = settings.default_input_dir, settings.default_output_dir, settings.default_n_mappers, settings.default_n_reducers
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        n_mappers = int(sys.argv[3])
        n_reducers = int(sys.argv[4])
    word_count = WordCount(input_dir, output_dir, n_mappers, n_reducers)
    word_count.run()
    result = (word for word in word_count.join_outputs())
    print("-- Results of wordcount with parameters:", input_dir, output_dir, n_mappers, n_reducers)
    results_to_show = 50
    print("-- Showing ", results_to_show, " words:")
    for i in range(results_to_show):
        try:
            word, count = result.next()
            print(word, count)
        except Exception:
            pass