def reverse_string(word):
    if len(word) == 0 :
        return 

    last_char = word[len(word)-1]
    print(last_char, end='')
    return reverse_string(word[0:len(word)-1])
  

reverse_string('hello')
print()
