import re

txt = "Use of python in Machine Learning"
v = re.search("^Use.*Learnings$", txt)
if (v):
    print("Yes! We have a match!")
else:
    print("No match")
