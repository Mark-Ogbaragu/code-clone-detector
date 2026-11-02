from difflib import SequenceMatcher
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()
code1 = "def add(a,b): return a+b"
code2 = "def add(x,y): return x+y"
score = similarity(code1, code2)
print(f"Similarity: {score:.2f} - Clone!" if score>0.8 else "Not clone")
