
# Questions BIO392 day 10
These questions are designed to test your understanding of the sequence analysis practical and the accompanying literature. Please change the name of this file to \<First letter\>-\<Last name\>-questions-day-10.md, (e.g., M-Mustermann-questions-day-10.md), and upload it to your folder in the course GitHub.

These questions will not be graded separately, but may be considered when determining your participation grade. The most important thing is not that you get everything right, but that you show that you thought about the questions; so no copy/pasting!

### Q1
**What information do the CHROM, POS, REF, and ALT columns contain in a VCF file?**
- **CHROM**: reference chromosome where a variant is located
- **POS**: position of the variant in the reference chromosome
- **REF**: reference allele(s) at the given position on the reference chromosome
- **ALT**: alternate allele(s) at the given position of the sequenced sample

### Q2
**Using these four columns, how could you determine whether a sequencing sample contains a variant?**
If the base(s) in the 'REF' and 'ALT' field are not the same, the sequenced sample contains a variant.

### Q3
**After loading all the files into IGV, there should be four different kind of tracks. Briefly explain what type of information each track contains**
- first track: our custom APC reference sequence (only reference genome uploaded via genome button)
- second track: VCF file shows where the alternative alleles are (light blue means there is a variant, grey means theres no difference between sampled sequence and reference genome)
- third track: GTF file shows the length of the gene (APC gene) and where Coding Sequences (CDS) are on the gene (marked below the gene)
- fourth track: BAM file shows number of reads and mapping quality (if coloured: bad quality)

### Q4
**Based on the VEP output, which of the STR variants you identified do you expect to have the most impact? Why?**
Intron variants are the most prevalent (40%) but don't have much influence. The most impact has the variant in the coding sequence (GAGAGAGA) as it leads to a frameshift mutation and thus leads to different amino acids and stop of translation.

### Q5
**What phenotype or disease do you expect this variant to be involved with?**
The phenotype with this frameshift variant is involved in the formation of large intestine tumours.
