# your code here
yes = 0
no = 0
front_vow = "eiöü"
back_vow = "aıou"
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
                if (begins == True):
                    harmony = True
                    is_front_vow = False
                    is_back_vow = False
                    for char in form:
                        if char in front_vow:
                            is_front_vow = True
                        elif char in back_vow:
                            is_back_vow = True
                    if is_back_vow == True:
                        if is_front_vow == True:
                            harmony = False
                    if harmony == True:
                        yes = yes + 1
                    else:
                        no = no + 1
print(yes, no)
