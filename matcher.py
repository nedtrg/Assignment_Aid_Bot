import spacy
from spacy.matcher import Matcher

# Load spaCy model
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

patterns = [
    [{"LOWER": "help"}, {"LOWER": "me"}, {"LOWER": "with"}],
    [{"LOWER": "help"}, {"LOWER": "me"}, {"LOWER": "learn"}],
    [{"LOWER": "assist"}, {"LOWER": "me"}, {"LOWER": "with"}],
    [{"LOWER": "teach"}, {"LOWER": "me"}],
    [{"LOWER": "i"}, {"LOWER": "want"}, {"LOWER": "help"}, {"LOWER": "with"}],
    [{"LOWER": "i"}, {"LOWER": "need"}, {"LOWER": "help"}, {"LOWER": "with"}],
    [{"LOWER": "i"}, {"LOWER": "am"}],
    [{"LOWER": "my"}, {"LOWER": "name"},{"LOWER":"is"}],
    [{"LOWER": "what"}, {"LOWER": "is"}, {"LOWER": "the"}, {"LOWER": "capital"}, {"LOWER": "of"}, {"ENT_TYPE": "GPE"}],
    [{"LOWER": "what"}, {"LOWER": "is"}],
    [{"LOWER": "how"}, {"LOWER": "are"},{"LOWER":"you"}],
    [{"LOWER": "define"}],
    [{"LOWER": "fine"}],
    [{"LOWER": "explain"}],
    [{"LOWER": "describe"}],
    [{"LOWER": "solve"}, {"LOWER": "the"}, {"LOWER": "equation"}],
    [{"LOWER": "thank"}, {"LOWER": "you"}],
    [{"LOWER": "thanks"}]
]

# Add patterns to the matcher
for pattern in patterns:
    matcher.add("HomeworkPattern", [pattern])

def match_string(substring, mstring):
    p = []
    for s in substring:
        if s in mstring:
            p.append(s)
    return p
