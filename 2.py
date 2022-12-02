

shape_pts = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


LOSS=0
DRAW=3
WIN=6




loses = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

draws = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}



with open("input") as f:
    total_points = 0
    for l in f.readlines():
        a, b = l.split(" ")
        b = b.replace("\n","")
        
        select = None
        if b == "X":
            total_points += LOSS
            select = loses[a]
        elif b == "Y":
            total_points += DRAW
            select = draws[a]
        else:
            total_points += WIN
            select = wins[a]
        
        total_points += shape_pts[select]



print(total_points)

