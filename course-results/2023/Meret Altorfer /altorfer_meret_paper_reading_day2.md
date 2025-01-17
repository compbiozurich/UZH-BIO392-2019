# Paper Reading: Progenetix
## What is CNV/CNA?
- **copy number aberrations (CNAs)**: 
Structural genome aberrations which are present in the majority of cancer types and have a functional impact in cancer   development. So CNAs typically refer to copy number changes (deletion or insertions of large genomic regions) that are considered abnormal or aberrant and are often associated with cancer.
- **copy number variation (CNV)**:
CNVs refer to structural variations in the DNA of an organism where a segment of the genome has been duplicated (gained) or deleted (lost) compared to a reference genome with normal genomic content.

## How will you describe or introduce progenetix (scale, datasource, cancer types and so on)
Progenetix is a open accessible cancer genome data resource, that has the goal to provide a representation of genomic variation in cancer. The data is produced by a variety of oncogenomic studies which have  derived the data from genomic arrays and chromosomal Comparative Genomic Hybridization (CGH) as well as Whole Genome or Whole Exome Sequencing (WGS, WES). Leading to a cancer genome CNA database with more than 138663 profiles including 115357 tumor copy number variation profiles. The Progenetix database specializes in cataloging CNVs. Users can search for specific genes, genomic regions, or cancer types to access relevant data and studies within the Progenetix database.Furthermore, it offers tools for visualizing and analyzing the CNV data. For example it is possible to visualize cancer samples (of a distinct cancer type) and their chromosomal regions with their copy number gains (yellow) and copy number deletions (blue). 




## Describe NCIt, ICOD, UBERON codes, and thier relationships.
- **National Cancer Institute Thesaurus (NCIt)**: is a dynamically developed hierarchical ontology, which enables layered data aggregation and transfer between classification systems and resources. In Progenetix the different cancer sample profiles are accessible with their NCIt code. 
  
- **International Classification of Diseases in Oncology (ICD-O)**: The ICD-O topography system offers a mapping of organ-specific and substructure specific locations, drawing from the traditional clinical and diagnostic aspects associated with a tumor entity. However, the current ICD-O is limited in its representation of hierarchical concepts and does not easily translate to modern ontologies.

- **UBERON**:  cross-species anatomical structural ontology system, linked to developmental processes, enables integrated queries connecting databases across model animals and humans.



## What are CNV segmentations and CNV frequencies, and how to use them?
- **CNV segmentation**: CNV segmentations refer to the division of a genome into segments based on copy number variations. It is used to identify genomic regions that exhibit alterations in copy numbers (compared to a reference genome).
- **CNV frequencies**: Occurence (frequency) of specific CNVs within a population or a collection of samples. It quantifies how often a particular CNV is observed in a group of samples. Can be used to determine if a CNV is frequent or rather rare. 




## What are APIs and how to use APIs in progenetix?
- API stands for Application Programming Interface. It is a set of rules and protocols that allows different software applications to communicate and interact with each other, enabling them to share data and functionality. In the context of databases it  provides a way for developers to send queries, retrieve data, and perform various database operations programmatically [Wikipedia](https://en.wikipedia.org/wiki/API)
- Beacon application programming interface (API) is  used in Progenetix. The query interface for retrieving sample-specific data within Progenetix is  enabeld by the GA4 Beacon API, incorporating features from the upcoming version 2 of this standard. It is used to perform a CNA query with start and end position and filter options for cancer type, tissue location, morphology, cell line or geographic location.

## How does progenetix visualise CNA profiles?
**Chromosome CNA visualisation**: This visualization shows the distribution of CNAs across different chromosomes. Amplifications and deletions are usually represented using different colors eg. yellow and blue. And there is also the option to zoom in on certain chromosomes for viszualizing CNAs at a specific chromosomal location (e.g. q and p arms)
<img width="982" alt="Bildschirmfoto 2023-10-09 um 15 50 49" src="https://github.com/compbiozurich/UZH-BIO392/assets/145456627/0fde5d41-1001-4764-add1-598194ba0477">

## What do you think should be improved in progenetix?
- Generally to make the interface more userfriendly, it would be useful to have tutorial how to use the website (for example with videos). The [Info Progenetix] (https://info.progenetix.org) is helpful but not that understandable and detailed for new users.
- Ensure that there is as much as possible data available.



