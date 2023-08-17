from pathlib import Path

vault = Path(".")

for file in vault.rglob("*"):
    for c in ["á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú", "ñ", "Ñ"]:
        if c in str(file):
            print(file)
