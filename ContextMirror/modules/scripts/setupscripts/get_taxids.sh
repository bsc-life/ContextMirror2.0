#!/bin/bash

#1. instalamos taxonkit
#2. instalamos taxdump
#3. https://www.biostars.org/p/9521718/

target_tax=$1
currentdir="$PWD"

taxonkit list --ids 2 -I "" | taxonkit filter -E species -o bacteria_species.txt #quiero todos los taxids de bacteria (2), sin indentación (-I "") y que esté en el rango de speceies (-E species)
#ahora ya tenemo stodos los taxID de las bacterias (nivel especie) --> excluimos las cepas

bash $currentdir/../ContextMirror/modules/scripts/setupscripts/get_species_taxids.sh -t $target_tax > target.txids #esto se descarga todos los tax ids de E. coli
#ahora tenemos que descargarnos ltodos los tax ids de la especie que nos interesa, en este caso E. coli (sería interesante que el taxid sea un argumento)

awk 'NR==FNR{a[$0]=1;next}!a[$0]' target.txids bacteria_species.txt > bacteria_species_no_strains_no_target.txids
#ahora hemos restado los de la especie que estudiamos (E. coli) del total, de manera que cuando busque E. coli contra la bbdd no se encontrará a sí misma porque la especie que estudio ya no está en la bbdd
