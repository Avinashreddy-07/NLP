"""
CS5760 HW1 — Q1 Regex
"""

import re

# Inline sample text
test_text = """
Here are some ZIP codes: 12345, 90210-1234, 78701 5678, A12345 (invalid).
Some words: Hello world, don't worry, state-of-the-art solution, JavaScript.
Numbers: +123, -45.67, 1,234,567.89, 2.5e-10, 42, -3.14e+5.
Contact via email, e-mail, or e mail. Send to EMAIL@example.com.
Reactions: go, goo!, gooo?, goooooo.
Questions end here?
"Is this a question?”
What about this one?'
Not a question.
"""

def main():
    # 1) US ZIP codes
    zip_pattern = r'\b\d{5}(?:[-\s]\d{4})?\b'

    # 2) Words not starting with capital letter
    non_capital_pattern = r"\b(?![A-Z])[A-Za-z]+(?:[’'-][A-Za-z]+)*\b"

    # 3) Numbers with sign/commas/decimals/scientific notation
    number_pattern = r'[+-]?(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?'

    # 4) Email variants
    email_pattern = r'(?i)\be[-\s–]?mail\b'

    # 5) go+ with optional punctuation
    go_pattern = r'\bgo+(?:[!.,?])?(?=\s|$)'

    # 6) Lines ending with ?
    question_line_pattern = r'.*\?[\"”’\')\]\s]*$'

    print("1) ZIP codes:", re.findall(zip_pattern, test_text))
    print("\n2) Non-capital words:", re.findall(non_capital_pattern, test_text))
    print("\n3) Numbers:", re.findall(number_pattern, test_text))
    print("\n4) Email variants:", re.findall(email_pattern, test_text))
    print("\n5) go+ interjections:", re.findall(go_pattern, test_text, flags=re.IGNORECASE))
    print("\n6) Question lines:")
    for line in test_text.splitlines():
        if re.match(question_line_pattern, line.strip()):
            print(" ", line.strip())

if __name__ == "__main__":
    main()
