#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------1---------2---------3---------4---------5---------6---------7---------8
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Name    : INI-03_Fonctions-01a.py
Author  : Vitor COVAL
Date    : 2024.12.16
Version : 0.01
Purpose : Programme qu'affiche le nom de l'utilisateur.

# ------------------------------------------------------------------------------
# Revisions
# ------------------------------------------------------------------------------

# 2024-12-21 01 VCL
  - Version initiale
"""


# Définition d'une fonction qui dit bonjour à une personne dont le nom
# est le premier argument
def fonction_dit_bonjour(arg_nom):
    print("Bonjour", arg_nom)


# ------------
# --- Main ---
# ------------

# Demande du nom de la première personne
nom = input ("Quel est votre nom ? ")
noms = {1:nom}
# Demande du nom de la deuxième personne
nom = input ("Quel est le nom de la personne à votre gauche ? ")
noms[2] = nom
# Demande du nom de la troisième personne
nom = input ("Quel est le nom de la personne à votre droite ? ")
noms[3] = nom

# Affiche tous les noms
print("A qui je dois dire bonjour")
for id in noms.keys():
    print (id, "-", noms[id])

choix = input("Choisissez un numéro (1, 2 ou 3) pour dire bonjour à la personne : ")

choix = int(choix)

# Dis bonjour à la personne choisie
fonction_dit_bonjour(noms[choix])
