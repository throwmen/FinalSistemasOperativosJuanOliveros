#!/bin/bash

# Define el directorio donde están los archivos JSON
JSON_DIR="./user_data"

# Define el bucket de S3
BUCKET="s3://jdo-so-ueia-2024"

# Subir los archivos JSON al bucket
aws s3 cp "$JSON_DIR" "$BUCKET" --recursive --exclude "*" --include "*.json"

# Eliminar los archivos JSON locales después de la carga
rm "$JSON_DIR"/*.json
