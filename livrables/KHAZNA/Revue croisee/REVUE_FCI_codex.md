# Revue contradictoire de la FCI v6 — KHAZNA ORY01

Revue du 16 octobre 2026. Montants HT en euros. **La FCI v6 vaut 468 579,35 € sur les lots 4 à 7. La proposition à périmètre identique atteint 535 965,26 € ; le budget CFA élargi atteint 647 713,50 €**, avec les provisions détaillées ci-dessous. Ce dernier montant suppose une astreinte mutualisée, pas une présence permanente sur site. Les équipements AV à cinq micros et les fonctions vidéo/EPI restent à faire accepter/recoter : ce budget est une base de négociation, pas une offre techniquement démontrée conforme.

Sources lues : `BRIEF_codex.md`, `fci/lines.py`, `fci/build_fci_v6.py`, les cinq CSV recalculés séparés par `;`, `dpgf/DPGF_lots4-8_CFA.tsv` et, pour le repérage EXE, le DPGF complet. Les numéros ci-dessous désignent les **numéros physiques de ligne du TSV**, non une numérotation commerciale. Les devis originaux AETHERYS/Octet Plus/Sonepar ne sont pas dans les pièces lues : contrôle des ventilations transcrites, pas audit de leurs originaux.

## 1. Calculs, quantités et affectations

Les 60 lignes du dictionnaire sont présentes dans le détail CSV. Recalcul indépendant : MO = 40 M + 60 T + 62 S + 75 BE ; PR = achats + ajouts + MO ; PV/u arrondi au centime puis multiplié par la quantité DPGF. Aucune divergence de PR, quantité ou PV sur ces lignes en reprenant les coefficients effectivement stockés à six décimales. Le script écrit `round(K_STD, 6)` et `round(K_SSI, 6)` dans Paramètres : par rapport aux coefficients exacts, L33 perd 0,01 €/u × 6, L89 perd 0,02 €, et L4/L11/L34/L45/L53/L62/L78 perdent chacune 0,01 €, soit **0,15 € au total**. Le total avec coefficients exacts serait 468 579,50 €. Écart sans enjeu économique, mais conserver une seule convention de précision. Les totaux CSV FCI et récap concordent :

| Lot | PR actuel | PV actuel |
|---|---:|---:|
| 4 | 210 172,89 | 303 582,85 |
| 5 | 46 237,40 | 62 450,49 |
| 6 | 38 199,41 | 55 176,91 |
| 7 | 32 794,00 | 47 369,10 |
| **Total** | **327 403,70** | **468 579,35** |

Le script classe toutes les prestations AETHERYS, y compris études, développement et TMA, dans « Fournitures PR ». Le total reste juste mais cette présentation fausse la lecture achats/MO et empêche un coefficient par nature. Les 4 % sont une majoration de PR et les 8 % une quote-part du PV : `1,04/(1−20 %−8 %) = 1,444444…`. La marge brute PR/PV est donc 30,77 %, pas 20 % ; en SSI, 25,96 %, pas 15 %. Le bénéfice cible de 20 %/15 % n’est obtenu qu’après consommation effective des frais/aléas prévus.

### Ventilation exhaustive AETHERYS

| Ligne TSV | Affectation AETHERYS | PR/u | Quantité | PR total |
|---|---|---:|---:|---:|
| 83 | 949 contrôleur + 273 paire DI16 + 26 borne finale | 1 248,00 | 3 | 3 744,00 |
| 84 | Alimentation | 78,00 | 3 | 234,00 |
| 85 | Aucun achat AETHERYS ; liaison PROSYB | 0,00 | 3 | 0,00 |
| 86 | Aucun achat AETHERYS ; câblage TOR PROSYB | 0,00 | 3 | 0,00 |
| 87 | Aucun achat AETHERYS ; bus PROSYB | 0,00 | 3 | 0,00 |
| 88 | PC 1 430 + deux écrans 234 au total | 1 664,00 | 1 | 1 664,00 |
| 89 | Prestations, licences, routeur, abonnement, TMA | 23 072,00 | 1 | 23 072,00 |
| **Total devis** | | | | **28 714,00** |

L89 se reconstitue exactement : 3 240 études + 810 paramétrage + 6 480 développement + 3 240 MES/essais + 405 DOE + 405 formation + 3 413,80 Ignition/OPALE selon transcription + 902,20 routeur/antenne + 936 abonnement + 3 240 TMA = **23 072 €**. Ni oubli ni double compte des 28 714 € dans les données. Les 273 € sont le prix du lot de deux DI16, pas 273 € par module ; 234 € couvre les deux écrans, pas chacun. Ces interprétations sont indispensables à la concordance et à confirmer sur le devis signé. OPALE ne bénéficie pas d’une ventilation séparée vérifiable.

Le lot 7 ajoute 1 320 € d’achats PROSYB : 90 liaison Ethernet + 240 TOR + 120 RS485 + 870 prolongation, puis 2 760 € de MO ; soit **32 794 € PR**. Les 870 € ne font pas partie des 28 714 €. Ils couvrent cinq mois de 5G/TMA, **pas automatiquement le CARE Ignition**. Ne pas remettre les mêmes TMA/5G en maintenance §8. L’installation du PC étant AETHERYS, les 0,5 h PROSYB doivent rester une réception/assistance. Les 3 h automate sont une pose physique, distincte des quatre jours de MES AETHERYS ; faire signer cette limite.

### Anomalies et incohérences de périmètre

