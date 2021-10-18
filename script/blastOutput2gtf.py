
BLASTN_FILE="/data2/eric/TE_LR_RNAseq/Dm_Goth_10-1_insertions_vsTEdb.bln"
NEW_ANNOTATION_FILE = "/data2/eric/TE_LR_RNAseq/Dm_Goth_10-1_insertions_vsTEdb.gtf"

def create_gtf_attributes(subjectId, chrom, start, end):
	gtf_attributes = 'gene_id "{}"; transcript_id "{}:{}:{}:{}";'.format(subjectId, subjectId, chrom, start, end)
	return gtf_attributes

def blastn_line_to_gtf_line(line):

	(queryId, subjectId, percIdentity, alnLength, mismatchCount, 
    gapOpenCount, queryStart, queryEnd, subjectStart, 
    subjectEnd, eVal, bitScore) = line.split("\t")
	strand = queryId.split(":")[0]
	seq = queryId.split(":")[2]
	startQueryId, endQueryId = queryId.split(':')[3].split("-")
	source = "dmgoth101"
	feature = "exon"
	score = "."
	phase = "."
	start = min(int(subjectStart), int(subjectEnd)) + int(startQueryId)
	end = max(int(subjectStart), int(subjectEnd)) + int(startQueryId)
	attributes = create_gtf_attributes(subjectId, seq, str(start), str(end))
	new_gtf_line = "\t".join([seq, source, feature, str(start), str(end), score, strand, phase, attributes]) + "\n"
	return new_gtf_line
	

def from_blastn_to_gtf(blastn_file, new_gtf_file):
	with open(new_gtf_file, 'w') as output:
		with open(blastn_file, 'r') as input:
			for line in input:
				gtf_line = blastn_line_to_gtf_line(line)
				output.write(gtf_line)


from_blastn_to_gtf(BLASTN_FILE, NEW_ANNOTATION_FILE)
