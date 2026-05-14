subject=input(str("what is your subject? Enter all lowercases."))

if subject="math":
    M=subject
else subject="reading":
    R=subject
list=[f"grade", "score", "math", "reading"]
score=input(int(f"what is your nwea {list[1]} for {list[0]}"))
if score<=160:
    print