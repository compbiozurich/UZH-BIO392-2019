
# Questions BIO392 day 08
These questions are designed to test your understanding of the sequence analysis practical and the accompanying literature. Please change the name of this file to \<First letter\>-\<Last name\>-questions-day-08.md, (e.g., M-Mustermann-questions-day-08.md), and upload it to your folder in the course GitHub.

These questions will not be graded separately, but may be considered when determining your participation grade. The most important thing is not that you get everything right, but that you show that you thought about the questions; so no copy/pasting!

## Practical

### Q1 Does the sequence quality graph of your data look different from the examples shown in the slides? Are there any adapter sequences in the data? Why do you think this is?**
- Yes, the graph looks diffrent. The quality, reflected as a Phred score is much higher for the single nucleotides as in the graph of the slides. Under the ADAPTER CONTENT section you see that there are no adapters used.  

### Q2 Given the FastQC reports, does it make sense to perform adapter and/or quality-trimming on your data?**
- No, I would say it wouldn't make any sense to make a quality trim or adapter trim, cause the quality for the nucleotides are already very high. 

### Q3 Why are so many files in the bioinformatics pipeline compressed and indexed?**

- Basically, data compression can save a lot of memory, but it also makes the handling more convenient for the processing of the data.
- Indexing make the work more efficient to get datas/informations of bigger datasets back. 

### Q4 In the bash script that processes alignment files, you will see calls to samtools sort, samtools view, and samtools index (among others). Explain what these three programs do. Why do you think each program is needed?**
*Hint: look at the [Samtools manual](http://www.htslib.org/doc/samtools.html)*.


- samtools index:
  handles SAM, BAM and CRAM files and is required when region arguments are used to specify specific regions of interest for samtools view and
  related operations.

- samtools view:
  Given Datas in SAM, BAM or CRAM format will be converted to SAM files and you can provide area specifications to
  limit the output for alignments that overlap the specified regions. 

- samtools sort:
  Alignments can be sorted by leftmost coordinates or for a specifc sequences if you use ' -n '. 



### Q5 Explain what files are needed for GangSTR to run. Specifically: explain what information is provided to GangSTR via the --ref, --region, and --bam command line arguments.**
*Hint: look at the [GangSTR manual](https://github.com/gymreklab/gangstr).*

- GangSTR handles BAM files and and takes repeats in the reference genome as an input and  will get you outputs in a VCF format containing genotypes for each locus.


--ref stands for the Refererence genome (.fa) \
--region stands for the Target TR loci (regions) (.bed) \
--bam stands for Comma separated list of input BAM files\
--bam-samps <string>  you can also create a comma separated list of sample IDs for --bam \



## Literature
During the practical so far, you have generated variant calls from short read sequencing data using bioinformatics approaches. Now it's time to take a step back and do some background reading in order to prepare for the analysis and interpretation of the results next week. 

First, read the following sections of [this review](https://www.sciencedirect.com/science/article/pii/S0959437X16301538):
* Abstract
* Introduction``
* Genotyping STRs from high-throughput sequencing data
Then, answer Q6 and Q7.

### Q6 Why is STR variation relevant to health and disease?**

Because STRs are so often naturally repetitive, errors can occur during DNA replication what leads to frequent mutations in the number of repeats and therefore represent high mutation rates, much higher than other variations, so STR expansions are often found together with many disorders. 


### Q7 What are some of the challenges in analysing STRs from NGS data?**

One of the problems can occur when you have very short segments, as it is more difficult to match them with the reference genome due to the lack of information/number of nucleotides. Another problem is that errors can occur in PCR, i.e. there can be deletions or insertions that lead to further errors in the process, so you want to match them with the reference genome, but this can lead to some discrepancies.  

Second, read the following sections of the [paper describing GangSTR](https://academic.oup.com/nar/article/47/15/e90/5518310):
* Abstract
* Introduction
* Overview of the GangSTR model
Then, answer Q8 and Q9.

### Q8 What sets GangSTR apart from other STR genotyping tools?**
Most of the currently available tools have mostly concentrated on repeat-enclosing read.
To determine maximum likelihood TR lengths, GangSTR gathers data from paired-end reads and fuse it into a single model.
Several characteristics of paired-end short reads can provide information about the size of a repeating area.
Researchers are using GangSTR in the future to try to discover new disease-associated variants that are currently not accessible with NGS.

### Q9 What types of information does GangSTR use for STR genotyping?**
A sequence alignment and a reference set of TRs are inputs for the GangSTR, which works via end-to-end method that provides an estimated repeat length. The most important part of this method is a maximum likelihood framework that combines different information from short paired-end reads into a single model and applies it separately to each TR in the genome.




