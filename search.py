
def rank(phrase, items):
    ranks = []
    for item in items:
        rank = 0
        if phrase in item:
            rank = 1
        else:
            phr = phrase
            for index in range(1, len(phr)):
                phr = phr[:-index]
                
                if phr in item:
                    rank = 1 + index
                    break

                phr = phrase
                
        ranks.append(rank)
    return [items, ranks]

def list(phrase, items):
    ranked = rank(phrase, items)
    entrys = ranked[0]
    ranks = ranked[1]
    final_list = []
    for index in range(len(phrase) + 1):
        if index == 0:
            continue
        
        ind = 0
        for ranking in ranks:
            if ranking == index:
                final_list.append(entrys[ind])
            ind += 1
    i = 0
    for ranking in ranks:
        if ranking == 0:
            final_list.append(entrys[i])
        i += 1
    return final_list
        

        
'''test_list = ["word", "something else", "what dis?", "another word", "hello"]
test_phrase = "word"
print(rank(test_phrase, test_list))
print(list(test_phrase, test_list))'''
