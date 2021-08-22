# PYTHON_SCRIPTS
2020 - 2021 Développement Informatique II (T201)

![Image de l'ephec](https://i.imgur.com/k1pB47i.png?1)

## Présentation

Je suis élève en 2TL1 à l'EPHEC

[DAXHELET Nicolas](https://github.com/nicodax) (HE201753)

## Description

Ceci est le repository contenant les scripts Python pour l'évaluation "0.2-base - Ecrire un script en Python"

[Lien vers TLCA](https://www.tlca.eu/dashboard/courses/T201/competencies/5f67c0b191429e08ff4c5962)

### JXCEL

Ce script permet de créer un fichier excel (.xlsx) à partir d'un fichier JSON (.json)

### RANDOM_PWD_GENERATOR

Ce script permet de générer un mot de passe aléatoire de 12 caractères contenant entre 3 et 5 chiffres, et entre 3 et 5 caractères spéciaux. Le reste des caractères est formé à partir de lettres majuscules et minuscules.

## Personalisation

### JXCEL

Modifier les lignes suivantes pour adapter le nom du fichier JSON à adapter en fichier .xlsx

```python
...

# JSON file name conventions
json_file_number = 3
json_file_name = "file" + str(json_file_number)

...
```

Par exemple :

```python
...

# JSON file name conventions
json_file_name = "monFichier"

...
```

Attention, ne pas ajouter l'extension du fichier (.json). Celle-ci est ajoutée automatiquement lors de l'importation.

### RANDOM_PASSWORD_GENERATOR

Modifier la longueur du mot de passe à générer (pwdLength), le nombre de chiffres (ranDig) et le nombre de caractères spéciaux (ranPunct).

```python
...

# Set password variables (length, number of digits and number of special characters)
pwdLength = 12
ranDig = random.randint(3,5)
ranPunct = random.randint(3,5)

...
```