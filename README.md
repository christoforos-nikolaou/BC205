# BC205

## Algorithms in Bioinformatics - MSc in Bioinformatics - University of Crete

This is the git repository on the Course on Algorithms in Bioinformatics (BC205) which forms part of the Program of the Masters in Bionformatics at the University of Crete

**Contact Details**  
*Christoforos Nikolaou: cnikolaou@fleming.gr*  
*web: https://computational-genomics.weebly.com/*

## 2025-2026 Academic Year (March-June 2026)

Welcome to the course on Algorithms in Bioinformatics (BC205) for the 2025-2026 academic year. The course will run from March to June 2026.

This year we will attempt to use a more interactive format for the lectures, with a focus on problem-solving and hands-on exercises. We will cover a range of topics in bioinformatics, focusing primarily on sequence analysis algorithms, but also touching on other areas such as comparative genomics and gene regulation.

The goal is to make the class more interactive and engaging, but also to provide the framework of something that has been missing from the program, which is reading scientific papers, understanding how we formulate research questions and then how we may implement algorithms to answer them.

In this way, we will be centering the course around a set of papers that we will read and discuss in class, and then we will implement the algorithms described in those papers.

### March 19th, 2026: Discussion on Projects, Preliminary Journal Club

In this class we will begin discussing suggested projects. Below, I am providing a list of papers, which may serve as fine starting points for the development of projects.

