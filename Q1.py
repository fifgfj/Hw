info = {
        ("123","a") : [80,70,50,59,43]
        ,("12356","b") : [80,70,50,59,43]
        ,("151356","c") : [80,70,50,59,43]
        }
def good_student():
    for i in range(5):
        if info["123","a"[i]] > 80:
            b =+ 1
        if b >= 2:
            return info["123","a"]
    for i in range(5):
        if info["12356","b"[i]] > 80:
            b =+ 1
        if b >= 2:
            return info["12356","b"]
    for i in range(5):
        if info["151356","c"[i]] > 80:
            b =+ 1
        if b >= 2:
            return info["151356","c"]
good_student()
print(good_student())