"""
Programa: Final
Descrição: Este programa organiza arquivos em pastas de acordo com sua extensão.
Autor: Mayara Binsfeld
Data: 27/03/2025
Versão: 0.0.1

"""

import os
import shutil

# Arquivos
arquivos = [
    "orcamento.xls",
    "orcamento.docx",
    "clientes.xls",
    "clientes.doc",
    "relatorio.doc"
]

# Pastas de destino
pastas = {
    "xls": "planilhas",
    "docx": "documentos",
    "doc": "documentos"
}

# Criar pastas
for pasta in pastas.values():
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Mover arquivos
for arquivo in arquivos:
    extensao = arquivo.split(".")[-1]  # Obtém a extensão do arquivo
    if extensao in pastas:
        shutil.move(arquivo, os.path.join(pastas[extensao], arquivo))

print("Arquivos organizados.")
