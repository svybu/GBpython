seq = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, word in  enumerate(seq):
    if word[1:].isdigit() or word.isdigit():
        if int(word) < 10:
            if len(word) == 2:
                word = word[0] + "0" + word[1:]
            else :
                word = "0" + word
        seq[i] = '"' + word + '"'
print(' '.join(seq))

