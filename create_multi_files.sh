#!/bin/bash
echo "Cual es el nombre ?"
read NAME
echo "Cual es la extencion ?"
read EXT
for i in {1..5}
do
    touch 104-$NAME$i.$EXT
    echo "Se creo $i-$NAME.$EXT"
done