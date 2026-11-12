
import re
POSITIVE = {"seen","only","needed","relatable","thank","understood","feel","helpful","same","exactly"}
NEGATIVE = {"not","never","disagree","doesnt","does","irrelevant","wrong","unhelpful"}
def label_comment(text):
    words=set(re.findall(r"[a-z']+",str(text).lower()))
    score=len(words & POSITIVE)-len(words & NEGATIVE)
    sentiment="Positive" if score>0 else ("Negative" if score<0 else "Neutral")
    relatable="Relatable" if ({"seen","only","relatable","understood","same","needed"} & words) else "Neutral"
    return sentiment, relatable
