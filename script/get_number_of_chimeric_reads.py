BAM = "/data2/eric/TE_LR_RNAseq/data/dmgoth101_genome_alignments/bam/FC30.against_dmgoth.filtered_max_AS.primary_only.bam"

import pysam

tot_nb_of_reads = 0
tot_nb_of_chimeric_reads = 0
with pysam.AlignmentFile(BAM) as bam:
	for ali in bam:
		tot_nb_of_reads += 1
		if ali.has_tag("SA"):
			tot_nb_of_chimeric_reads += 1
print(tot_nb_of_reads, tot_nb_of_chimeric_reads)