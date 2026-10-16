# Consigne pour la session Claude sur le PC — remplir la FCI KHAZNA

**Fichier à remplir (déjà dupliqué du modèle Commerce, macros conservées) :**
`02-Commerce/Propositions commercial/EXYTE/Data Center KHAZNA/Elec base vie/Dossier réponse/Chiffrage/FCI_EXYTE_KHAZNA_ORY01_CFA.xlsm`
(copie de `02-Commerce/Propositions commercial/FCI_CLIENT_PROJET_LOT_v2.xlsm`)

**Données à reporter :** onglet `DPGF` du fichier
`livrables/KHAZNA/Chiffrage/FCI_EXYTE_KHAZNA_ORY01_CFA_v2.xlsx` (GitHub Wseale842/Claude-, branche `claude/busy-volta-ah6fib`).
Ce .xlsx a la même structure que le modèle PROSYB (mêmes onglets et colonnes) : lignes 17 à 118 = objet, 8 chapitres (lots 4 à 7 par phase, SSI, vidéo, GTB AETHERYS), totaux, nota.

**À faire dans Excel, en gardant le .xlsm (macros) :**
1. Ouvrir les deux fichiers.
2. Dans `FCI_EXYTE_KHAZNA_ORY01_CFA.xlsm`, onglet DPGF : reporter pour chaque ligne les colonnes A (réf.), B (désignation DPGF), C (lot), D (famille), E (constructeur), F (référence), G (description / source fournisseur), H (unité), I (quantité), J (PRU matériel), L (h monteur), N (h technicien), P (h BE). Ne pas écraser les formules des colonnes K, M, O, Q à AB : les recopier depuis une ligne article du modèle.
3. Reprendre les titres de chapitres, sous-totaux, total HT / TVA / TTC et le nota (B119).
4. Page de garde / Recap_FCI : client EXYTE, affaire « KHAZNA ORY01 — Base vie & chantier — Lot courants faibles », site Fouju (77), N° d'offre et date.
5. Contrôle : total HT attendu ≈ 464 670 € (coefficients du Recap_FCI du modèle) ; lot GTB ≈ 47 304 €.
6. Enregistrer, sans écraser le modèle de base.

**Rappel GTB (AETHERYS 16/10/2026, 28 714 € HT) :** WAGO PFC100 750-8112 + 2 × 750-1405 + 750-600 = 1 248 €/TGBT ; alim 787-1212 78 € ; poste HP + 2 écrans 1 664 € ; études / dév. / MES / DOE / formation / licence Ignition Edge / IXON 5G / abonnement / TMA = 23 072 € + provision 870 € (prolongation à 29 mois).
