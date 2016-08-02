#coding:UTF-8
from __future__   import division
import itertools

trans = {'A':'1',
         'T':'10',
         'J':'11',
         'Q':'12',
         'K':'13'}

ops = list(itertools.permutations(['+','-','*','/'], r=3))

feature = {}

def gen_feature_table(seq_pai):
    new_seq_pai = map(lambda x: trans.get(x, x), seq_pai)

    for op in ops:
        expt = '%s'.join(new_seq_pai) % op
        if eval(expt) == 24:
            #print expt
            f = sorted(new_seq_pai,reverse=True)
            feature[''.join(i.zfill(2) for i in f)] = expt
            print  ''.join(i.zfill(2) for i in f), expt

def calc24(seq_pai):
    new_seq_pai = map(lambda x: trans.get(x, x), seq_pai)

    for op in ops:
        expt = '%s'.join(new_seq_pai) % op
        if eval(expt) == 24:
            return expt

    return None

def calc24_feature_tabke(seq_pai):
     new_seq_pai = sorted(map(lambda x: trans.get(x, x), seq_pai), reverse=True)
     return feature.get(''.join(i.zfill(2) for i in new_seq_pai), None)

if __name__ == "__main__":
    seq = "A23456789TJQK"
    allseq = seq*4

    for i in seq:
        for j in seq:
            for p in seq:
                for q in seq:
                    gen_feature_table(i+j+p+q)


    import time
    b = time.clock()
    print calc24('1111')
    print time.clock() - b

    import time
    b = time.clock()
    print calc24_feature_tabke('1111')
    print time.clock() - b