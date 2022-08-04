sentence_one = "My name is Suyash Purwar!"

print(len(sentence_one))
print(sentence_one[1].capitalize())
print("The index of first 'a' is " + str(sentence_one.find('Suyash')))

def find_index_of_all(string, word):
    word_count = string.count(word)
    index_list = []
    for x in range(0, word_count):
        index = string.find(word)
        index_list.append(index)
        string = string[index+1:len(string)]
    return index_list

index_list = find_index_of_all(sentence_one, 'a')
print(index_list)

uni_name = 'LovelyProgessionalUniversity' # Spaces are not allowed
print(uni_name.isalpha())  # sentence_one is aplhabetical. hence, true

registration_no = '12100435'
print(registration_no.isdigit())

sen_one = "I am damn sleepy"
print(sen_one.replace(" ", "-").upper())

my_name = "Suyash"
print(my_name + my_name[-1]*5)