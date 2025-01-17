# Cancer Genome Database Progenetix
## 1) What is CNV/CNA?
 * CNV: copy number variation
 * CNA: copy number aberration
 * CNV/CNA are structural genome variations that are more frequent in cancers cells and are used to characterize different molecular subtypes of cancers.
 
## 2) How would you describe or introduce progenetix?
Progenetix is a free resource that is accessible by the public. Its goal is to collect different all different cancer profiles.
* scale: 138'663 (of which 115'357 tumor) CNV profiles
* data source: publications based on molecular cytogenetics and sequencing (collecting data from all different kinds of methods)
ArrayExpresss (4351 samples), cBioPortal (19'712 samples), TCGA (22'142 samples), GEO (63'568 samples)
* cancer types: Spanning all cancer types, e.g. breast, brain, liver, stomach, skin, kidney, ovary, prostate gland, esophagus, pancreas, heart, spleen, bones. 
* which information does the database provide: CNA profiles and their metadata, further services to work with the data, phenotypic information on the profiles

## 3) Describe NCIt, UBERON codes, and their relationships.
* National Cancer Institute Thesaurus: describes different cancer types. It is a hierarchical ontology that is developed dynamically.
* UBERON: An ontology system based on cross-species anatomical structures. It allows queries that link different databases, link different organs within the same organism and between model animals and humans. 
* Progenetix connects ICD-O T (International Classification of Diseases in Oncology) codes to UBERON terms. This means we can make connections between cancer type and phenotype in different organisms and of different organs within one organism. We get a link to the UBERON-code site and can see where the body part is from that we our queried CNV is from.

## 4) What are CNV segmentations and CNV frequencies, and how to use them?
CNV frequencies tell us how frequent the alleles with the queried CNA are. This is a proxy for the frequency of a cancer type in the population. 

## 5) What are APIs and how to use APIs in progenetix?
* Application programming interface (GA4GH Beacon)
* This is the interface that allows the users to give in queries and extract data. The user can enter start and end position range, filter for cancer type, location in the tissue, morphology, cell line or geographic location. 

## 6) How does progenetix visualize CNA profiles?
The user can customize the visualization of the CNA profile e.g. for specific chromosomal regions or according to studies.
The output visualization is structured followingly:
* Genome-wide CNA with the percentage of samples that have more CNs vs those that have fewer.
* There is a table with the subsets using the definitions of ICD-O-3 and NCIt Ontology terms. 
* Biosamples tab: Displays the information of all biosamples that matched the query. Description, classification, external identifiers. 
* Biosamples Map: map of the world with the geographical locations of the matched biosamples
* variants tab: summarized format of the chromosome with its start and end position

## 7) What do you think should be improved in progenetix?
It would be useful to have more general information on the different functions and possibilites for people that do not have a large expertise in the field and want to get an overview. An example query with interpretation of the results would be nice.
