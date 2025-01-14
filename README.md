# ContextMirror2.0 

ContextMirror2.0 is a tool designed to estimate pairwise coevolution of genes in a given proteome, in described in https://doi.org/10.1101/2024.12.27.630483. This repository provides everything you need to run the pipeline locally, including configuration options for customizing your analysis.

Clone this repository to your local machine:

    git clone https://github.com/m-iguel/ContextMirror2.0.git
    cd ContextMirror2.0

- BLAST: Version 2.13 (https://blast.ncbi.nlm.nih.gov/doc/blast-help/downloadblastdata.html)
- MAFFT: Version 7.471 (https://mafft.cbrc.jp/alignment/software/source.html)
- FastTree: Version 2.1 (https://anaconda.org/bioconda/fasttree)
- csvkit: Version 1.3.0 (https://csvkit.readthedocs.io/en/0.9.1/install.html)

- Python: Version 3.6.1 (os, sys, Bio v1.79 (modules: SeqIO, AlignIO, Phylo, ClustalWCommandline, DistanceTreeConstructor),numpy v1.21.5, networkx v2.8.5, requests v2.28.1, pandas v1.4.3, community v0.16, scipy v1.8.1, pingouin v0.5.5)

Install the ContextMirror2.0 package:

    pip isntall .

Within the ContextMirror2.0 folder create a new directory to perform your analysis (e.g. results/). Inside this directory you should place:

* Config.ini file: Adjust the parameters in the config.ini file to match your dataset and analysis needs. Remember tospecify your input file path.

Open the config.ini file and modify the parameters as needed (e.g., file, tools and database paths, thresholds, ...). This pipeline runs locally, therefore, an appropiate BLAST+ database must be installed and formatted with taxonomic information. Here (https://www.ncbi.nlm.nih.gov/books/NBK569841/) are some resources on how to build a custom databse with the BLAST+ suite. Consider disk space requirements before installing everything, these databases can be sizable. For bacterial analysis, my advice would be to go with the Refseq Select, a comprehensive yet modestly sized database. For your convenience, the build_refseq_select_db.sh script will build it automatically for you.

You are good to go!

ContextMirro2.0 offers two modules:

    MirrorTree: the pipeline runs until the contruction of the tree-tree correlation matrix.
    
    ContextMirror: runs the full ContextMirror pipeline.

For each protein in the input file, a Rreciprocal Best Hit will be performed, creating an individual directory for each of the cases (e.g. output_NP_414456.2/). Wihtin this folder, you will be able to access the homolog searches (both directions) and the orthologue search results. After that, a new directory will be created (tree_resuts/), were all possible pairs of porteins will be assessed and a subdirectory will be created (e.g. NP_414456.2_vs_NP_413258.1/) for each pair of proteins that share a orthologs in, at least, a number of species defined by the user in the config.ini file. Multiple Sequence Alignments (MSAs), phylogenetic trees, distance matrices and the correlation between them will be computed automatically and placed in a dataframe containing the tree-tree correlations (tree_results/tree_tree_matrix.csv).

Later, the correlation is recomputed by calculating the correlation between their coevolutionary profiles (one row of the tree_tree_matrix.csv). Several files (.pkl) will be created to store the correlation values between the coevolutionary profiles as well as the associated p-values for each possible pair. These correlations will then be gathered in a new dataframe (tree_results/profile_profile_matrix.csv).

Finally, a new matrix is created containing every possible combinations of significantly correlated protein pairs so far and every other third protein in the analysis, displaying the influence of every protein on every pair computed as the partial correlation coefficients (df/partial_matrix.csv).

Finally, the predictions are processed and the final ranked list is produced (info_df.csv), gathering the following information:

- interactorA: proteinA
- interactorB: proteinB
- third_protein_info: list of lists with third profiles influencing the pair proteinA-proteinB -> [[proteinC, partial_correlation, p-value], [proteinC2, partial_correlation, p-value], ...]
- PPcorrelation: correlation between coevolutionary profiles of proteins A and B.
- third_proteins: list of third proteins significantly influencing the interaction between proteins A and B.
- third_proteins_len: number of third proteins significantly influencing the interaction between proteins A and B.
- av_partial: average partial correlation of third proteins significantly influencing the interaction between proteins A and B.
- interactor_pair: proteinA-proteinB (sorted alphabetically)
- combined_score: scores from Tree-Tree Matrix, Profile-Profile Matrix and Partial Matrix imputed.
- interaction_score: final interaction score calculated by correcting the combined_score.

The final output of the ContextMirror2.0 approach is this ranked list, alongside the three matrices and the Jupyter Notebook dedicated to prodice analysis figures as described in the original publication is available:



