# Subset of proteins to test the functionality of ContextMirror2.0 pipeline. These proteins correspond to two different protein complexes.

## Murein (mur ligases)

- **NP_414632.1**: N-acetylglucosaminyl transferase - **murG**  
- **NP_414627.1**: UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase - **murE**  
- **NP_418403.1**: UDP-N-acetylenolpyruvoylglucosamine reductase - **murB**  
- **NP_414633.1**: UDP-N-acetylmuramate--L-alanine ligase - **murC**  
- **NP_414630.1**: UDP-N-acetylmuramoyl-L-alanine--D-glutamate ligase - **murD**  
- **NP_414628.1**: D-alanyl-D-alanine-adding enzyme - **murF**  
- **NP_417656.1**: UDP-N-acetylglucosamine 1-carboxyvinyltransferase - **murA**

## Respiratory complex I
- **NP_416780.1**: NADH:quinone oxidoreductase subunit M - **nuoM**  
- **NP_416788.1**: NADH:quinone oxidoreductase subunit E - **nuoE**  
- **NP_416785.1**: NADH:quinone oxidoreductase subunit H - **nuoH**  
- **NP_416784.1**: NADH:quinone oxidoreductase subunit I - **nuoI**  
- **NP_416782.1**: NADH:quinone oxidoreductase subunit K - **nuoK**  
- **NP_416791.3**: NADH:quinone oxidoreductase subunit A - **nuoA**  
- **NP_416779.2**: NADH:quinone oxidoreductase subunit N - **nuoN**  
- **NP_416786.4**: NADH:quinone oxidoreductase subunit G - **nuoG**  
- **NP_416783.1**: NADH:quinone oxidoreductase subunit J - **nuoJ**  
- **NP_416787.1**: NADH:quinone oxidoreductase subunit F - **nuoF**  
- **NP_416781.1**: NADH:quinone oxidoreductase subunit L - **nuoL**

Follow the steps outlined in the README.md file to run ContextMirror2.0 on the subset of proteins we selected for you. After installing all the required packages and tools, this task should take approximately 2–3 hours, depending on the strictness of the parameters specified in the config.ini file. For example, setting lower common species thresholds will result in more pairs to evaluate, which increases computing time.

The results for this example are provided in the test_results.zip file. You can analyze the info_df.csv dataframe and split it into communities using the included Jupyter notebook (test_results_analysis.ipynb). From the initial set of 18 proteins, ContextMirror2.0 identified functional communities. Note that the performance of this software improves with a larger initial set of proteins, as it provides a more comprehensive context for protein coevolution. Therefore, the presence or absence of additional proteins in the initial set can significantly impact interaction predictions. To enhance the robustness of your predictions, consider including more information in your initial multifasta file.


<div style="display: flex; justify-content: space-around; align-items: center;">
  <img src="https://github.com/user-attachments/assets/544879d1-f09f-4983-a25b-8037c1309b4b" alt="Image 1" style="width: 30%; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/c04f6d40-d69f-41ad-8c28-66bb4f21e183" alt="Image 2" style="width: 30%; margin-right: 10px;">
  <img src="https://github.com/user-attachments/assets/4d471faf-8fb3-4acc-a58d-2223dc3ac9da" alt="Image 3" style="width: 30%;">
</div>



