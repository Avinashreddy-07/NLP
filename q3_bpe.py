"""
CS5760 HW1 — Q3 BPE
"""

from collections import Counter

CORPUS = (
    "low low low low low lowest lowest "
    "newer newer newer newer newer newer "
    "wider wider wider new new"
).split()

def add_eow(words): return [w + "_" for w in words]
def to_symbols(w): return list(w + "_")
def sequences(words): return [list(w + "_") for w in words]
def pair_counts(seqs):
    c = Counter()
    for seq in seqs:
        for i in range(len(seq)-1):
            c[(seq[i], seq[i+1])] += 1
    return c
def merge(seqs, pair):
    a,b = pair; out=[]
    for seq in seqs:
        i=0; new=[]
        while i < len(seq):
            if i < len(seq)-1 and seq[i]==a and seq[i+1]==b:
                new.append(a+b); i+=2
            else: new.append(seq[i]); i+=1
        out.append(new)
    return out
def vocab(seqs): return {s for seq in seqs for s in seq}

def learn_bpe(words, steps=12):
    seqs = sequences(words)
    merges=[]
    for step in range(steps):
        counts = pair_counts(seqs)
        if not counts: break
        (a,b),f = counts.most_common(1)[0]
        merges.append((a,b))
        seqs = merge(seqs,(a,b))
        print(f"[Step {step+1}] merge {(a,b)} freq={f} | vocab={len(vocab(seqs))}")
    return merges

def apply_bpe(word, merges):
    seq = to_symbols(word)
    for (a,b) in merges:
        i=0; new=[]
        while i < len(seq):
            if i < len(seq)-1 and seq[i]==a and seq[i+1]==b:
                new.append(a+b); i+=2
            else: new.append(seq[i]); i+=1
        seq=new
    return seq

def main():
    merges = learn_bpe(CORPUS, steps=12)
    tests = ["new","newer","lowest","widest","newestest"]
    print("\nSegmentations:")
    for w in tests:
        print(w,"->",apply_bpe(w,merges))
    print("\nReflection:")
    print("BPE composes unseen words from known subwords (e.g., newestest).")
    print("Frequent merges like 'low','new','er','est' align with morphemes.")
    print("Pros: smaller vocab, handles OOV. Cons: splits can ignore meaning.")

if __name__=="__main__":
    main()
