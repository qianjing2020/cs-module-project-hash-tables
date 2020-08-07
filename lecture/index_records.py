# indexing
# get records for all Engineering personnel
records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Erin", "Engineering")
]

engineers = []
for record in records:
    if record[1] =='Engineering':
        engineers.append(record)

# let's make an index for instant access by attribute search
indexed_records = {}

def build_index():
    for record in records:
        # find dept attribute for each record
        dept = record[1]
        if dept not in indexed_records:
            indexed_records[dept] = []
        indexed_records[dept].append(record)

build_index()

print(indexed_records['Engineering'])

