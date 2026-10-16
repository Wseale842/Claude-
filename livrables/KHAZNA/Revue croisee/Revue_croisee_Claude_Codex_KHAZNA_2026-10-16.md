# KHAZNA ORY01 — Revue croisée Claude × Codex — 16/10/2026

Mémoire v1.3 → v1.4, FCI v1 → v2 (mise à jour GTB AETHERYS). Deux relecteurs indépendants (Claude, Codex/GPT), puis un second tour où chacun a challengé l'autre. Les revues complètes sont jointes (REVUE_codex.md, REVUE_FCI_codex.md, REPLIQUE_codex.md, REVUE_claude.md).

## Appliqué au mémoire v1.4
| # | Correction | Source |
|---|---|---|
| 1 | **Nouveau chapitre 8 « Sécurité incendie »** (lot 5 DPGF chiffré mais absent du mémoire) ; § 13 ne déclare plus le SSI hors prestation | Claude + Codex |
| 2 | **Chapitre GTB réécrit sur l'offre AETHERYS** : WAGO PFC100 750-8112 + DI16 750-1405, Ignition Edge + OPALE, archivage, alertes, IXON 5G en VLAN 910, déroulement études → DOE | Claude + Codex |
| 3 | Détection vidéo **ramenée à ce que font les caméras chiffrées** (détection de mouvement 2.0 humain/véhicule par zones sur 28 voies + AcuSense NVR sur 2 vues) ; franchissement de ligne natif et **EPI en options** | Codex (constat) / Claude (arbitrage : corriger sans aveu de doute) |
| 4 | Stockage **2 × 10 To** au lieu d'un disque de 20 To (limite 16 To par baie du NVR), 15 j à 3,5 Mbit/s | Claude + Codex |
| 5 | SLA défini : heures calendaires, point de départ, disponibilité ≥ 99 % par service sur trimestre glissant | Codex, ajusté au 2ᵉ tour |
| 6 | Cohérences : switch L3 (SFP et non PoE), F/FTP vs F/STP, fibre Corning retirée, switch L3 de secours en option, micro caméras désactivé (RGPD), « un mois recommandé par la CNIL », compatibilité chariot 86" et totem OHDX validée avant commande, durées 29 mois de chantier / 28 mois d'exploitation | Claude + Codex |
| 7 | Questions ajoutées : switchs « incluant switch PoE » (hypothèse EXYTE), Est 3 / Ouest 3 sur la boucle fibre, PTZ / barrières IR, SMS GTB | Codex |
| 8 | Chapitres renumérotés 9 à 14, sommaire et renvois mis à jour | — |

## Appliqué à la FCI
- **FCI_EXYTE_KHAZNA_ORY01_CFA_v2.xlsx** (template PROSYB) : 7 lignes GTB sur l'offre AETHERYS (28 714 € HT, ventilation vérifiée par Codex sans oubli ni double compte), plus une provision de 870 € pour porter la TMA et la 5G de 24 à 29 mois. **Total : 464 670 € HT** (v1 : 432 244 €), dont GTB 47 304 €.
- FCI_Khazna_..._v6_AETHERYS.xlsx : version de travail indépendante (Détail, Récap, Points ouverts), 468 579 € HT, cohérente avec la v2.

## À décider par Woody (non appliqué)
1. **Coefficients** : k 1,4444 = 30,8 % de marge sur vente (et non 20 %). Codex propose : fourniture ×1,30, MO ×1,60, sous-traitance AETHERYS ×1,18 (GTB −4 à −7,6 k€).
2. **MO** : Codex juge l'hypothèse optimiste trop serrée (tirage cuivre 1,6 h/lien au lieu de 1,2 h, fibre 4 h/100 m, SSI 5 h/100 m, recettes) : **+33,7 k€ PR**.
3. **Postes absents de la FCI** : nacelle, certificateur, déplacements, encadrement, EXE.CFA, maintenance CFA 28 mois, astreinte, repli, aléas 3 %. Avec ces postes, le périmètre élargi atteint ≈ 648 k€ HT selon Codex.
4. **Permanence 24/7 (DPGF § 8)** : clarifier avec EXYTE qu'il s'agit d'une astreinte et non d'une présence sur site. Une présence physique est hors de prix et n'est pas incluse.

## Relances fournisseurs
- **AETHERYS** : prolongation TMA, CARE et 5G jusqu'à 29 mois ; connecteur 750-960 non chiffré ; libellés HUB 2/HUB 3 ; SMS.
- **CCF** : disques 2 × 10 To compatibles ; variante caméras AcuSense franchissement de ligne ; solution EPI en option.
- **Sonepar AV** : 4 Rally Mic Pod au lieu du MeetUp, totems pour OHDX, serveur et licences Navori.
- **Octet Plus** : devis révisé sans coffrets IP55.
- **Tous** : validité des prix ≥ 90 jours (exigence Haskoning), les devis actuels expirant les 27-31/10.

## Pièces encore à produire pour l'offre
Matrice C/D/E clause par clause, version EN, BPU vidéo (PTZ, barrière IR, déplacement de caméra, option EPI), N° d'offre et date sur la page de garde, références data center et CV.
