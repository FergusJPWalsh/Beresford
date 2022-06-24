import csv
import re

dcc_headwords_in = []

with open("greek-core-list.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        dcc_headwords_in.append(row[0])

dcc_headwords = []

for item in dcc_headwords_in:
    item = item.replace(",","")
    part = item.partition(" ")[0]
    dcc_headwords.append(part)

dcc_headwords = sorted(dcc_headwords)

beresford = []

with open("vocab_beresford_2.tsv", "r", encoding="utf-8") as g:
    reader = csv.reader(g, delimiter="\t")
    for row in reader:
        beresford.append(row)

unique = []
vocab_set = set()

for i, row in enumerate(beresford):
    token = row[1]
    if token not in vocab_set:
        unique.append(row)
        vocab_set.add(token)

not_dcc = []
for i, row in enumerate(unique):
    token = row[1]
    if token not in dcc_headwords:
        not_dcc.append(row)

print("original list",len(beresford))
print("list with unique lemmata and with DCC removed",len(not_dcc))

with open("vocab_beresford_2_no_dcc.tsv", "w", newline="", encoding="utf-8") as o:
    writer = csv.writer(o, delimiter="\t")
    writer.writerows(not_dcc)