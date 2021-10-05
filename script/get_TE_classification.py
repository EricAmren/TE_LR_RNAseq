RM_OUTPUT = "/data2/eric/TE_LR_RNAseq/data/dmgoth101_genome_alignments/annotations/dmgoth101_onecode.all_chr.csv"
CSV_OUTPUT = "/data2/eric/TE_LR_RNAseq/data/dmgoth101_genome_alignments/annotations/TE_classification.from_RM_output.csv"

# ['2558', '4.3', '0.8', '1.7', '2L_RaGOO', '1', '356', '353', '+', 'IVK_DM', 'LINE/I', '5010', '5362', '(40)', '1', '1', '0.065']

with open(CSV_OUTPUT, 'w') as output:
	with open(RM_OUTPUT, 'r') as input:
		for line in input:
			sline = line.strip().split()
			chrom, start, end = sline[4:7]
			TE_id, TE_family = sline[9:11]
			subclass, superfamily = TE_family.split("/")
			transcript_id = "$".join([TE_id, chrom, start, end])
			new_line = "\t".join([subclass, superfamily, TE_id, transcript_id]) + "\n"
			output.write( new_line)
