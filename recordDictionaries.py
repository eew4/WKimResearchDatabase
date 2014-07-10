#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def mutationKeyValue(key):
	options = {	'aa_new_seq':0,
				'aa_position':1,
				'aa_ref_seq':2, 
				'codon_new_seq':3,
				'codon_number':4,
				'codon_position':5,
				'codon_ref_seq':6,
				'frequency':7,
				'gene_list':8,
				'gene_name':9,
				'gene_position':10,
				'gene_product':11,
				'gene_strand':12,
				'html_gene_name':13,
				'locus_tag':14,
				'snp_type':15,
				'transl_table':16}
	return options[key]

def RAKeyValue(key):
	options = {	'aa_new_seq':0,
				'aa_position':1,
				'aa_ref_seq':2,
				'bias_e_value':3,
				'bias_p_value':4,
				'codon_new_seq':5,
				'codon_number':6,
				'codon_position':7,
				'codon_ref_seq':8,
				'deleted':9,
				'fisher_strand_p_value':10,
				'frequency':11,
				'gene_list':12,
				'gene_name':13,
				'gene_position':14,
				'gene_product':15,
				'gene_strand':16,
				'genotype_quality':17,
				'html_gene_name':18,
				'ks_quality_p_value':19,
				'log10_base_likelihood':20,
				'log10_qual_likelihood_position_model':21,
				'log10_strand_likelihood_position_model':22,
				'locus_tag':23,
				'mixed':24,
				'new_cov':25,
				'new_seq':26,
				'no_show':27,
				'polymorphism_changed_to_consensus':28,
				'polymorphism_quality':29,
				'quality':30,
				'quality_position_model':31,
				'ref_cov':32,
				'reject':33,
				'ref_seq':34,
				'snp_type':35,
				'tot_cov':36,
				'transl_table':37}
	return options[key]
def MCKeyValue(key):
	options = {	'gene_name':0,
				'gene_product':1,
				'html_gene_name':2,
				'left_inside_cov':3,
				'left_outside_cov':4,
				'locus_tag':5,
				'right_inside_cov':6,
				'right_outside_cov':7}
	return options[key]
def JCKeyValue(key):
	options = {	'alignment_overlap':0,
				'circular_chromosome':1,
				'coverage_minus':2,
				'coverage_plus':3,
				'flanking_left':4,
				'flanking_right':5,
				'frequency':6,
				'overlap_registers':7,
				'junction_key':8,
				'junction_possible_overlap_registers':9, ##added
				'key':10, ##added
				'max_left':11,
				'max_left_minus':12,
				'max_left_plus':13,
				'max_min_left':14, ##added
				'max_min_left_minus':12,
				'max_min_left_plus':13,
				'max_min_right':14,
				'max_min_right_minus':15,
				'max_min_right_plus':16,
				'max_pos_hash_score':17,
				'max_right':18,
				'max_right_minus':19,
				'max_right_plus':20,
				'neg_log10_pos_hash_p_value':21,
				'new_junction_coverage':22,
				'new_junction_frequency':23,
				'new_junction_read_count':24,
				'pos_hash_score':25,
				'reject':26,
				'read_count_offset':27,
				'side_1_annotate_key':28,
				'side_1_continuation':29,
				'side_1_coverage':30,
				'side_1_possible_overlap_registers':31,  ##added
				'side_1_overlap':31,
				'side_1_overlap_register':32,
				'side_1_read_count':33,
				'side_1_redundant':34,
				'side_2_annotate_key':35,
				'side_2_continuation':36,
				'side_2_coverage':37,
				'side_2_possible_overlap_registers':38, ##added
				'side_2_overlap':38,
				'side_2_overlap_register':39,
				'side_2_read_count':40,
				'side_2_redundant':41,
				'total_non_overlap_reads':42,
				'unique_read_sequence':43}
	return options[key]