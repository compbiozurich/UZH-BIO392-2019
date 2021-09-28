## How big is a genome in terms of bytes?

So, I found a good article which gives a good overview about how to calculate the ways, in which different sizes of basepairs can be converted into Bytes. 

Below I will present a table, where one can check which file takes how many Bytes for which size of base pairs. 


[The article can be found here](https://medium.com/precision-medicine/how-big-is-the-human-genome-e90caa3409b0). 


| File format   | Base pairs    | Bytes  |
| ------------- |:-------------:| -----:|
| None, just bp | whole genome  | 700mb |
| FASTQ         | whole genome  | 200gb |
| VCF           | whole genome  | 125mb |


So now I will present the calculations from the article:


1. For no file format it's 2 bits per basepair. So we have 2x3 billion base pairs = 6 billion base pairs. But we search it in Bytes. So we know a Byte is a sequence of Bits (usually 8). And from there we calculate: We divide the 5'800'000 bits by 8 and get 750'000'000 bytes. This we divide by 1024 (2x2x2x2x2x2x2x2x2x2) and we get 715 mega bytes. So there we have our answer. Of course, to find out how much stoarge 1000 genomes would use, we would calculate 715mb x 1000 = 715'000 mb = 750 GB for 1000 genomes.
2. For FASTQ we have to consider the alignment process. Here we assume that one base pair equals 1 byte, not one bit. We call the alignment process coverage. A coverage of 30 means that for one genome we found 30 alignments, so to speak (the genome was covered by 30 sequence reads). If we now have 3 billion base pairs, and a coverage of 30, we have 90 billion letters, which equals around 90 GB space. So double the haploid genome, and all in all we get around 180-200 GB. Again, if we calculate for 1000 genomes, we get 200gb x 1000 = 200'000 GB = 200 TB.
3. For the variant file format, we look at the specific format it presents and find that one line uses 45 bytes. So we multiply this by by 3 million variants (0.1% of the genome) and we get a VCF-file of about 135'000'000 bytes, which is around 125 megabytes. 

As we see, it depends very much on what we'd like to cover. And the different file formats will present very different things. The variant file format of course only presents the variants present in the genome. But also for the file formats, the article only presents some version of a calculation. In the end, many factors play a role when trying to calculate something like this.


----
## THE PYTHON TOOL SEGMENT_LIFTOVER

Finally, some thoughts on segment_liftover tool for Python from the Article by Baudis et Al. The success rate of 99.99% in one of the "use" examples seems very good, especially good if one wants to switch from some of the most famous versions of the reference genomes. I also think it's very nice that the tools for converting these famous reference genomes is already in the package which one can download. I don't know how useful the segment_liftover tool will be for other species, since it does come with a large amount of exceptions and difficulties, it seems. If "unconvertible regions" are e.g. telomeres, centromeres, but also "gene-sparse locations", I ask myself the question if this will not be a problem in a lot of genomic material with which Biologists or whoever in the end will be working with. 
But considering that there already are different tools, and this tool is meant as a sort of addition with which one has less problems in the tedious task of constant switching from one reference to the other, I think it's very useful to provide this. I also saw that there were some useful comments for the article, so maybe in the end the package can be improved and improved. But still - very annoying that there are these different reference genomes etc. I hope that in the future this will not be such a problem anymore, since many will be working on the same reference genome!