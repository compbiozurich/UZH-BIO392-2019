# Segment liftover
<br/>

> segment_liftover aims at continuity-preserving remapping of genome segments between assemblies.
<br/>

**Features** provided by segment liftover are the following:
*  approximate locus conversion
*  automated batch processing
*  comprehensive logging to facilitate processing of datasets containing large numbers of structural genome variation data


The process of assembling a species’ reference genome may be performed in a number of iterations, with subsequent genome assemblies differing in the coordinates of mapped elements.


However, when performing genome analyses integrating data from multiple resources, it is imperative to convert all data to the same genomic coordinate system.

This method, although bearing a side effect of minor information loss, for most applications provides a good balance between performance and accuracy.

All those tools are efficient in coordinate conversion and provide almost identical results. However, as shown in Figure 1a, challenges arise when dealing with genome segments that are not continuous anymore in the target assembly

In research such as analysis of copy number variation (CNV) data, where the quantitative representation of a genomic range takes precedence over base-specific representation, the integrity of a continuous segment indicates the proper conversion between assemblies, but may not be a direct outcome of current re-mapping approaches.