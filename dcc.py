import csv
import re
from progress.bar import Bar


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


beresford = []

with open("vocab_beresford_2.tsv", "r", encoding="utf-8") as g:
    reader = csv.reader(g, delimiter="\t")
    for row in reader:
        beresford.append(row)

dcc_i = []

with Bar("Working...", max=len(beresford)) as bar:

    for i, row in enumerate(beresford):
        row_1 = row[1]
        for headword in dcc_headwords:
            if re.match(f"^{headword}$", row_1):
                dcc_i.append(i)
                # print(headword,"->",row_1,"\n",beresford[i])
                bar.next()

print(len(beresford))
print(len(dcc_i))
for i in sorted(dcc_i, reverse=True):
    del beresford[i]



print(len(beresford))
with open("vocab_beresford_2_no_dcc.tsv", "w", newline="", encoding="utf-8") as o:
    writer = csv.writer(o, delimiter="\t")
    writer.writerows(beresford)