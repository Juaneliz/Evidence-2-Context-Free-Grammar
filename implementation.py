import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det Nom NP2
    NP2 -> Conj NP NP2 | EPS
    Nom -> Adj Nom | N
    VP -> V VP2 | V PP VP2 | V NP VP2 | V NP PP VP2
    VP2 -> Conj VP VP2 | EPS
    PP -> Prep NP
    EPS ->
    Det -> 'der' | 'die' | 'das' | 'ein' | 'eine' | 'dem'
    Adj -> 'fleißige' | 'kleine' | 'schwere' | 'neue' | 'intelligent' | 'interessant' | 'alt'
    N -> 'Schüler' | 'Lehrerin' | 'Buch' | 'Klasse' | 'Klassenzimmer' | 'Rucksack' | 'Kurs'
    V -> 'liest' | 'schreibt' | 'ist' | 'erklärt' | 'macht'
    Prep -> 'in' | 'mit' | 'auf'
    Conj -> 'und' | 'oder'
""")

parser = ChartParser(grammar)

# Test function
def test_sentence(sentence, should_accept):
    tokens = sentence.split()
    trees = list(parser.parse(tokens))
    accepted = len(trees) > 0
    result = "PASS" if accepted == should_accept else "FAIL"
    print(f"[{result}] '{sentence}' -> {'Accepted' if accepted else 'Rejected'}")
    if accepted and trees:
        trees[0].pretty_print()

# Sentences that SHOULD be accepted
print("=== VALID SENTENCES ===")
test_sentence("der Schüler schreibt", True)
test_sentence("die Lehrerin erklärt das Buch", True)
test_sentence("der fleißige Schüler liest", True)
test_sentence("der Schüler schreibt und macht und erklärt", True)
test_sentence("die Lehrerin ist in dem Klassenzimmer", True)
test_sentence("der Schüler schreibt in das Klassenzimmer", True)

# Sentences that SHOULD be rejected  
print("\n=== INVALID SENTENCES ===")
test_sentence("Schüler der schreibt", False)
test_sentence("der Schüler und", False)
test_sentence("und der Schüler schreibt", False)
test_sentence("der Schüler Schüler", False)