"""
CS5760 HW1 — Q2 Tokenization

"""

import re


text = ("John's new laptop is fast. However, it isn't cheap! "
        "Many students still buy it. They often wait for discounts.")

def naive_space_tokens(txt: str):
    return txt.split()

def manual_tokens(txt: str):
    txt = re.sub(r'([.,!?])', r' \1 ', txt)
    txt = re.sub(r'\s+', ' ', txt).strip()
    toks = txt.split()
    out = []
    for t in toks:
        if t.endswith("n't") and len(t) > 3:
            out.append(t[:-3]); out.append("n't"); continue
        for cl in ("'s", "'re", "'ve", "'d", "'ll"):
            if t.endswith(cl) and len(t) > len(cl):
                out.append(t[:-len(cl)]); out.append(cl); break
        else:
            out.append(t)
    return out

def try_tool_tokens(txt: str):
    try:
        import spacy
        nlp = spacy.load("en_core_web_sm")
        return [t.text for t in nlp(txt)]
    except Exception:
        try:
            import nltk
            from nltk.tokenize import word_tokenize
            try: nltk.data.find("tokenizers/punkt")
            except LookupError: nltk.download("punkt")
            return word_tokenize(txt)
        except Exception: return None

def diff_lists(a, b, la="A", lb="B"):
    print(f"\nDiff ({la} vs {lb}):")
    m = max(len(a), len(b))
    for i in range(m):
        av = a[i] if i < len(a) else "∅"
        bv = b[i] if i < len(b) else "∅"
        print(f"{i:>3}: {av:10} | {bv:10} {'<--' if av!=bv else ''}")

def main():
    print("Paragraph:\n", text, "\n")

    naive = naive_space_tokens(text)
    manual = manual_tokens(text)
    print("Naïve:", naive)
    print("\nManual:", manual)
    diff_lists(naive, manual, "Naïve", "Manual")

    tool = try_tool_tokens(text)
    if tool:
        print("\nTool:", tool)
        diff_lists(manual, tool, "Manual", "Tool")

    mwes = ["New York City", "kick the bucket", "high school"]
    print("\nMWEs:", mwes)

    print("\nReflection:")
    print("Hardest parts: clitics (isn't → is + n't), possessives (John's → John + 's), punctuation.")
    print("English is easier than agglutinative languages with complex morphology.")
    print("MWEs complicate tokenization since they act as single semantic units.")
    print("Tools like spaCy align well, but noisy text requires custom rules.")

if __name__ == "__main__":
    main()
