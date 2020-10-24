# your code here
for smth in "a"*10:
    str = input()
    form = ""
    lemma = ""
    if (str == "") == False:
        if (str[0] == "#") == False:
            number_tabs = 0
            index = 0
            for smth in "a"*len(str):
                current_char = str[index]
                if current_char == "\t":
                    number_tabs = number_tabs + 1
                elif number_tabs == 1:
                    form = form + current_char
                elif number_tabs == 2:
                    lemma = lemma + current_char
                index = index + 1   
            if (form == lemma) == False:
                begins = False
                if len(lemma) < len(form):
                    index = 0
                    count = 0
                    for smth in "a"*len(lemma):
                        if lemma[index] == form[index]:
                            count = count + 1
                        index = index + 1    
                    if count == len(lemma):
                        begins = True
                if (begins == False):        
                    print(form, lemma)
