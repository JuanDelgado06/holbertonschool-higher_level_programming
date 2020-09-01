#!/bin/bash
git add .
echo "Escribe  el mensaje de tu commit"
read MSG
git commit -m "$MSG"
git push origin master
git log -2
