### Q1
**What information do the CHROM, POS, REF, and ALT columns contain in a VCF file?**
* CHROM: Which chromosome are we on? It is identified via the reference genome. 
* POS: Which position contains a variant? 
* REF: What is the nucleotide in the reference genome? A ‘.’ means there is no variant.  
* ALT: What is the alternate allele of our sequence at this position? 

### Q2
**Using these four columns, how could you determine whether a sequencing sample contains a variant?**
* Check the ALT column and see which nucleotide is noted there.  
* To double-check you compare it with the base in the 	REF column.

### Q3
**After loading all the files into IGV, there should be four different kind of tracks. Briefly explain what type of information each track contains**
* We have the tracks with the alignments of each patient. We see the different reads and their associated information when we click on them (read name, alignment start and map quality). At the top of each alignment we see a profile which could be the coverage of each base.
* We also have one track that represents the gene, with information on the source and the location on the chromosome that we are at. 
* Another one representing the transcript.
* And the last one “merged_results.vcf” contains the variant information for each patient.  

### Q4
**Based on the VEP output, which of the STR variants you identified do you expect to have the most impact? Why?**
I expect the longer STR variant (agagagaga) to have most impact because it leads to a frameshift mutation in an exon.  

### Q5
**What phenotype or disease do you expect this variant to be involved with?**
The phenotype that is associated with this variant is a tumor in the large intestine or in the stomach.  
