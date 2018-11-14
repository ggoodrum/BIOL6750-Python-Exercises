# Author: Greg Goodrum
# Course: BIOL 6750 with Dr. Will Pearse
# Section: 11 - Introduction to BioPython
# Exercise 11
# ----------------

# 1. Write a function that searches Entrez for a particular gene in a particular species.


def gene_retrieve(genus, species, gene, database):
    from Bio import Entrez
    term_input = str('(' + genus + ' ' + species + '[Organism]) AND ' + gene + '[Gene]')
    handle = Entrez.esearch(db=database, term=term_input, retmode='text')
    generet_results = Entrez.read(handle)
    handle.close()
    return generet_results


results = gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')


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


# 3. Write a wrapper function that uses your functions above to search for a gene for a
# particular species, the download the first such sequence it finds.


# This version requires running the previous two functions
def first_gene_retrieve(genus, species, gene, database):
    entrez_gene = gene_retrieve(genus, species, gene, database)
    seq_return = seqID_download(database=database, Entrez_gene=entrez_gene)
    return seq_return


first_gene_retrieve('quercus', 'robur', 'rbcL', 'nucleotide')


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


# 4. Got to the BioPython cookbook website and use that to write the code (no need to wrap
# it in a function unless you want) to save a sequence to your harddrive.
