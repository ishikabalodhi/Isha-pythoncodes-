#global and local variables
num_1=100
def func_1():
    num_1=40
    print(num_1)

def func_2():
        print(num_1)
func_1()
func_2()

# write a python program that takes sentence as input and return a dictionary with the count of each word.
# calculate the frequency of each word in a sentence.

def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    sentence = input("Enter a sentence: ")
    word_count_dict = count_words(sentence)
    print("Word count dictionary:", word_count_dict)

if _name_ == "_main_":
    main()
