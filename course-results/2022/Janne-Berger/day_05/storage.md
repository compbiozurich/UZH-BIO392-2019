# WGS 
Advantages: <br>
Coverage of all genes and also non-coding DNA  <br>
Disadvantages:<br>
Low acuracy, longest turnaround time, most expensive, depth 30 x<br>
# WES
Advantages:<br>
At least entire exome, good acuracy, cost effective and higher depth<br>
Disadvantages:<br>
Still long turnaround time<br>
# Different file formats
## FASTA
1. Reference genome comes typically in fasta format
2. ">" line contains the scaffold name
3. Following lines contain the sequence (single line, 80 nt-column sized...)<br>
4. Example: <br>
\>NC_009902.1 Babesia bovis T2Bo mitochondrion, complete genome
TTTAAAAAAGTGTTAAAAACTTTATACATTAAAAAATTTAAACAAGTGATCATGTATAAAGTACACTTGT
TACTGTGTAAATATCAAAAACAATTTAATTTCAAAATTTTTGAAATATGTTTTTTGTGTTGTGTTATAAA
GTTTTTTTTCAAAATTATATATGTTTGCATTTGCTGGATATAGTTCGGTCTCTGCAAACCATAAAGTCAT
CGGTATATCCTACATATGGCTTTCATATTGGTTTGGAGTTATTGGATTTTATATGAGTATTTTGATAAGA
ACAGAATTGAGTATGAGTGGTTTAAAGATTATGACAATGGATACTCTTGAGATATACAATATGATGTTTT
(...) <br>
## FASTQ
1. Like Fasta but with quality information
2. Plain text files with chunks of four lines:
   1. @ identifier line
   2. Sequence
   3. "+" (sometimes the sequence name, again)
   4. Quality scores (different encodings exist)
3. Sequence quality is represented using Phred scores
4. The sequencing quality score of a given base Q is defined by as Q = −10 log10 P <br>
5. Example: <br>
@SRR001666.1 071112_SLXA-EAS1_s_7:5:1:817:345 length=36 <br>
GGGTGATGGCCGCTGCCGATGGCGTCAAATCCCACC <br>
\+ <br>
IIIIIIIIIIIIIIIIIIIIIIIIIIIIII9IG9IC <br>
## SAM
1. Consists of one header section and one alignment section
2. The lines in the header section start with character ‘@’, and lines in the alignment section do not
3. SAM (Sequence Alignment Map) files are human-readable text files
4. BAM (Binary Alignment Map)files are their binary (and compressed) equivalent

![grafik](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2F1756-0381-6-13/MediaObjects/13040_2013_Article_92_Fig8_HTML.jpg?as=webp)
## VCF
1. Standardfile format for storing variation data
2. Unambiguous, scalable and flexible
3. 8 columns:CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO

![grafik](https://www.ebi.ac.uk/training/online/courses/human-genetic-variation-introduction/wp-content/uploads/sites/76/2020/05/fig12.png)
# Costs
Costs to store 1 GB = 0.5 CHF <br>
2 bites are enough per base(pair)<br>
Genome= 3 bilion bp<br>
Exons= 1.5 % of the genome = 45000000 bp<br>

## WGS
### Raw data
2*(3*10^9) = 6000000000 bits<br>
6000000000 bits = 750 megabyte<br>
For 1000 genes =  750000 megabytes = 375 CHF<br>
## WES
### Raw data
2*45000000 = 90000000 bits<br>
90000000 bits = 11.24 megabyte<br>
for 1000 genes = 11250 megabytes = 5.625 CHF <br>