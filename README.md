# Evidence-2-Context-Free-Grammar
## Language chosen
### Description
The language chosen  is the German language. More precisely, the language specifically for a school context. This subset focuses on sentences a student would build in the everyday school life.

#### Language Structure
According to (Klein, 2025), the golden German rule in sentence structure is that the verb is the second element in a sentence. But that does not mean that it needs to be the second word. With this in mind, German structure tends to be a bit confusing. <strong> Many sentences can mean the same, but will be with a different structure</strong>. For example:
- Der Schüler liest das Buch
- Das Buch liest der Schüler.
That is why this language is perfect for this project. By eliminating ambiguity, this language will change from an ambiguos natural language to a properly defined grammar. So that we can develop a parser to process the grammar developed.

#### Rules

In German sentence Structure, there are certain structures that represent how a Sentence must follow certain steps to be created. 
- A sentence Structure follows a Noun phrase with a Verb phrase.
- Adjectives before nouns -> For an adjective to be placed in a sentence, its position must be before a Noun.
- Prepositional Phrases -> In german when we use a prepositional element, it must be followed by a noun phrase. Could be represented as PP -> Prep NP
- Conjunctions -> A conjunction is a connection between two verb phrases.
- A Nominal Phrase Can be connected with another by a conjunction.
- A verb phrase can have either a preposition or a connection of conjunction.

### Models
With all the rules previously mentioned, our grammar initially look like this:
```python
S -> NP VP
NP -> NP Conj NP | Det NOM
NOM -> Adj NOM | N
VP -> VP Conj VP | V PP| V NP PP| V NP | V
PP -> Prep NP
Det -> 'der' | 'die' | 'das' | 'ein' | 'eine'
Adj -> 'fleißige' | 'kleine' | 'schwere' | 'neue'|'intelligent'|'interessant'|'alt'
N   -> 'Schüler' | 'Lehrerin' | 'Buch' | 'Klasse' | 'Klassenzimmer'|'Rucksack'|'Kurs'
V   -> 'lesen' | 'schreibt' | 'ist' | 'erklärt' | 'macht'|'machen'
Prep -> 'in' | 'mit' | 'auf'
Conj -> 'und' | 'oder'

```python
As you can see, the grammar can be segmented in several types of sentence structures. Which according to (GeeksforGeeks, 2025) could be interpreted as a context Free grammar (CFG). It says that on the left side it can only be a Variable in there, not a terminal, however the right side can be either non terminal or terminal.

For the visualization of the ambiguity and left recursion with our grammar the sentence will  be the following.

"Der Schüler liest und schreibt und erklärt"

With this sentence there are two type of trees that can be made according to our grammar.




- Ambiguity elimination process
- Left Recursion Elimination
Include the corresponding syntactic trees to show the changes in the grammar.

### Implementation and tests
Implement a tester for your grammar using a natural language toolkit or library such as nltk in python,
You can choose a substitute but you should schedule an appointment to make sure I can run it before the hand-in.
If I can't compile/run it, you will get 0 as a grade.
Implement and document a set of tests that show both: strings that should be accepted by the grammar and strings that shouldn't.
Test documentation should include examples of the pushdown automata or LL1 parsing for the grammar and a specific string.
### Analysis.

#### Chomsky's Hierarchy before elimination of Ambiguity and LR

#### Chomsky's Hierarchy after elimination of Ambiguity and LR
#### Time implications
Explain the time implications of the different levels and provide a brief example of a string of each level
#### References 
- Klein, A. (2025, March 22). Mastering German Word Order: An Absolute Beginner’s Guide. LearnOutLive. https://learnoutlive.com/german-word-order-guide-for-beginners/

- GeeksforGeeks. (2025, July 23). What is ContextFree Grammar? GeeksforGeeks. https://www.geeksforgeeks.org/theory-of-computation/what-is-context-free-grammar/

