#!/bin/bash
echo "Nombre del Archivo"
read NF
touch $NF
BIN="#!/usr/bin/python3"
echo $BIN >> $NF
chmod u+x $NF
# nano $NF

