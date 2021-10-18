GTF_INPUT = "/data2/eric/TE_LR_RNAseq/data/dmgoth101_genome_alignments/annotations/dmgoth101.onecode.v2.gtf"
TE_HIERARCHY = "/data2/eric/TE_LR_RNAseq/HIERARCHY_DF.tsv"
CSV_OUTPUT = "/data2/eric/TE_LR_RNAseq/data/dmgoth101_genome_alignments/annotations/TE_classification.v2.tsv"

# ['2558', '4.3', '0.8', '1.7', '2L_RaGOO', '1', '356', '353', '+', 'IVK_DM', 'LINE/I', '5010', '5362', '(40)', '1', '1', '0.065']

TE_dict = {}

with open(TE_HIERARCHY, 'r') as input:
	input.readline()
	for line in input:
		sline = line.strip().split("\t")
		TE_dict[sline[2]] = sline

with open(CSV_OUTPUT, 'w') as output:
	with open(GTF_INPUT, 'r') as input:
		for line in input:
			sline = line.strip().split('\t')
			# print(sline)
			attributes = sline[8]
			gene_id = attributes.split('"')[1]
			transcript_id = attributes.split('"')[3]
			if gene_id not in TE_dict.keys():
				print(gene_id)
# 			chrom, start, end = sline[4:7]
# 			TE_id, TE_family = sline[9:11]
# 			subclass, superfamily = TE_family.split("/")
# 			transcript_id = "$".join([TE_id, chrom, start, end])
# 			new_line = "\t".join([subclass, superfamily, TE_id, transcript_id]) + "\n"
# 			output.write( new_line)