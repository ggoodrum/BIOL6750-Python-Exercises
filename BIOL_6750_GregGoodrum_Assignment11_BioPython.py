# Author: Greg Goodrum
# Course: BIOL 6750 with Dr. Will Pearse
# Section: 11 - Introduction to BioPython
# Exercise 11
# ----------------


# Always establish email identity before accessing sequence information
from Bio import Entrez
Entrez.email = 'goodrum.greg@aggiemail.usu.edu'


# 1. Write a function that searches Entrez for a particular gene in a particular species.


def gene_retrieve(genus, species, gene, database):
    from Bio import Entrez
    term_input = str('(' + genus + ' ' + species + '[Organism]) AND ' + gene + '[Gene]')
    handle = Entrez.esearch(db=database, term=term_input, retmode='text')
    generet_results = Entrez.read(handle)
    handle.close()
    return generet_results


results = gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')
print(results)
print('End: Q1')


# 2. Write a function that downloads a particular SeqID that it's given from GenBank


def seqID_download(database, Entrez_gene):
    from Bio import SeqIO
    from Bio import Entrez
    seq_id = Entrez_gene['IdList'][0]
    # print(seq_id)
    handle = Entrez.efetch(db=database, id=seq_id, rettype='gb', retmode="text")
    # print(handle)
    seq_record = SeqIO.read(handle, "genbank")
    handle.close()
    return seq_record


seq_record = seqID_download('nucleotide', results)
print(seq_record)
print('End: Q2')


# 3. Write a wrapper function that uses your functions above to search for a gene for a
# particular species, the download the first such sequence it finds.


# This version requires running the previous two functions
def first_gene_retrieve(genus, species, gene, database):
    entrez_gene = gene_retrieve(genus, species, gene, database)
    seq_return = seqID_download(database=database, Entrez_gene=entrez_gene)
    return seq_return


first_gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')
my_seq = first_gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')


# This version is self-contained
def first_gene_retrieve(genus, species, gene, database):
    from Bio import SeqIO
    from Bio import Entrez
    term_input = str('(' + genus + ' ' + species + '[Organism]) AND ' + gene + '[Gene]')
    handle = Entrez.esearch(db=database, term=term_input, retmode='text')
    Entrez_gene = Entrez.read(handle)
    handle.close()
    seq_id = Entrez_gene['IdList'][0]
    # print(seq_id)
    handle = Entrez.efetch(db=database, id=seq_id, rettype='gb', retmode="text")
    # print(handle)
    seq_record = SeqIO.read(handle, "genbank")
    handle.close()
    return seq_record


first_gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')
# my_seq = first_gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')
print(my_seq)
print('End: Q3')


# 4. Got to the BioPython cookbook website and use that to write the code (no need to wrap
# it in a function unless you want) to save a sequence to your harddrive.


from Bio import SeqIO
SeqIO.write(my_seq, 'example_seq.faa', 'fasta',)
print('End: Q4')


# 5. Got to the BioPython cookbook website and use that to write the code (no need to wrap
# it in a function unless you want) to load a sequence from your harddrive.


# Use SeqIO.read() for single sequences, SeqIO.parse() for multiple sequences which uses indexing
from Bio import SeqIO
fasta_sequence = SeqIO.read(open('example_seq.faa'),'fasta')
print(fasta_sequence)
print('End: Q5')


# 6. Go to the BioPython Cookbook and use that to write the code to save, and then load back
# in the alignment created above.

# ---- Create alignment data for use in exercise ----
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq


align = MultipleSeqAlignment([
    SeqRecord(Seq('ACGTACGTACGTACGT', generic_dna), id='quercus_robur'),
    SeqRecord(Seq('ACGTCCGTACTTACGA', generic_dna), id='quercus_ilex'),
    SeqRecord(Seq('CCGTCCGGACATACGA', generic_dna), id='quercus_rubra'),
    SeqRecord(Seq('AGGTCAGTACTTGCGA', generic_dna), id='quercus_macrocarpa')
])
# ---- Begin exercise answer ----


# Write alignment to file
from Bio import AlignIO
AlignIO.write(align, 'example_alignment.phylip', 'phylip')


# Read alignment from file (use Bio.AlignIO.read for single alignments, Bio.AlignIO.parse for multiple alignments)
from Bio import AlignIO
test_alignment_read = AlignIO.read('example_alignment.phylip', 'phylip')


print(test_alignment_read)
print('End: Q6')



# 7. Write a function that BLAST-searches a given sequence in GenBank, prints out how many
# matches passed a certain threshold, and returns the blast search results.


def blastSearch(sequence_record, less_than_threshold):
    # Import required packages
    from Bio.Seq import Seq
    from Bio.Blast import NCBIWWW, NCBIXML
    # Convert the sequence record to a sequence (i.e. strip annotations and background)
    seq = sequence_record.seq
    # print('1')
    # Create a handle for the blast search
    result_handle = NCBIWWW.qblast("blastn", "nt", seq)
    # print('2')
    # Create an object to hold results of the blast search
    blast_records = NCBIXML.read(result_handle)
    # Create a blank list to hold all the blast records that are beyond a given threshold
    # print('4')
    blast_records_threshold = []
    # For every returned alignment in the blast records
    for alignment in blast_records.alignments:
        # For every high scoring pair in the alignments
        for hsp in alignment.hsps:
            # If the hsp.expect value is less than 0.001
            if hsp.expect < less_than_threshold:
                # Add the alignment into a the threshold list
                blast_records_threshold.append(alignment)
    print('Number of alignments with hsp.expect < ' + str(less_than_threshold) + ' = ' + str(len(blast_records_threshold)))
    return blast_records


test_blast_records = blastSearch(seq_record, .01)


print(test_blast_records)
print('End: Q7')


# 8. Write a function that builds a neighbor-joined tree from an alignment.


def create_NJ_tree(alignment):
    # Import Phylo library for tree constructor and draw methods
    from Bio import Phylo
    from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
    # Create simpler names for tree-constructing methods
    constructor = DistanceTreeConstructor()
    calculator = DistanceCalculator('identity')
    # Calculate the distances between the sequences in alignment
    dists = calculator.get_distance(alignment)
    # Create the phylo tree
    tree = constructor.nj(dists)
    # Print the phylo tree
    print(Phylo.draw_ascii(tree))
    # Return the phylo tree
    return tree

test_tree = create_NJ_tree(test_alignment_read)
print(test_tree)
print('End: Q8')
print('---- End Exercise ----')
