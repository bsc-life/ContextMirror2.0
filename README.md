# ContextMirror2.0 

ContextMirror2.0 is a tool designed to estimate pairwise coevolution of genes in a given proteome, described in described in https://doi.org/10.1101/2024.12.27.630483. This repository provides everything you need to run the pipeline locally, including configuration options for customizing your analysis.

Clone this repository to your local machine:

    git clone https://github.com/yourusername/ContextMirror2.0.git
    cd ContextMirror2.0

Make sure you have the required tools that will be needed for downstream analysis:

* BLAST+ suite ()
* MAFFT ()
* FastTree ()

BLAST: Version 2.13, used to search the NCBI database for potential orthologs. 

    sudo apt-get blast lo q sea

MAFFT: Version 7.471 for multiple sequence alignments (MSAs) with the following settings:

    sudo apt-get mafft lo q sea

Python: Version 3.6.1 with these dependencies:
    os, sys
    Bio v1.79 (modules: SeqIO, AlignIO, Phylo, ClustalWCommandline, DistanceTreeConstructor)
    numpy v1.21.5
    networkx v2.8.5
    requests v2.28.1
    pandas v1.4.3
    community v0.16
    scipy v1.8.1
    
FastTree: Version 2.1 for phylogenetic tree construction.

    sudo apt-get FAstTreee lo que sea
    
csvkit: Version 1.3.0 for handling CSV files.

    sudo apt-get csvkit lo q sea
    
Install the ContextMirror2.0 package:

    pip isntall .

Within the ContextMirror2.0 folder create a new directory to perform your analysis (e.g. results/). Inside this directory you should place:

* Config.ini file: Adjust the parameters in the config.ini file to match your dataset and analysis needs. Remember tospecify your input file path.

Open the config.ini file and modify the parameters as needed (e.g., file, tools and database paths, thresholds, ...). This pipeline runs locally, therefore, an appropiate BLAST+ database must be installed and formatted with taxonomic information. Here are some resources on how to build a custom databse with the BLAST+ suite. Consider disk space requirements before installing everything, these databases can be sizable. For bacterial analysis, my advice would be to go with the Refseq Select, a complete yet modestly sized database. For your convenience, the build_refseq_select_db.sh script will build it automatically for you.

You are good to go!

ContextMirro2.0 offers two modules:

    MirrorTree: the pipeline runs until the contruction of the tree-tree correlation matrix.
    
    ContextMirror: the pipeline runs the full ContextMirror pipeline.

For each protein in the input file, a Rreciprocal Best Hit will be performed, creating an individual directory for each of the cases (e.g. output_NP_414456.2/). Wihtin this folder, you will be able to access the homolog searches (both directions) and the orthologue search results. After that, a new directory will be created (tree_resuts/), were all possible pairs of porteins will be assessed and a subdirectory will be created (e.g. NP_414456.2_vs_NP_413258.1/) for each pair of proteins that share a orthologs in, at least, a number of species defined by the user in the config.ini file. Multiple Sequence Alignments (MSAs), phylogenetic trees, distance matrices and the correlation between them will be computed automatically and placed in a dataframe containing the tree-tree correlations (tree_results/tree_tree_matrix.csv).

Later, the correlation is recomputed by calculating the correlation between their coevolutionary profiles (one row of the tree_tree_matrix.csv). Several files (.pkl) will be created to store the correlation values between the coevolutionary profiles as well as the associated p-values for each possible pair. These correlations will then be gathered in a new dataframe (tree_results/profile_profile_matrix.csv).

Finally, a new matrix is created containing every possible combinations of significantly correlated protein pairs so far and every other third protein in the analysis, displaying the influence of every protein on every pair computed as the partial correlation coefficients (partial_matrix.csv).

The final output of the ContextMirror2.0 approach are these three matrices and the Jupyter Notebook dedicated to prodice analysis figures as described in the original publication is available:



