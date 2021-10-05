RM_FILE = "/data2/eric/TE_LR_RNAseq/data/pour_Eric/dmgoth101_onecode.all_chr.csv"
NEW_GTF = "/data2/eric/TE_LR_RNAseq/data/pour_Eric/dmgoth101.onecode.v3.gtf"

# 2558    4.3     0.8     1.7     2L_RaGOO        1       356     353     +       IVK_DM  LINE/I  5010    5362    (40)    1       1       0.065
# TO
# 2L_RaGOO        dmgoth101       exon    1       356     2558    +       .       gene_id "IVK_DM"; transcript_id "IVK_DM_2L_RaGOO_1_356";
with open(NEW_GTF, 'w') as output:
	with open(RM_FILE, 'r') as input:
		for line in input:
			sline = line.strip().split("\t")
			chrom, start, end, score, strand, gene_id, family = sline[4:11]
			subclass, superfamily = family.split("/")
			source = "dmgoth101"
			feature = "exon"
			phase = "."
			transcript_id = "$".join([gene_id, chrom, start, end])
			attributes = 'gene_id "{}"; transcript_id "{}";'.format(gene_id, transcript_id)
			new_line = "\t".join([chrom, source, feature, start, end, score, strand, phase, attributes]) + "\n"
			output.write(new_line)
