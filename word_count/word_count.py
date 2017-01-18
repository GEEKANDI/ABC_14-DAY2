def words(my_words):
    split_word = my_words.split() #elimination of whitespaces
    output_word_dict ={}
    special_word = set(split_word) #set to store special values
    for word in special_word:
        special = 0
        for y in split_word: #iterate throgh the unique elements and check it wit a word list
            if word  == y:
                special = special + 1
                if word.isdigit() == True:
                    word = int(word)
        output_word_dict[word] = special
    return output_word_dict