#########################################################################
# File Name: CountData.sh
# Author: jyxu
# mail: ahcigar@foxmail.com
# Created Time: 四  9/27 10:43:00 2018
#########################################################################
#!/bin/bash
path=$(pwd)
echo $path
metals=('Ge' 'Ir' 'Mo' 'Os' 'Ru' 'Rh' 'Ti' 'V')
rtype=('suf' 'CH3ab' 'Hab2' 'Hab3' 'ts' 'tsra' 'fs' 'fsra')
for dir in `ls .`
do
    if [ -d $dir ]
    then
        for r in ${rtype[@]}
        do
            cons="./${dir}/${r}_cons"
            if [ -d ${cons} ]
            then
                echo "`ls ${cons} | wc -l`   \c"
                echo "${cons}"
            fi
        done
    fi
done
