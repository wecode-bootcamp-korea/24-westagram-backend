
import random

SEED = 1

def shuffler(lst_pw):
    seed = SEED
    random.seed(seed)
    idx_pw = list(range(len(lst_pw)))
    random.shuffle(idx_pw)
    random.seed()
    return idx_pw

def encoder(raw_pw):
    lst_pw = list(raw_pw)
    idx_pw = shuffler(lst_pw)

    lst_pw[:] = [lst_pw[i] for i in idx_pw]
    tot = ''.join(lst_pw)
    return tot

def decoder(encoded_pw):
    lst_pw = list(encoded_pw)
    idx_pw = shuffler(lst_pw)

    res = [None] * len(lst_pw)
    for i, j in enumerate(idx_pw):
        res[j] = lst_pw[i]
    lst_pw[:] = res
    tot = ''.join(lst_pw)
    return tot
    