1. **Fibre L11 :** 3 728,57 + 6 × 561,06 = 7 094,93 €, contre 7 094,92 saisi : écart documentaire de 0,01 € PR, non significatif et non corrigé au tableau faute de devis original. Plus important : Est 3/Ouest 3 ne concordent pas entre boucle et coffrets ; faire valider le PIC et les six tronçons. Les liens 12 brins ne prouvent pas à eux seuls une topologie redondante : vérifier fibres, ports SFP et ERPS sur les switchs EXYTE.
2. **L14/L42 :** zéro acceptable si Octet Plus fournit réellement la réflectométrie demandée. Photométrie et réflectométrie sont deux essais différents ; exiger traces OTDR 1310/1550 nm, deux sens, bilan optique et PV. Ne pas acheter une seconde fusion/mesure ailleurs. Les douze forfaits de tronçons reconstitués (6 + 1 + 2 + 1 + 1 + 1) représentent 6 732,72 € mêlant tiroirs et prestations ; ne pas multiplier une seconde fois L29 par deux dans les achats.
3. **Cuivre et Wi-Fi :** 24 + 96 + 360 = 480 liens îlots ; +30 extérieurs +28 caméras = 538 certifications. Le bordereau dit « postes + bornes » : pas d’ajout automatique de 84 prises Wi-Fi. Confirmer les 84 bornes (4 + 20 + 60), dont 64 sans fourniture PROSYB. À 160 €/u, un transfert de ces 64 bornes ajouterait 10 240 € PR / 13 312 € PV selon la politique proposée. Ce risque n’est pas inclus en base. Les switchs EXYTE et coffrets SPIE doivent également être contractualisés ; aucun montant fiable pour les racheter n’est disponible.
4. **AV L18/L26 :** les sommes des composants 8 102,65 € sont justes ; 756 € ajoutés financent trois Mic Pods estimatifs, mais la ligne garde le micro MeetUp 252 €. Cela ne constitue pas quatre Mic Pods compatibles. Le bordereau exige cinq micros déportés. La Rally Bar est limitée à quatre Mic Pods selon [Logitech](https://futureisnow.logitech.com/content/dam/logitech/en_eu/video-collaboration/pdf/rallybar.pdf) : obtenir une dérogation à quatre ou une solution modulaire à cinq, avec recotation. Notre réserve nette 500 €/salle ne vaut pas démonstration du coût d’une solution à cinq. Confirmer le chariot pour 86 pouces et sa charge admissible. Les dix lecteurs AV + six lecteurs extérieurs = seize : le paramétrage L34 n’est pas surcompté.
5. **Affichage :** 4 852,81 €/écran et moyenne support 775 € sont arithmétiquement justes (3 × 250 + 3 × 1 300, sur six). L’adaptation du totem OH55F à OHDX, l’orientation, les ancrages et les licences Navori restent à prouver. Un serveur à 1 100 € ne prouve pas l’achat du logiciel serveur ni les droits pendant toute la durée.
6. **SSI :** cohérence des multiplications apparente, mais ni métrés ni architecture de report validés. Ne pas assimiler un contact d’alarme technique à un report SSI conforme. L59 achète douze CONCEPT 3 complets alors que la désignation demande des diffuseurs : valider compatibilité, synchronisation, déclenchement et audibilité avant de conserver ou remplacer ces 2 124 € ; aucune économie forfaitaire retenue. Câbles CR1 et coffret estimatifs, boîtes, traversées et protections à confirmer.
7. **Vidéo :** 28 caméras/mâts sont bien multipliés par 28 ; les huit switchs/alimentations et SFP sont déjà en L76, ne pas les remettre en L75. Les 28 massifs sont explicitement « LOT GC » L74 : conserver cette exclusion contractuelle. La nacelle EXYTE est une hypothèse non sécurisée. Le matériel actuel ne justifie pas l’analyse EPI/intrusion des 28 vues ; réserve dédiée, recotation impérative. Le disque 20 To doit être remplacé par une capacité validée pour la référence exacte : la [fiche Hikvision K4/16P(D)](https://www.hikvision.com/content/dam/hikvision/products/S000000001/S000000132/S000000007/S000000026/OFR031212/M000141857/Data_Sheet/Datasheet-of-DS-7732NXI-K4_16PD_20240523.pdf) annonce 16 To par baie. Deux disques ne créent pas automatiquement une redondance RAID. À 28 × 4 Mbit/s, 20 To bruts représentent environ 16,5 jours, avant réserve système ; fixer rétention, débit, écriture et mode dégradé.
8. **GTB :** environ 40 points Modbus RS485 ne signifient pas 40 appareils. Exiger nombre de compteurs, longueurs et schéma de bus avant de retenir 30 m. Réserver connectique/terminaisons et vérifier la référence série native du contrôleur ; ne pas ajouter arbitrairement un second module. Les doublons de libellé HUB 2/HUB 3 et « coupleur » doivent être corrigés par AETHERYS. Liste de points, OPALE, rétention énergie 24 mois/événements 45 jours, SMS et 2 clients simultanés à faire accepter.

## 2. Main-d’œuvre : avis ligne par ligne

Les heures sont des **heures-personnes par unité DPGF**, et non une durée d’équipe. M/T/S/BE = monteur/technicien CFA/technicien SSI/bureau d’études. Un ensemble de 360 prises porte toutes ses heures sur une seule unité. Ratios proposés de jugement de chantier, pas barèmes normatifs ni devis locaux : chemins accessibles, fourreaux principaux disponibles, travaux diurnes, consignations organisées. Les longueurs restent des hypothèses à mesurer. Des tranchées, chemins neufs ou délais d’accès importants imposeraient un recalcul. Les rapports locaux restent aux lignes ; EXE générale, encadrement et maintenance sont distincts.

| Ligne TSV | Qté | M/T/S/BE actuelles par u | M/T/S/BE proposées par u | Avis et ratio |
|---|---:|---|---|---|
| 4 | 1 | 0/5/0/0 | 2/4/0/0 | Baie lourde : manutention à deux, 2 h M + 4 h T ; configuration réseau en L13. |
| 5 | 1 | 0/5/0/0 | 2/4/0/0 | Même ratio baie ; switch fourni EXYTE à formaliser. |
| 6 | 1 | 0/2/0/0 | 0/2/0/0 | 2 h T conservées pour intégration coffret, hors configuration centrale. |
| 7 | 1 | 0/2/0/0 | 0/2/0/0 | 2 h T conservées pour intégration coffret, hors configuration centrale. |
| 8 | 1 | 0/2/0/0 | 0/2/0/0 | 2 h T conservées pour intégration coffret, hors configuration centrale. |
| 9 | 1 | 0/2/0/0 | 0/2/0/0 | 2 h T conservées pour intégration coffret, hors configuration centrale. |
| 10 | 1 | 0/2/0/0 | 0/2/0/0 | 2 h T conservées pour intégration coffret, hors configuration centrale. |
| 11 | 1 | 72.5/0/0/0 | 116/0/0/0 | 4 h-personnes/100 m × 2 900 m ; équipe de deux, déroulage et repérage, cheminement accessible. |
| 12 | 1 | 11.25/0/0/0 | 18/0/0/0 | 4 h/100 m × 450 m ; 2,5 h/100 m trop tendu pour chantier phasé. |
| 13 | 1 | 0/20/0/16 | 0/28/0/12 | 7 équipements × 3 h + 7 h de bascule/essais ; DOE local 12 h, architecture générale en EXE séparée. |
| 14 | 1 | 0/0/0/0 | 0/0/0/0 | Zéro MO PROSYB conservé si mesures contractuellement incluses Octet Plus ; contrôler réflectométrie et fichiers natifs. |
| 16 | 1 | 28.8/0/0/0 | 38.4/0/0/0 | 24 liens × 1,6 h, tirage 35 m, deux extrémités et repérage ; cheminements disponibles. |
| 17 | 4 | 0.75/0.25/0/0 | 0.75/0.5/0/0 | Pose 45 min + 30 min adoption et contrôle radio ; réseau configuré en L13. |
| 18 | 3 | 3/3/0/0 | 6/5/0/0 | Deux personnes × 3 h de montage/manutention 86 pouces, puis 5 h réglage, essais audio et visioconférence. |
| 19 | 1 | 0/3.4/0/0 | 0/5.6/0/0 | 24 × 0,15 h + 2 h rapport, étalonnage et reprises simples ; location distincte. |
| 22 | 1 | 0/0/0/0 | 0/0/0/0 | Sans objet : aucune heure ni fourniture. |
| 24 | 1 | 115.2/0/0/0 | 153.6/0/0/0 | 96 × 1,6 h/lien intérieur 35 m ; 1,2 h suppose des conditions répétitives idéales. |
| 25 | 20 | 0.75/0.25/0/0 | 0.75/0.5/0/0 | 45 min pose + 30 min adoption/test par borne ; prix matériel conservé comme estimation. |
| 26 | 7 | 3/3/0/0 | 6/5/0/0 | Même ratio que L18 pour chacune des 7 salles. |
| 27 | 1 | 0/10.6/0/0 | 0/16.4/0/0 | 96 × 0,15 h + 2 h rapport/reprises ; essais en plusieurs îlots. |
| 29 | 2 | 3.75/2/0/0 | 6/2/0/0 | 150 m × 4 h/100 m + 2 h intégration, par répartiteur ; pas une seule liaison pour les deux. |
| 30 | 30 | 2.5/0/0/0 | 3.5/0/0/0 | 60 m extérieurs : tirage, protection locale, deux terminaisons ; 2,5 h trop court. |
| 31 | 1 | 0/4.5/0/0 | 0/6.5/0/0 | 30 × 0,15 h + 2 h rapport/reprises, absentes du ratio initial. |
| 33 | 6 | 6/1.5/0/0 | 8/2.5/0/0 | Deux poseurs × 4 h pour manutention/support/étanchéité ; 2,5 h T raccordement et test. |
| 34 | 1 | 0/16/0/12 | 0/24/0/16 | 16 lecteurs × 0,75 h + 12 h serveur, groupes et formation ; 10 modèles FR/EN à 1,6 h. |
| 37 | 1 | 0/5/0/0 | 2/4/0/0 | Manutention baie à deux ; configuration en L41. |
| 38 | 1 | 3.75/0/0/0 | 6/0/0/0 | 150 m × 4 h/100 m ; fusion et mesures restent chez Octet Plus. |
| 39 | 1 | 5/0/0/0 | 8/0/0/0 | 200 m × 4 h/100 m. |
| 40 | 1 | 5/0/0/0 | 8/0/0/0 | 200 m × 4 h/100 m. |
| 41 | 1 | 0/16/0/8 | 0/24/0/8 | 3 ensembles × 4 h + 12 h tests de bascule et continuité ; BE local maintenu. |
| 42 | 1 | 0/0/0/0 | 0/0/0/0 | Zéro MO PROSYB conservé si mesures contractuellement incluses Octet Plus ; contrôler réflectométrie et fichiers natifs. |
| 44 | 2 | 0/5/0/0 | 2/4/0/0 | 2 h M + 4 h T par baie, quantité 2. |
| 45 | 1 | 432/0/0/0 | 576/0/0/0 | 360 × 1,6 h ; 18 prises par îlot ne comprennent pas automatiquement des points supplémentaires. |
| 46 | 60 | 0.75/0.25/0/0 | 0.75/0.5/0/0 | 45 min montage + 30 min adoption/mesure ; 60 bornes, fourniture EXYTE à confirmer. |
| 47 | 1 | 0/38/0/0 | 0/58/0/0 | 360 × 0,15 h + 4 h rapports ; 38 h initiales trop serrées pour 20 îlots. |
| 52 | 1 | 0/0/4/0 | 0/0/8/0 | 30 contacts : montage/repérage 2 h + câblage interne et contrôles 6 h ; essais bout en bout ailleurs. |
| 53 | 1 | 32.4/0/5/0 | 54/0/8/0 | 1 080 m × 5 h/100 m + 5 reports × 1,6 h raccordements aux extrémités. |
| 54 | 1 | 0/0/4/0 | 0/0/4/0 | 4 h centrale/DM/télécommande acceptables si circuits et alimentation prêts. |
| 55 | 1 | 0/0/4/0 | 0/0/4/0 | 4 h conservées ; réception globale en L60. |
| 56 | 1 | 0/0/5/0 | 0/0/6/0 | 4 h de base + 2 DM × 1 h ; accessoires et petites liaisons à prévoir. |
| 58 | 1 | 54.4/0/8/0 | 80/0/8/0 | 1 280 m × 5 h/100 m + 16 DM × 1 h = 80 h M ; raccordement 16 × 0,5 h SSI. |
| 59 | 1 | 40.8/0/6/0 | 60/0/6/0 | 960 m × 5 h/100 m + 12 diffuseurs × 1 h = 60 h M ; 12 × 0,5 h SSI. |
| 60 | 1 | 0/0/8/8 | 0/0/16/8 | Deux journées SSI pour essais scénario, audibilité et reports ; DOE local 8 h maintenu. |
| 62 | 1 | 60/0/8/0 | 100/0/16/0 | 2 000 m × 5 h/100 m ; 8 liaisons × 2 h raccordements. |
| 64 | 1 | 0/0/6/2 | 0/0/12/2 | 8 reports × 1 h + 4 h recette commune ; DOE 2 h. |
| 66 | 1 | 0/0/4/0 | 0/0/4/0 | Même centrale type 3 : 4 h maintenues. |
| 67 | 1 | 75/0/20/0 | 125/0/30/0 | 2 500 m × 5 h/100 m + 20 reports × 1,5 h ; tirage 3 h/100 m trop optimiste. |
| 69 | 1 | 0/0/8/4 | 0/0/24/4 | 20 îlots × 0,75 h + 9 h essais communs, défauts et PV ; BE local maintenu. |
| 75 | 28 | 4.5/0.5/0/0 | 5/0.75/0/0 | Mât sur massif GC prêt : 2 personnes × 2 h + 1 h accessoires ; 45 min pointage initial, recette nuit en L78. |
| 76 | 1 | 56/16/0/0 | 84/24/0/0 | 28 liaisons × 3 h + 8 coffrets × 3 h (PoE, SFP, repérage) ; limite cuivre à contrôler. |
| 77 | 1 | 0/3/0/0 | 0/4/0/0 | Pose, deux disques, initialisation et essais stockage ; analyse capacité en BE vidéo. |
| 78 | 1 | 0/36/0/20 | 0/52/0/28 | 28 caméras × 1 h + 24 h VMS, alarmes, essais nuit/intrusion et formation ; BE couverture/RGPD/DOE 28 h. |
| 79 | 1 | 0/5/0/0 | 0/7.6/0/0 | 28 × 0,2 h + 2 h rapport ; essais des fonctions vidéo comptés en L78. |
| 83 | 3 | 0/3/0/0 | 0/3/0/0 | 3 h/automate conservées : montage et repérage PROSYB, configuration sous-traitée. |
| 84 | 3 | 0/0.5/0/0 | 0/0.5/0/0 | 30 min/alimentation conservées si départ protégé disponible côté tableautier. |
| 85 | 3 | 1/0/0/0 | 0.5/0/0/0 | Liaison locale déjà accessible : 30 min, contre 1 h ; test global par AETHERYS. |
| 86 | 3 | 5/1/0/0 | 4.5/1/0/0 | 52 TOR estimés (19 + 20 + 13) × 0,25 h = 13 h, + 0,5 h repérage ; moyenne 4,5 h M/u, 1 h T/u. |
| 87 | 3 | 2/1/0/0 | 2/1/0/0 | Bus interne 30 m et un raccordement : 2 h M + 1 h T conservées ; 40 points ne sont pas 40 compteurs. |
| 88 | 1 | 0/0.5/0/0 | 0/0.5/0/0 | Installation AETHERYS incluse ; 30 min réception PROSYB conservées, sans seconde pose. |
| 89 | 1 | 0/8/0/4 | 0/12/0/8 | Trois séquences de coordination/recette × 4 h T + 8 h revue points/interfaces ; aucune reprogrammation du forfait AETHERYS. |

La réserve initiale L58 n’oubliait pas les 16 poses : 1 280 × 3/100 + 16 = 54,4 h M. L59 : 960 × 3/100 + 12 = 40,8 h. Le défaut porte sur le rendement de tirage, pas sur une omission de toutes les poses. Les ratios de cuivre incluent les terminaisons ; les contrôles de certification sont séparés.

| Ressource | Heures actuelles lots 4–7 | Proposées lots 4–7 |
|---|---:|---:|
| M | 1 353,60 | 1 886,00 |
| T | 306,50 | 441,10 |
| S | 90,00 | 146,00 |
| BE | 74,00 | 86,00 |

MO directe : **83 664,00 → 117 408,00 € PR**, soit +33 744,00 €. Ces heures excluent les interventions du sous-traitant AETHERYS déjà dans son prix. Les baisses ciblées concernent BE L13 (16 → 12), Ethernet GTB (1 → 0,5 h M) et TOR GTB (5 → 4,5 h M en moyenne). Les poses 86 pouces et les recettes SSI sont sous-évaluées dans v6.

## 3. Ajouts et risques : montants sans double compte

Les ajouts suivants sont **nets des provisions existantes**. Ils ne réachètent ni les supports 775 €, ni les 756 € AV, ni les 870 € GTB. Ils restent estimatifs, à remplacer par devis.

| Ligne | Ajout PR/u | Base et risque couvert |
|---|---:|---|
| 18 | 500,00 | Réserve nette 500 €/salle : remplacer MeetUp par 4 vrais Mic Pods, câbles/hubs et adaptation chariot ; 5 micros déportés exigent variante. |
| 26 | 500,00 | Même correction AV ; pas un 4e Mic Pod ajouté aveuglément au MeetUp. |
| 30 | 60,00 | 60 €/liaison protection extérieure locale (30 × 60 m), hors tranchée/chemin de câble général. |
| 33 | 225,00 | Support porté de 775 à 1 000 €/u en moyenne, adaptation OHDX et antivol à recoter. |
| 34 | 2 400,00 | 2 400 € réserve licences/serveur sur durée, en plus du serveur 1 100 € déjà prévu. |
| 52 | 300,00 | 300 € interfaces relais/borniers, acceptation SSI à valider. |
| 54 | 80,00 | 80 € accessoires et petites liaisons. |
| 55 | 80,00 | 80 € accessoires et petites liaisons. |
| 56 | 120,00 | 120 € accessoires pour 3 DM. |
| 58 | 200,00 | 200 € boîtes/protections locales. |
| 59 | 300,00 | 300 € protections IP/abris et accessoires. |
| 66 | 80,00 | 80 € accessoires. |
| 75 | 220,00 | 220 €/u nets : 150 caméra intrusion et 70 platine, accessoires mât, mise à la terre ; massif GC exclu. |
| 76 | 1 600,00 | 1 600 € réserve protections/UPS locaux ; alimentation et autonomie à dimensionner. |
| 77 | 0,00 | Budget HDD 1 545,45 € conservé pour 2 disques compatibles, sans gain de prix garanti. |
| 78 | 6 000,00 | 6 000 € provision analyse vidéo/EPI, intégration et licences ; solution non justifiée par le devis. |
| 87 | 100,00 | 100 €/Hub réserve connectique RS485/terminaisons, pas ajout automatique de module série. |
| 89 | 1 000,00 | 1 000 € : SMS 250 + renouvellement CARE estimé 750 ; prolongation 5G/TMA 870 déjà présente. |

Total achats complémentaires lots 4–7 : **26 770,00 € PR**. Les bases de prix des devis en attente de correction restent conservées ; aucune baisse hypothétique sur HDD, micro MeetUp ou SSI n’est comptabilisée.

| Référence | Complément hors v6 | PR | PV | Base retenue |
|---|---|---:|---:|---|
| M1 | Moyens communs : nacelle | 3 600,00 | 4 320,00 | 8 j × 350 € + 800 € transports ; pose valorisée aux lignes, pas de nouvelle MO. |
| M2 | Moyens communs : certificateur cuivre | 2 400,00 | 2 880,00 | 8 j × 250 € + 400 € livraison/étalonnage ; 538 liens à tester, MO aux lignes 19/27/31/47/79. |
| M3 | Déplacements installation | 6 000,00 | 7 200,00 | 60 rotations × 100 € véhicule/péages ; temps productif local dans ratios, trajet supplémentaire en encadrement ci-dessous si nécessaire à réviser. |
| M4 | Encadrement installation | 10 800,00 | 17 280,00 | 144 h chef de projet à 75 € : 18 revues/phases × 8 h, hors programmation, BE métier et TMA. |
| §2 EXE.CFA | Architecture IT & audiovisuel | 6 000,00 | 9 600,00 | 80 h BE × 75 €, architecture, cybersécurité, interfaces, visas et matrice FR/EN ; en plus des DOE locaux, sans refaire études GTB AETHERYS. |
| 105 CFA | Maintenance préventive/corrective 28 mois | 19 312,00 | 30 179,20 | 28 × (8 h CFA × 60 + 2 h SSI × 62) + 2 400 € pièces ; hors TMA/5G GTB déjà en L89, hors permanence. PV = 16 912 × 1,60 + 2 400 × 1,30. |
| 106 CFA | Astreinte mutualisée à distance 28 mois | 5 600,00 | 6 608,00 | 28 × 200 € de sous-traitance estimée pour réception/qualification hors heures ouvrées ; interventions courantes dans 105. Ne couvre pas un technicien présent 24/7. |
| 104 CFA | Modifications chantier | 4 000,00 | 6 340,00 | 80 h M + 10 h T + 200 € petit matériel : PV corrigé par nature = 3 800 × 1,60 + 200 × 1,30 ; hors déplacement installation et repli. |
| 107 CFA | Repli phase 3 | 2 240,00 | 3 392,00 | 32 h M + 8 h T + 480 € évacuation ; PV = 1 760 × 1,60 + 480 × 1,20. |
| 108 CFA | Repli final | 6 560,00 | 9 984,00 | 96 h M + 24 h T + 1 280 € évacuation ; PV = 5 280 × 1,60 + 1 280 × 1,20. |
| R1 | Aléas techniques installation | 11 637,53 | 13 965,04 | 3 % × 387 917,70 € PR direct corrigé lots 4–7 ; valorisation 1,20. Hors maintenance et moyens communs. |

Nacelle : huit jours est une provision de campagne, non une promesse de disponibilité EXYTE. Certificateur : 538 tests en huit journées supposent des prises accessibles et des campagnes regroupées ; augmenter les jours si phasage dispersé. Déplacements : 60 rotations sont une allocation, à caler au planning de pose ; les trajets des visites de maintenance doivent tenir dans les dix heures mensuelles ou être révisés. Encadrement : 144 h n’achètent pas une présence hebdomadaire pendant 29 mois ; la mission inclut seulement réunions clés, visas et suivi d’interface. À titre de sensibilité, un jour/mois sur 29 mois représente 232 h, soit +88 h BE / +10 560 € PV au-delà de la provision.

**Maintenance §8 :** dix heures mensuelles moyennes CFA/SSI et un stock 2 400 € sont une base pour visites regroupées et correctifs courants, à affiner par parc et phases ; matériel vandalisé, déplacements multiples et engagements courts imposent une autre enveloppe. La TMA GTB, limitée à distance, ne remplace pas la maintenance physique. La durée 28 mois DPGF prévaut pour cette allocation ; l’hypothèse de 29 mois du brief reste utilisée pour les cinq mois d’extension GTB. Novembre 2026 à décembre 2028 ne démontre pas à lui seul 29 mois : fixer les dates contractuelles et démarrages par équipement. Si 28 mois GTB suffisent, réduire d’un mois, soit 174 € PR / 205,32 € PV.

**Permanence 24/7 : risque majeur non soldé.** Les 5 600 € PR achètent uniquement une astreinte externalisée mutualisée avec qualification à distance, sous réserve d’un devis et de SLA acceptés. Le libellé DPGF peut imposer une présence sur site : un poste continu vaut environ 28 × 730 = 20 440 h de couverture. À 60 €/h de coût hypothétique, cela fait 1 226 400 € PR avant majorations de nuit/remplacement ; PV à 1,60 = 1 962 240 €, à substituer à la provision 6 608 € PV et à répartir CFO/CFA contractuellement. Ce scénario n’est pas inclus dans le total de base. Ne pas présenter l’astreinte comme conforme à une permanence physique.

Autres réserves : délais et validité des devis 27–31/10 versus validité d’offre 90 jours ; prix cuivre/électronique et change ; garantie sur matériels réemployés ; longueurs cuivre ≤90 m permanent link, dorsales supplémentaires au-delà ; source internet autonome vidéo, débit/SIM hors routeur de télémaintenance GTB ; secours énergétique NVR/switchs, protections foudre et terre ; capacité serveur Navori/GTB et licences sur toute la période ; environnement poussière/vandalisme ; déplacements de caméras hors quota modifications ; reprises des cheminements et rebouchages coupe-feu. La réserve R1 absorbe de petites variations, pas une infrastructure extérieure complète, une présence 24/7 ou une refonte AV/vidéo. Aucun prix ferme de conformité totale n’est possible tant que ces interfaces ne sont pas levées.

## 4. Politique de coefficients et effet isolé

Un coefficient unique sur un achat ferme de prestation AETHERYS est commercialement possible puisque PROSYB porte le contrat client, mais **1,4444 est élevé pour un forfait sous-traité déjà chargé en études, MES et TMA** si les frais d’encadrement sont facturés à part. Je retiens les coefficients de vente suivants, à valider avec la structure réelle des frais et la marge minimale PROSYB :

| Nature | k proposé | Marge brute PV avant frais | Application |
|---|---:|---:|---|
| Fourniture et licence achetée directement | 1,30 | 23,08 % | Achats devis et estimatifs PROSYB |
| MO propre, études et encadrement | 1,60 | 37,50 % | Coûts horaires inchangés ; suppose taux de revient chargés à confirmer |
| Forfait sous-traité piloté | 1,18 | 15,25 % | Ensemble AETHERYS, y compris matériel intégré et prolongation 870 € ; astreinte externalisée |
| Location, évacuation, frais directs et provision aléas | 1,20 | 16,67 % | Moyens communs et R1 explicités |

Les 8 % et les 4 % de l’ancienne formule ne sont pas rajoutés : les nouveaux coefficients les remplacent. Les frais généraux de siège restent à absorber dans ces marges ; l’encadrement de projet est une ressource directement affectée, identifiée séparément. La réserve 3 % remplace la logique forfaitaire d’aléas anciens, sans seconde majoration de 4 %. Le même barème par nature est proposé en SSI ; il faut vérifier son acceptabilité commerciale et le niveau de risque SSI.

Sur **le seul devis AETHERYS 28 714 €**, k actuel donne 41 475,78 € PV théorique ; k 1,18 donne 33 882,52 €, soit **−7 593,26 €**. Sur devis + extension 870 € : économie théorique 7 823,32 €. Ces montants isolés sont calculés avant arrondis unitaires ; les tableaux suivent l’arrondi par unité DPGF. La fourniture/pose du PC n’est pas remargée une seconde fois en MO PROSYB.

Octet Plus contient une sous-traitance fusion/mesures dans un forfait mêlé de fournitures. Faute de décomposition fiable, tout le forfait reste provisoirement en fourniture à 1,30. Si les 6 732,72 € étaient intégralement des prestations (hypothèse haute), leur passage à 1,18 réduirait encore le PV d’environ 807,93 € ; ne pas déduire cela sans séparer tiroirs/jarretières et MO.

**Pont de prix vérifiable :**

| Étape | PV | Écart de l’étape |
|---|---:|---:|
| FCI v6 actuelle, lots 4–7 | 468 579,35 | — |
| Coefficients seuls, achats/heures v6 conservés | 447 173,86 | -21 405,49 |
| + heures corrigées + achats nets, lots 4–7 | 535 965,26 | 88 791,40 |
| + moyens, EXE et §8 CFA | 633 748,46 | 97 783,20 |
| + R1 aléas | **647 713,50** | 13 965,04 |

## 5. Tableau final de vente

PV par **ligne totale**, quantité comprise. Ancien zéro pour les compléments signifie « absent de la FCI », pas « prestation gratuite au marché ». Les forfaits M/R1 doivent être répartis dans les prix DPGF si le client interdit les lignes nouvelles ; ne pas conserver simultanément les forfaits et leur réaffectation. Les lignes hors lot SSI et L74 GC restent hors PROSYB. Les lignes 93–103 du §8 sont des prestations CFO, non transférées au CFA.

| Ligne DPGF (TSV) | Désignation courte | PV actuel | PV proposé | Écart | Raison |
|---|---|---:|---:|---:|---|
| 4 | Baie Hub 1 | 2 485,71 | 2 359,14 | -126,57 | Coef par nature ; MO revue §2 |
| 5 | Baie Hub 2 | 1 350,34 | 1 337,31 | -13,03 | Coef par nature ; MO revue §2 |
| 6 | Secondaire Est 1 | 173,33 | 192,00 | 18,67 | Coef par nature |
| 7 | Secondaire Est 2 | 173,33 | 192,00 | 18,67 | Coef par nature |
| 8 | Secondaire Est 3 | 173,33 | 192,00 | 18,67 | Coef par nature |
| 9 | Secondaire Ouest 1 | 173,33 | 192,00 | 18,67 | Coef par nature |
| 10 | Secondaire Ouest 2 | 173,33 | 192,00 | 18,67 | Coef par nature |
| 11 | Boucle fibre | 14 437,10 | 16 647,40 | 2 210,30 | Coef par nature ; MO revue §2 |
| 12 | Fibre Hub 1–2 | 2 296,13 | 2 633,52 | 337,39 | Coef par nature ; MO revue §2 |
| 13 | Configuration P2 | 3 466,67 | 4 128,00 | 661,33 | Coef par nature ; MO revue §2 |
| 14 | Réflectométrie P2 | 0,00 | 0,00 | 0,00 | Zéro MO PROSYB conservé si mesures contractuellement incluses Octet Plus ; contrôler réflectométrie et fichiers natifs. |
| 16 | 24 liens cuivre | 2 777,32 | 3 459,59 | 682,27 | Coef par nature ; MO revue §2 |
| 17 | 4 bornes Wi-Fi | 260,00 | 384,00 | 124,00 | Coef par nature ; MO revue §2 |
| 18 | 3 salles AV | 39 687,48 | 39 090,75 | -596,73 | Coef par nature ; MO revue §2 ; achats §3 |
| 19 | Recette 24 liens | 294,67 | 537,60 | 242,93 | Coef par nature ; MO revue §2 |
| 22 | Sans objet | 0,00 | 0,00 | 0,00 | Sans objet : aucune heure ni fourniture. |
| 24 | 96 liens cuivre | 11 109,29 | 13 838,37 | 2 729,08 | Coef par nature ; MO revue §2 |
| 25 | 20 bornes Wi-Fi | 5 922,20 | 6 080,00 | 157,80 | Coef par nature ; MO revue §2 |
| 26 | 7 salles AV | 92 604,12 | 91 211,75 | -1 392,37 | Coef par nature ; MO revue §2 ; achats §3 |
| 27 | Recette 96 liens | 918,67 | 1 574,40 | 655,73 | Coef par nature ; MO revue §2 |
| 29 | 2 répartiteurs annexes | 2 958,00 | 3 112,20 | 154,20 | Coef par nature ; MO revue §2 |
| 30 | 30 liens extérieurs | 6 444,00 | 10 959,60 | 4 515,60 | Coef par nature ; MO revue §2 ; achats §3 |
| 31 | Recette extérieurs | 390,00 | 624,00 | 234,00 | Coef par nature ; MO revue §2 |
| 33 | 6 afficheurs extérieurs | 51 634,32 | 50 163,90 | -1 470,42 | Coef par nature ; MO revue §2 ; achats §3 |
| 34 | Paramétrage Navori | 4 275,55 | 8 774,00 | 4 498,45 | Coef par nature ; MO revue §2 ; achats §3 |
| 37 | Baie Hub 3 | 1 350,34 | 1 337,31 | -13,03 | Coef par nature ; MO revue §2 |
| 38 | Fibre Hub 1–3 | 1 305,66 | 1 364,10 | 58,44 | Coef par nature ; MO revue §2 |
| 39 | Fibre A | 1 470,73 | 1 575,66 | 104,93 | Coef par nature ; MO revue §2 |
| 40 | Fibre B | 1 470,73 | 1 575,66 | 104,93 | Coef par nature ; MO revue §2 |
| 41 | Configuration P4 | 2 253,33 | 3 264,00 | 1 010,67 | Coef par nature ; MO revue §2 |
| 42 | Réflectométrie P4 | 0,00 | 0,00 | 0,00 | Zéro MO PROSYB conservé si mesures contractuellement incluses Octet Plus ; contrôler réflectométrie et fichiers natifs. |
| 44 | 2 baies P4 | 2 700,68 | 2 674,62 | -26,06 | Coef par nature ; MO revue §2 |
| 45 | 360 liens cuivre | 41 659,83 | 51 893,86 | 10 234,03 | Coef par nature ; MO revue §2 |
| 46 | 60 bornes Wi-Fi | 3 900,00 | 5 760,00 | 1 860,00 | Coef par nature ; MO revue §2 |
| 47 | Recette 360 liens | 3 293,33 | 5 568,00 | 2 274,67 | Coef par nature ; MO revue §2 |
| **Lot 4** | **Sous-total** | **303 582,85** | **332 888,74** | **29 305,89** | |
| 52 | Coffret reports SSI | 2 901,19 | 3 653,60 | 752,41 | Coef par nature ; MO revue §2 ; achats §3 |
| 53 | Liaisons SSI P2 | 7 501,50 | 9 382,00 | 1 880,50 | Coef par nature ; MO revue §2 |
| 54 | Type 3 garde | 777,16 | 926,42 | 149,26 | Coef par nature ; achats §3 |
| 55 | Type 3 Hub 1 | 743,40 | 893,92 | 150,52 | Coef par nature ; achats §3 |
| 56 | Type 3 Hub 2 | 901,15 | 1 215,56 | 314,41 | Coef par nature ; MO revue §2 ; achats §3 |
| 58 | 16 DM chantier | 7 887,79 | 10 292,00 | 2 404,21 | Coef par nature ; MO revue §2 ; achats §3 |
| 59 | 12 diffuseurs chantier | 8 039,06 | 9 957,60 | 1 918,54 | Coef par nature ; MO revue §2 ; achats §3 |
| 60 | MES SSI P2 | 1 480,31 | 2 547,20 | 1 066,89 | Coef par nature ; MO revue §2 |
| 62 | Liaisons SSI P3 | 11 745,24 | 15 527,20 | 3 781,96 | Coef par nature ; MO revue §2 |
| 64 | MES SSI P3 | 705,04 | 1 430,40 | 725,36 | Coef par nature ; MO revue §2 |
| 66 | Type 3 Hub 3 | 743,40 | 893,92 | 150,52 | Coef par nature ; achats §3 |
| 67 | Liaisons SSI P4 | 17 950,13 | 22 741,00 | 4 790,87 | Coef par nature ; MO revue §2 |
| 69 | MES SSI P4 | 1 075,12 | 2 860,80 | 1 785,68 | Coef par nature ; MO revue §2 |
| **Lot 5** | **Sous-total** | **62 450,49** | **82 321,62** | **19 871,13** | |
| 75 | 28 caméras et mâts | 26 375,44 | 35 077,84 | 8 702,40 | Coef par nature ; MO revue §2 ; achats §3 |
| 76 | Réseau vidéo | 18 219,64 | 21 997,68 | 3 778,04 | Coef par nature ; MO revue §2 ; achats §3 |
| 77 | NVR et stockage | 3 513,06 | 3 311,76 | -201,30 | Coef par nature ; MO revue §2 |
| 78 | Logiciel vidéo/recette | 6 635,44 | 17 365,90 | 10 730,46 | Coef par nature ; MO revue §2 ; achats §3 |
| 79 | Recette cuivre vidéo | 433,33 | 729,60 | 296,27 | Coef par nature ; MO revue §2 |
| **Lot 6** | **Sous-total** | **55 176,91** | **78 482,78** | **23 305,87** | |
| 83 | 3 automates GTB | 6 188,01 | 5 281,92 | -906,09 | Coef par nature ; forfait AETHERYS à 1,18 |
| 84 | 3 alimentations GTB | 468,00 | 420,12 | -47,88 | Coef par nature ; forfait AETHERYS à 1,18 |
| 85 | 3 liaisons Ethernet | 303,33 | 213,00 | -90,33 | Coef par nature ; MO revue §2 |
| 86 | 3 câblages TOR | 1 473,33 | 1 464,00 | -9,33 | Coef par nature ; MO revue §2 |
| 87 | 3 bus RS485 | 780,00 | 1 218,00 | 438,00 | Coef par nature ; achats §3 |
| 88 | PC et 2 écrans | 2 446,89 | 2 011,52 | -435,37 | Coef par nature ; forfait AETHERYS à 1,18 |
| 89 | Logiciel/MES/TMA GTB | 35 709,54 | 31 663,56 | -4 045,98 | Coef par nature ; MO revue §2 ; achats §3 ; forfait AETHERYS à 1,18 |
| **Lot 7** | **Sous-total** | **47 369,10** | **42 272,12** | **-5 096,98** | |
| **Lots 4–7** | **Périmètre comparable** | **468 579,35** | **535 965,26** | **67 385,91** | |
| M1 | Moyens communs : nacelle | 0,00 | 4 320,00 | 4 320,00 | Allocation nouvelle §3 |
| M2 | Moyens communs : certificateur cuivre | 0,00 | 2 880,00 | 2 880,00 | Allocation nouvelle §3 |
| M3 | Déplacements installation | 0,00 | 7 200,00 | 7 200,00 | Allocation nouvelle §3 |
| M4 | Encadrement installation | 0,00 | 17 280,00 | 17 280,00 | Allocation nouvelle §3 |
| §2 EXE.CFA | Architecture IT & audiovisuel | 0,00 | 9 600,00 | 9 600,00 | Allocation nouvelle §3 |
| 105 CFA | Maintenance préventive/corrective 28 mois | 0,00 | 30 179,20 | 30 179,20 | Allocation nouvelle §3 |
| 106 CFA | Astreinte mutualisée à distance 28 mois | 0,00 | 6 608,00 | 6 608,00 | Allocation nouvelle §3 |
| 104 CFA | Modifications chantier | 0,00 | 6 340,00 | 6 340,00 | Allocation nouvelle §3 |
| 107 CFA | Repli phase 3 | 0,00 | 3 392,00 | 3 392,00 | Allocation nouvelle §3 |
| 108 CFA | Repli final | 0,00 | 9 984,00 | 9 984,00 | Allocation nouvelle §3 |
| R1 | Aléas techniques installation | 0,00 | 13 965,04 | 13 965,04 | 3 % PR direct × 1,20 |
| **TOTAL CFA ÉLARGI** | **Sous les hypothèses explicites ci-dessus** | **468 579,35** | **647 713,50** | **179 134,15** | **Écart périmètre + prix ; hors scénario présence 24/7** |

Priorités avant engagement : obtenir les devis corrigés AV/vidéo et validation SSI ; verrouiller switchs/coffrets/GC/cheminements/énergie et les métrés sur PIC ; séparer astreinte et permanence dans le §8 ; demander AETHERYS 28/29 mois, CARE/OPALE/SMS et limites de pose signés. Les provisions associées doivent ensuite être remplacées, jamais additionnées aux devis de remplacement.
