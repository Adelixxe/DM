# =============================================================================
#                                DM INFO 15/03
# VOLKAERT Thomas 
# =============================================================================

# =============================================================================
#                                   Import
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                                 Exercice 1 
# =============================================================================

#Question 1:
def f_parite(mot):
    S=0
    for elt in range(len(mot)):
        S+=mot[elt]
    if S%2 == 0:
        return 0
    else:
        return 1

#Question 2:
def f_encode_mot_4b(mot):
    p1=f_parite([mot[0],mot[1],mot[3]])
    p2=f_parite([mot[0],mot[2],mot[3]])
    p3=f_parite([mot[1],mot[2],mot[3]])
    return([p1,p2,mot[0],p3,mot[1],mot[2],mot[3]])

#Question 3:
def f_corrige_message_7b(message):
    p1,p2,d1,p3,d2,d3,d4 = message
    s1= p1+d1+d2+d4
    s2= p2+d1+d3+d4
    s3= p3+d2+d3+d4
    sprime = [s3%2,s2%2,s1%2]
    i=(s3%2)*2**2 + (s2%2)*2 + s1%2
    ind=(i-1)
    for k in range(len(sprime)):
        if sprime[k] != 0:
            message[ind]=(message[ind]+1)%2
    return message

#Question 4:
def f_decode_message_7b(message):
    p1,p2,d1,p3,d2,d3,d4 = message
    return([d1,d2,d3,d4])

#Question 5:
def f_bin_8b_to_lettre(lettre_binaire_8b):
    S=""
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for k in lettre_binaire_8b:
        S+=str(k)
    return alphabet[int(S,2)%26]

#Question 6:
def f_decode_texte_2x4b(texte_binaire_2x4b):
    return None

#Question 7:
def f_trancode_texte_7b_to_4b(texte_binaire_7b):
    return None

#Question 8:
def f_corrige_texte_7b(texte_binaire_7b):
    return None

# =============================================================================
#                                  Exercice 2
# =============================================================================

#Question 1:
def message_ini(code):
    return None