* Gene Regulation: [Boija et al, Cell, 2018. "Transcription Factors Activate Genes through the Phase-Separation Capacity of Their Activation Domains"](https://www.sciencedirect.com/science/article/pii/S0092867418313989?via%3Dihub)
* Genome Organization and Oncogenesis: [Flavahan et al., Nature, 2016. "Insulator dysfunction and oncogene activation in IDH mutant gliomas"](https://www.nature.com/articles/nature16490)
* Evolution of Gene Regulation: [Ali Sharifi-Zarchi et al., BMC Genomics, 2017. "DNA methylation regulates discrimination of enhancers from promoters through a H3K4me1-H3K4me3 seesaw mechanism"](https://link.springer.com/article/10.1186/s12864-017-4353-7)
* Genome Organization and Splicing: [Tammer et al., Molecular Cell, 2022. "Gene architecture directs splicing outcome in separate nuclear spatial regions"](https://www.sciencedirect.com/science/article/pii/S109727652200106X?via%3Dihub)
* Alternative Splicing Regulation: [Georgakopoulos-Soares et al., Nature Communications, 2022. "Alternative splicing modulation by G-quadruplexes"](https://www.nature.com/articles/s41467-022-30071-7)
* Transcriptional Elongation and Senensence[Debes, Papadakis et al., Nature, 2023. "Ageing-associated changes in transcriptional elongation influence longevity"](https://www.nature.com/articles/s41586-023-05922-y)
* Complexity of Eukaryotic Gene Regulation: [Fromel et al., Cell, 2025. "Design principles of cell-state-specific enhancers in hematopoiesis"](https://www.cell.com/cell/fulltext/S0092-8674(25)00449-0?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867425004490%3Fshowall%3Dtrue)
* Transcriptional Noise as a modulator of cell development: [Garcia-Blay et al., Developmental Cell, 2025. "Multimodal screen identifies noise-regulatory proteins"](https://www.cell.com/developmental-cell/fulltext/S1534-5807(24)00543-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1534580724005434%3Fshowall%3Dtrue)
* De novo gene birth in fungi: [Tassios et al., Molecular Biology and Evolution, 2021. "Intergenic Regions of Saccharomycotina Yeasts are Enriched in Potential to Encode Transmembrane Domains"](https://academic.oup.com/mbe/article/40/3/msad059/7077448)

### March 26th, 2026: Introductory Journal Club - Assignment of Projects

---

* **Athina Marougka**: Transcription Factor Rewiring in Human Accelerated Regions (HARs). (Next Time)

   * The main goal: Identify changes in Transcription Factor Binding Sites in human HARs
   * Questions:
      1. How to define HARs? How many are there? Where are they enriched in the genome (coding sequences) (next time)
      2. How to search for TFBS? Which database of PWMs will be used? How will the search be done?
      3. How will the "rewiring" be assessed? How will changes be identified/quantified?
---

* **Despina Georgiadou** : Noise in Gene Regulation: An underlying Mechanism in Cell Fate Determination ([Hansen paper](https://www.cell.com/developmental-cell/fulltext/S1534-5807(24)00543-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1534580724005434%3Fshowall%3Dtrue)) (Next Time)

   * The main goal: Relate intron size among SON targets and transcriptional noise. How does the gene structure make some genes more prone for transcriptional noise (enhancement or not)
   * Questions:
      1. How to calculate the K-ON/K-OFF from the data of Garcia-Bay et al.? (next time)
      2. Explain the two-state random telegraph model in greater detail.
      3. Is it only SON targets that show this link between intron size and transcriptional noise? 
      4. SON is a Nuclear Speckle Protein. Introns are key structural determinants of mRNA splicing. What could be the link between splicing and transcriptional noise?
---

* **Panagiota Meramveliotaki**: eQTL mapping to predict pharmacogenomics response

   * The main goal: Identify eQTLs that can be responsible for pharmacogenomics responses
   * Questions:
      1. eQTLs. How are they defined/calculated? How can we re-define them in new RNASeq data?
      2. How can we integrate the data from GTEx into the framework presented by the GEUVADIS study? (next time)

---

* **Lambros Dousias**: mRNA folding and transcriptional optimization 

   * The main goal: mRNA folding for optimal expression
   * Questions:
      1. What do we know on mRNA folding in general? How are mRNA molecules folded?
      2. What is the connection between mRNA and Codon Usage?
      3. How is MFE calculated? Description of the linearDesign algorithm. (Next Time)
      4. How is CAI calculated? (Next Time)
---

* **Ioanna Xenaki**: How Ghost lineages influence Introgression (Next Time) (also have a one-on-one) (next time)

   * The main goal:
   * Questions:
      1. What is the D-statistic (ABBA-BABA test)? How is it

---

* __Petros Kogios__: Machine Learning and Synthetic Enhancer Design in Gene Regulation ([Veltens paper](https://www.cell.com/cell/fulltext/S0092-8674(25)00449-0?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867425004490%3Fshowall%3Dtrue))

   * Papers: Fromel et al; DeepSTAR; Cell-type specific enhancers in Glial Cells in Drosophila
   * The main goal: Test the results of the Fromel et al paper against available gene expression dataset.
   * Questions:
      1. This is a very complex paper. Start by reading it carefully and outline main findings. 
      2. Could the results of Fromel et al. be validated in natural sequences? One could approach this by getting a gene expression profile of hematopoiesis (or perhaps even the one produced by Fromer et al.) and then check the gene expression of genes regulated by the combinations of TFs they are identifying. (Possible links with the Project of Athina in the search of TFBS).  
---

* **Eleftheria Pappa**: Integrating DNA methylation and gene expression data in a single gene network using the iNETgrate package (next time)

   * The main goal: Present a graph-based approach to integrate multiple modalities, focused on gene expression and DNA methylation
   * Papers:
   * Algorithms: Community Detection in Networks, Matrix Decomposition
   * Questions:
      1. How does iNETgrate actually work? Show a demo of the package and discuss the types of input/output. (next time)
---

* **Stergios Manakas**: Prediction of Splicing Outcomes based on the gene structure

   * The main goal: A Supervised ML pipeline to combine PSI values and gene structure features to improve the PSI prediction.
   * Questions:
      1. Which tools do you plan to use to calculate PSI? Where will you get the PSI values?
      2. Can we include splicing enhancers/silencers in the model? 
---

* **Vasilis Karouanas**: Transcriptional Elongation ([Papantonis & Beyer paper](https://www.nature.com/articles/s41586-023-05922-y))

   * The main goal: Investigate the properties that are associated with transcriptional elongation rate. Estimate the biological age of a given cell.
   * Questions:
      1. Explore the connection between chromatin structure, gene structure and elongation speed. We have a framework in the lab that you may use. 
      2. Note: Transcriptional elongation speed is **not connected** with noise. (Noise is a way for the cell to explore the gene expression space and assume new identities. Elongation speed is probably linked with a deterioration of chromatin structure.)
---

### April 2nd, 2026: Follow up and Consolidation of Projects. 

To present updates:

* **Ioanna Xenaki**
* **Athina Marouga**  
* **Despina Georgiadou**
* **Panagiota Meramveliotaki**  
* **Lambros Dousias**
* **Eleftheria Pappa**

