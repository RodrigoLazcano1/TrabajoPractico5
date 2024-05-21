#!/bin/bash

read $1
echo "Presione Enter para ejecutar el contador"

# Ejecutar el contador con bucle for en Python
python contador1.py "$1" &
python contador2.py "$1" &
python contador3.py "$1" &
