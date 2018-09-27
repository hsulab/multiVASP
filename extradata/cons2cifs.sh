#!/bin/bash
###
ms_dir=${HOME}/Documents/USRP/DopRutile_Files/Documents
###
for cif in ` ls ./ts_data/ts_cifs`
do
    cp ${con}.cif ./ts_data/ts_cifs
    mv ${con}.cif $ms_dir/ts_cifs      
done
