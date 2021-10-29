import csv
chimera_file = "chimeric_reads/potential_chimeric_reads.no_overlap.male.tsv"
chimera_count_dict = dict()

with open(chimera_file, 'r') as input:
	for line in input:
		TE_insertion = line.split("\t")[0]
		if TE_insertion not in chimera_count_dict:
			chimera_count_dict[TE_insertion] = 1
		else:
			chimera_count_dict[TE_insertion] += 1
# print(max(chimera_count_dict, key=chimera_count_dict.get))
sorted_chimera_dict = dict(sorted(chimera_count_dict.items(), key=lambda item: item[1], reverse=True))

# print(list(sorted_chimera_dict.keys())[:20])

csv_file = "chimeric_TE_insertion.male.tsv"
with open(csv_file, "w") as output:
	writer = csv.writer(output, delimiter="\t")
	for [insertion, count] in sorted_chimera_dict.items():
		writer.writerow([insertion, count])

