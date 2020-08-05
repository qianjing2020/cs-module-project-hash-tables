# indexing

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Erin", "Engineering")
]

index = {}
def build_index():
    for r in records:
        dept = r[1]
        if dept not in index:
            index[dept]=[]
        index[dept].append(r)
build_index()

print(index)