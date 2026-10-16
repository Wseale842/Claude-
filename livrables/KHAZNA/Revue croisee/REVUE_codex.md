# Revue senior — PROSYB / KHAZNA ORY01 — 16 octobre 2026

## Périmètre et niveau de preuve

Documents examinés : `BRIEF_codex.md`, source `memoire/memoire.html`, `dpgf/DPGF_lots4-8_CFA.tsv`, recherches ciblées dans `specs/General_Statement_of_Requirements.txt` (SoR Haskoning, 30 avril 2026). Les renvois au mémoire désignent ses chapitres ; les ancres de la section 3 reproduisent le HTML littéralement.

**Limite essentielle : `devis/` est vide.** Les références, caractéristiques, exclusions et validités fournisseurs ci-dessous proviennent du brief, pas d'une lecture des devis originaux. Le CCTP vidéo et son annexe A originaux ne sont pas présents : leur contrôle repose sur le résumé déclaré fidèle du brief. Une caractéristique produit non documentée reste à confirmer ; aucun contrôle constructeur externe n'a été effectué. Les illustrations liées par le HTML ne sont pas présentes dans le répertoire mémoire examiné : vérifier leur intégration au dossier final et leur cohérence avec les corrections proposées.

**Verdict : le mémoire est lisible mais présente comme acquises des fonctions et des fournitures que le dossier disponible ne démontre pas.** Pour convaincre EXYTE, il faut fermer les écarts de périmètre, prouver la chaîne fonctionnelle caméra–alarme–opérateur et transformer les engagements de service en prestations financées. Le classement ci-dessous est qualitatif : aucune grille de notation pondérée n'est disponible. EXYTE est ici le destinataire/entreprise générale, pas un concurrent dont une offre serait connue.

## 1. Top 10 des faiblesses, par impact probable sur la note technique

| Rang / impact | Faiblesse et preuve | Conséquence / correction prioritaire |
|---|---|---|
| **1 — critique** | **Intrusion et EPI promis sans chaîne fonctionnelle prouvée.** §1 : « analyse intrusion et port des EPI » ; §7 : franchissement de ligne, intrusion de zone, association automatique. Brief CCF : DS-2CD1643G2-LIZSU avec détection humain/véhicule ; analyse périmétrique du NVR limitée à 2 voies 4 MP. Aucune preuve du traitement des 28 voies, ni de l'analyse EPI. | Classification humain/véhicule ≠ preuve de règles périmétriques ni d'analyse EPI. Faire confirmer événements disponibles caméra/firmware, nombre de voies côté NVR et intégration iVMS ; démonstration puis PV. Chiffrer un moteur/détecteur adapté ou déclarer la déviation, sans retirer unilatéralement une exigence de base. |
| **2 — critique** | **Périmètre contractuel contradictoire : SSI et switchs.** §12 exclut le « système de sécurité incendie » ; DPGF §5 inclut centrales type 3, DM, diffuseurs, reports et mise en service. §3 met les switchs informatiques à EXYTE alors que plusieurs ensembles DPGF §4 sont « incluant switch PoE ». | Risque d'offre incomplète et d'avenants immédiats. Décrire le SSI AVISS et ses essais ; exclure seulement les équipements explicitement hors lot. Obtenir une clarification écrite pour les switchs ou fournir une base conforme et une variante déductive EXYTE. |
| **3 — critique** | **GTB décrite sur une autre base que l'offre retenue.** §8 : WAGO 751-9301, supervision générique ; absence Ignition Edge/OPALE/IXON et des rétentions. Brief AETHERYS : PFC100 750-8112, offre 28 714 € HT. | Réécrire la nomenclature et les fonctions autour d'AETHERYS, reprendre études/AF/recette/formation/DOE ; vérifier RS485, SMS et licence. Financer la continuité après les 24 mois de TMA et de 5G. |
| **4 — très fort** | **Chaîne AV chiffrée différente de la chaîne promise.** Mémoire : 4 Rally Mic Pod/salle ; brief Sonepar : micro MeetUp LOG025 incompatible Rally Bar. Chariot annoncé 50–85 pouces pour écran 86 pouces. Totems et serveur Navori non chiffrés. | Faire réviser le devis : micros compatibles, support approuvé pour modèle exact, serveur/licences/maintenance et 3 supports extérieurs. Les 4 micros restent une déviation aux 5 déportés du DPGF. |
| **5 — très fort** | **Stockage vidéo non sécurisé techniquement.** §7 : 1 HDD 20 To, environ 15 jours ; brief : plafond NVR 16 To/baie, compatibilité 20 To douteuse. | Confirmer suffixe matériel/firmware et liste HDD approuvée avant commande. À 28 × 4 Mbit/s, 15 jours demandent **18,144 To décimaux de vidéo seule**, avant réserve ; 20 To bruts offrent peu de marge et aucune redondance de disque. Fournir calcul et capacité utile garantis à débit plafonné. |
| **6 — fort** | **SLA chiffrés mais moyens non démontrés.** §11 promet 4 h sur site et rétablissement 8 h 24/7, stock chantier, ticket automatique et objectif ≥99 %. Aucun roulement d'astreinte, inventaire financé ou contrat fournisseur disponible. | Conserver les engagements seulement après plan de charge, suppléance, accès site et stock. Définir point de départ, heures calendaires/ouvrées, périmètre de disponibilité et solution provisoire. La TMA distante AETHERYS ne prouve pas un déplacement 24/7. |
| **7 — fort** | **Conformité vidéo déclarative et limites conflictuelles.** Annexe A §7 tout « Oui » ; PTZ/barrières en option sans BPU visible. Massifs exclus conformément au DPGF « LOT GC », mais résumé CCTP demandant supports/massifs inclus. Caméras IP67 sans IK10, pas d'anticorrosion spécifique selon brief. | Remplacer les auto-certifications par preuves/statuts. Arbitrer par RFI CCTP/DPGF sur massifs et besoin PTZ/IR ; ne pas transformer une fonction obligatoire en option sans accord. Justifier tenue chantier, implantation et protections. |
| **8 — fort** | **Autocicatrisation et autonomie énergétique surpromises.** §3 : toute coupure de fibre sans perte de répartiteur, reprise <50 ms ; caractéristiques L3 incohérentes (ports cuivre PoE+ demandés puis SFP annoncés). Départs « secourus » assimilés à continuité sans autonomie quantifiée. | Valider ERPS multi-modèles, trajet physique des retours, points uniques de panne et budget PoE/thermique. Tester coupure, perte d'un switch et perte d'alimentation. Documenter alimentation sur GE phase 1 et autonomie des équipements critiques ; distinguer GE et onduleur. |
| **9 — fort** | **Dossier de conformité et preuves entreprise insuffisants.** Pas de matrice clause par clause, version EN, validité ≥90 j, déviations formalisées, certificats ISO/EPD. §13 affirme l'expérience data center sans références. | Joindre dossier de conformité, références vérifiables avec rôle réel, CV/habilitations et planning nominatif. Ces éléments rendent l'offre auditable ; ne pas inventer de certifications. |
| **10 — significatif** | **Calendrier et quantités insuffisamment maîtrisés.** 29 mois annoncés, 28 mois DPGF, 24 mois fournisseurs GTB ; phases 2+5+17 = 24 mois ; novembre 2026 à décembre 2028 ne justifie pas seul 29 mois. 480 prises et 84 AP sont des sommes de phases, pas la preuve d'un parc simultané. | Produire calendrier contractuel daté, quantités installées/réemployées/déposées par phase, dates de départ des abonnements et repli. Prouver approvisionnements : « disponibles sous une semaine » n'est pas étayé par une confirmation de stock. |

## 2. Écarts factuels mémoire ↔ données fournisseurs du brief

Le statut « non démontré » ne signifie pas « impossible ». Demander les devis révisés et fiches avant de déclarer conformité.

| Citation du mémoire / repère | Donnée fournisseur rapportée | Lecture et action |
|---|---|---|
| §8 « WAGO Compact Controller 100 (751-9301) » | AETHERYS : **3 WAGO PFC100 750-8112** | Contradiction de référence certaine entre mémoire et brief. Remplacer nomenclature et légendes liées. |
| §8 « Poste fixe à deux écrans […] accès web aux automates » | HP ProDesk + 2 iiyama 24 pouces ; **Ignition Edge IGN-EDGE-PANEL-83, basic CARE 24 mois, 2 clients web concurrents + SME OPALE** | Description insuffisante, pas une équivalence au seul serveur web automate. Préciser limite de concurrence et recette fonctionnelle. |
| §8 « Tableaux de bord […] historisation » | Énergie **24 mois**, alarmes/états **45 jours**, enveloppe annoncée **10 millions d'enregistrements** | Donner ces limites ; vérifier périodes d'échantillonnage et volume permettant de tenir les deux rétentions. 24 mois d'archives ≠ 24 mois de support. |
| §3 « Routeur 4G/5G VPN […] Option » ; §12 « Arrivées opérateurs, abonnements […] (EXYTE) » | **IXON 5G + antenne extérieure, abonnement 5G 24 mois inclus** dans AETHERYS | Isoler le service GTB inclus de l'option vidéo et des arrivées EXYTE. Faire valider routage et cybersécurité. |
| §1 « maintenance assurée en continu pendant 29 mois » ; §11 « 28 mois d'exploitation » | AETHERYS : **TMA à distance 24 mois**, 5G 24 mois | Manque de couverture de 4 mois si exploitation 28 mois, 5 si 29 mois, à ajuster aux dates réelles d'activation. Faire chiffrer prorogation, pas l'assimiler au support PROSYB. |
| §8 compteurs « Modbus RS485 », GE/ASI « Liaison de communication » | Par Hub : **2 × DI16 750-1405**, terminaison **750-600**, alimentation **787-1212** ; ASI/GE Modbus TCP ; centrales de mesure RS485 ; ~20 TOR +40 points RS485 +30 TCP | Distinguer points logiciels et entrées physiques. 32 DI annoncées/Hub : vérifier liste de points finale et réserve. Le brief évoque un **750-960 non chiffré**, mais cette référence est **absente du HTML lu** : ne pas prétendre l'y avoir trouvée. Vérifier rôle et besoin exacts de l'interface RS485, les inclure si nécessaires. |
| §8 et §10 « Alertes SMS et e-mail » | Brief AETHERYS ne détaille pas passerelle SMS, service, quotas et licences de notification | Une liaison 5G ne prouve pas la fonction SMS. Faire confirmer chaîne complète et coût ; l'exigence DPGF SMS/Mail demeure. |
| §6 « 4 Logitech Rally Mic Pod (réf. 989-000430) » | Sonepar : **LOG025 MeetUp** ; brief indique incompatibilité Rally Bar | Remplacer les lignes d'achat, pas seulement le texte commercial. Confirmer rallonges/hubs et topologie audio. |
| §6 « Chief Voyager LSCUW […] charge 79 kg, VESA […] 600 × 400 » + écran 86 pouces | Chariot annoncé **50–85 pouces** | Charge et VESA seuls ne prouvent pas compatibilité ; le 85,6 pouces visible n'est pas une approbation fabricant. Faire confirmer ensemble écran/barre/accessoires ou remplacer support. |
| §6 « 3 totems ERARD PRO OUTDOOH » | Totems **non chiffrés**, prévus pour **OH55F**, portrait ; écran offert OHDX | Coût absent et compatibilité mécanique/ventilation non prouvée. Demander validation OHDX, fixation, lestage/vent et prix. |
| §6 « serveur de diffusion unique Navori QL installé sur site » ; « sans abonnement cloud » | Serveur **non chiffré**, durée des licences StiX à confirmer | Local/sans cloud ne veut pas dire licences perpétuelles. Confirmer serveur, OS, sauvegarde, activation hors ligne, 16 lecteurs et droits sur toute la durée. |
| §7 « franchissement de ligne et entrée en zone sur les caméras périmétriques » ; « pas de perte de fonctions » | Caméras : humain/véhicule ; NVR : périmétrique **2 voies 4 MP** selon brief | L'usage d'une marque unique ne prouve pas les événements ni leur transport. Faire établir matrice caméra/NVR/client et démontrer le scénario sur les voies requises. |
| §1 « analyse intrusion et port des EPI » | Aucune fonction EPI documentée dans la sélection CCF | Engagement non étayé. Le mode « statistique » du §7 n'apporte ni moteur d'analyse, ni validation de la finalité. |
| §7 « 1 disque […] 20 To » | NVR : **16 To maximum par baie** selon brief | Risque d'incompatibilité, à confirmer sur variante exacte ; ne pas qualifier l'incompatibilité de définitivement acquise. Envisager plusieurs HDD approuvés. |
| §7 caméras « IP67 » ; mâts « protégées des chocs » | Pas IK10, « no specific anti-corrosion » | IP67 traite l'intrusion eau/poussière, ne prouve pas résistance aux chocs/corrosion. Justifier pose hors d'atteinte ou variante durcie. |
| §7 « iVMS-4200 […] sur deux écrans » | Poste Inspiron seulement, caractéristiques et deux moniteurs vidéo non précisés au brief | Les 2 écrans AETHERYS sont affectés à la GTB ; ne pas les compter deux fois. Vérifier décodage simultané, sorties, moniteurs et ergonomie poste de garde. |
| §4 « Octet Plus réalise aussi la fusion et les mesures de la fibre » ; « Cuivre : certification de chaque lien » | Octet : fusion + photométrie incluses ; **pose et certification cuivre exclues** | Pas de contradiction si PROSYB réalise et chiffre réellement le cuivre. OTDR bidirectionnel promis §10 : non démontré par la seule photométrie, à réserver explicitement. Garantie ZVK 25 ans : obtenir conditions et certificat système. |
| §4 « Cuivre Cat. 6A F/STP » puis câble ZVK « F/FTP » | Octet : **F/FTP LSFROH intérieur**, sous fourreau en extérieur | Homogénéiser désignation et déclarer équivalence vis-à-vis du DPGF. Le fourreau ne démontre pas à lui seul l'aptitude à une exposition durable à l'eau ; vérifier parcours et fiche fabricant. |

**Écart SSI à traiter même sans comparaison de quantité AVISS :** le brief retient CONCEPT 3, DM 4710R1, DM étanches 4713R1C, TMS-300 ; le mémoire n'en présente ni nomenclature ni recette dédiée. Le DPGF prévoit les centrales de type 3 et les reports, y compris les liaisons phase 4. Les équipements îlots explicitement « Hors lot » ne dispensent pas PROSYB de ses reports et interfaces.

## 3. Quinze réécritures prioritaires, avec ancres HTML exactes

Les textes « après » sont des propositions de rédaction. Les engagements nouveaux (moyens, financement, délais) doivent être effectivement contractualisés avant remise. Les réserves ci-dessous rendent les écarts visibles ; elles ne rendent pas à elles seules l'offre conforme.

### 1 — P0 / Décrire la GTB réellement proposée

**Avant / ancre exacte :** `WAGO Compact Controller 100 (751-9301)` — remplacer le paragraphe §8 qui contient cette ancre.

**Après :**
> La GTB/GTE proposée est fondée sur l'offre AETHERYS : trois contrôleurs WAGO PFC100 750-8112, un par TGBT Hub, chacun équipé de deux modules DI16 750-1405, d'une terminaison 750-600 et d'une alimentation 787-1212. Les états TOR sont acquis sur entrées physiques, les centrales de mesure en Modbus RS485 et les ASI et groupes électrogènes en Modbus TCP. La liste de points d'exécution validera les adresses, unités, échelles, états de défaut et réserves disponibles. La fourniture de l'interface RS485 nécessaire sera confirmée dans la nomenclature définitive avant commande.

### 2 — P0 / Donner logiciel, rétentions et limites GTB

**Avant / ancre exacte :** `<h2>Supervision</h2>` — remplacer les deux listes qui suivent cette ancre au §8.

**Après :**
> La supervision est assurée par Ignition Edge, licence IGN-EDGE-PANEL-83 avec basic CARE 24 mois et deux clients web concurrents, complétée par le module SME OPALE pour le suivi énergétique. Elle est installée sur un HP ProDesk avec deux écrans iiyama 24 pouces au poste de garde. L'archivage prévu est de 24 mois pour les énergies et de 45 jours pour les alarmes et états, avec une enveloppe annoncée de 10 millions d'enregistrements. L'analyse fonctionnelle fixera les pas d'acquisition, règles d'archivage et modalités d'export ; le dimensionnement sera vérifié avant recette. Les études, la programmation, la recette, la formation et le DOE font partie de la prestation AETHERYS pilotée par PROSYB.

### 3 — P0 / Clarifier 5G et TMA

**Avant / ancre exacte :** `GTB : logiciel de supervision attendu (supervision web des automates ou logiciel tiers) et destinataires des alertes.`

**Après :**
> GTB : validation de la solution Ignition Edge + OPALE, des destinataires et des modalités des alertes SMS/e-mail. L'offre AETHERYS inclut un routeur IXON 5G avec antenne extérieure, un abonnement 5G et une TMA à distance de 24 mois. PROSYB fera préciser les dates de départ et le prix de prolongation jusqu'au terme contractuel d'exploitation. L'accès distant sera soumis au visa informatique d'EXYTE, avec comptes habilités et traçabilité ; son périmètre GTB est distinct de l'option d'accès distant vidéo.

### 4 — P0 / Rétablir le périmètre SSI

**Avant / ancre exacte :** `<li>Courants forts (HTA, TGBT, distribution, éclairage, IRVE) et système de sécurité incendie.</li>`

**Après :**
> Les courants forts (HTA, TGBT, distribution, éclairage, IRVE) sont hors du présent lot CFA. Le SSI décrit au §5 du DPGF est inclus : centrales de type 3 des postes de garde et énergie, déclencheurs et diffuseurs chantier, coffret de report et liaisons vers les équipements îlots, paramétrage et mise en service. Les seuls équipements SSI exclus sont ceux explicitement repérés « Hors lot » au DPGF. La base AVISS comprend CONCEPT 3, DM 4710R1, DM étanches 4713R1C et TMS-300 ; la liste des quantités et la matrice de reports seront soumises au visa. Les essais comprendront chaque déclenchement, chaque report au poste de garde et les défauts définis dans l'analyse fonctionnelle, avec PV.

### 5 — P0 / Rendre visible l'écart switchs

**Avant / ancre exacte :** `Fourniture des switchs du réseau informatique (bureautique) : EXYTE. Leur installation, leur raccordement et leur paramétrage sont compris dans notre offre.`

**Après :**
> Notre hypothèse de chiffrage est une fourniture des switchs informatiques par EXYTE, PROSYB assurant leur installation, raccordement et paramétrage. Cette hypothèse déroge aux ensembles du DPGF mentionnant « incluant switch PoE » ; elle est identifiée dans la matrice C/D/E et doit faire l'objet d'un accord écrit. La nomenclature, les modules optiques et les dates de livraison par phase seront arrêtés avec EXYTE ; une solution avec fourniture PROSYB sera chiffrée pour permettre la comparaison sur un périmètre complet.

### 6 — P0 / Retirer la garantie injustifiée de fonctions vidéo

**Avant / ancre exacte :** `Les analyses intelligentes des caméras (franchissement de ligne, intrusion de zone, filtrage humain / véhicule) sont reconnues nativement par l'enregistreur et par le logiciel : pas de passerelle, pas de licence tierce, pas de perte de fonctions entre la caméra et l'écran de l'opérateur.`

**Après :**
> La compatibilité sera justifiée par une matrice des événements entre les caméras DS-2CD1643G2-LIZSU, le NVR et iVMS-4200, avec les versions matérielles et logicielles retenues. La classification humain/véhicule ne vaut pas validation du franchissement de ligne ou de l'intrusion de zone sur 28 voies. La limite d'analyse périmétrique du NVR annoncée au brief fournisseur est de deux voies 4 MP ; le traitement des autres voies reste à démontrer. La recette vérifiera, pour chaque zone surveillée, la détection, la transmission de l'alarme, l'affichage associé et l'enregistrement. Les compléments nécessaires seront identifiés et chiffrés avant engagement de conformité.

### 7 — P0 / EPI : annoncer le véritable statut

**Avant / ancre exacte :** `<td>28 caméras sur mâts, réseau PoE, NVR, analyse intrusion et port des EPI</td>`

**Après :**
> 28 caméras sur mâts, réseau PoE, NVR et supervision locale. L'analyse périmétrique sur l'ensemble des voies et l'analyse du port des EPI demandées au DPGF font l'objet de points ouverts dans la matrice de conformité : la sélection matérielle disponible ne démontre pas ces deux fonctions. Leur solution technique, leur prix et leurs conditions d'utilisation seront explicités avant remise de l'offre définitive.

**Correction associée :** remplacer aussi le paragraphe « Analyse du port des EPI » ; un mode statistique ne doit pas être présenté comme une fonction livrée ou une validation de conformité juridique. Faire valider finalité et modalités par le responsable de traitement.

### 8 — P0 / Dimensionner le stockage au lieu de présumer sa compatibilité

**Avant / ancre exacte :** `1 disque de 20 To (HW-SP-HDD-SATA-20TB) : environ 15 jours de conservation (estimation AVP : 18 à 22 To) ; extension possible par ajout de disques dans les baies libres du NVR`

**Après :**
> Base de calcul proposée : 28 caméras 4 MP en continu, débit plafonné à 4 Mbit/s par caméra, soit 18,144 To décimaux pour 15 jours de vidéo, avant réserve d'exploitation. Le disque 20 To initialement sélectionné reste soumis à confirmation de compatibilité avec la variante exacte du NVR, le brief fournisseur annonçant 16 To maximum par baie. La nomenclature finale précisera les disques approuvés et la capacité utile après formatage et éventuelle redondance. La durée contractuelle sera validée par EXYTE, puis vérifiée par le débit mesuré et le contrôle des séquences conservées.

### 9 — P0 / Micros compatibles et déviation explicite

**Avant / ancre exacte :** `La DPGF mentionne un kit de 5 micros déportés. La Rally Bar accepte au maximum 4 Rally Mic Pod (donnée constructeur Logitech) : nous retenons 4 micros déportés, qui s'ajoutent aux 6 micros intégrés de la barre et couvrent les tables de réunion des modules.`

**Après :**
> Le DPGF exige cinq microphones déportés par salle. La variante Rally Bar proposée retient quatre Rally Mic Pod compatibles, en remplacement des microphones MeetUp LOG025 figurant dans les données du devis fournisseur. Cette variante constitue une déviation quantitative à approuver ; les microphones intégrés à la barre ne remplacent pas le cinquième microphone déporté exigé. L'acceptation sera fondée sur un essai d'intelligibilité à chaque place dans la salle type. À défaut d'accord, une solution compatible avec cinq microphones déportés sera proposée et chiffrée.

### 10 — P1 / Fermer les achats AV absents

**Avant / ancre exacte :** `Les licences Navori sont attachées à chaque lecteur, sans abonnement cloud ni accès internet.`

**Après :**
> La configuration Navori proposée est locale. La nomenclature et le devis révisé préciseront le serveur QL, ses ressources et sauvegardes, les seize lecteurs et licences, leur durée, la maintenance et les conditions d'activation hors ligne pendant toute l'exploitation. Le serveur n'est pas chiffré dans les données fournisseur disponibles ; ce point reste à fermer avant remise. Les trois totems feront également l'objet d'un prix et d'une validation de compatibilité avec l'écran Samsung OHDX retenu, la gamme de supports annoncée visant initialement OH55F.

### 11 — P1 / Ne plus affirmer un BPU absent

**Avant / ancre exacte :** `<tr><td>BPU et options complets</td><td class="ok">Oui</td><td>Déplacement ou ajout de caméra au prix unitaire ; caméra PTZ et barrière infrarouge en option</td></tr>`

**Après :**
> BPU et options : à compléter et à joindre. Le bordereau distinguera étude de couverture, caméra fixe, PTZ, détecteur/barrière IR, NVR, supervision et licences par mois, maintenance par mois, déplacement de caméra et astreinte de levée de doute. La qualification en option des PTZ et barrières IR reste soumise au besoin de couverture et aux exigences du CCTP. Les interfaces et prix des supports, massifs et déplacements seront explicités.

### 12 — P1 / SLA mesurable

**Avant / ancre exacte :** `<h2>Niveaux de gravité et délais</h2>` — insérer après le tableau existant.

**Après :**
> Pour les incidents critiques, les délais de quatre heures d'arrivée sur site et de huit heures de rétablissement, y compris provisoire, courent en heures calendaires à compter du premier signalement à l'astreinte ou de l'alarme prise en charge par PROSYB ; ces heures sont enregistrées au ticket. Les délais majeurs et mineurs sont comptés en heures ou jours ouvrés selon le tableau. Le rétablissement provisoire décrit le service effectivement restauré et fait l'objet d'une validation EXYTE. Le plan d'astreinte, la suppléance, les habilitations d'accès et l'inventaire des pièces réservées au chantier sont joints à l'offre. L'objectif mensuel de disponibilité de 99 % est suivi séparément pour la vidéo, la GTB et le réseau : disponibilité = (temps de service convenu − durée d'indisponibilité du service) / temps de service convenu. Les fenêtres de maintenance et causes externes sont définies avec EXYTE et restent visibles au rapport mensuel.

**Condition :** financer et joindre ces annexes avant d'utiliser ce texte. 99 % sur 30 jours à service 24/7 autorise 7 h 12 d'indisponibilité ; un incident de 8 h dépasserait déjà ce budget. L'objectif et le délai de rétablissement sont donc deux mesures distinctes.

### 13 — P1 / Limiter la promesse ERPS au scénario vérifié

**Avant / ancre exacte :** `la coupure d'une fibre, fréquente sur un chantier, ne coupe aucun répartiteur ; le trafic repart par l'autre sens en moins de 50 ms (protocole ERPS, ITU-T G.8032).`

**Après :**
> l'anneau est conçu pour maintenir la desserte après la coupure simple d'une liaison, sous réserve de la continuité du chemin retour et de la compatibilité des équipements. L'objectif de convergence est inférieur à 50 ms ; sa tenue sera vérifiée sur la configuration installée, par coupure contrôlée et mesure des pertes. Le PV distinguera coupure de liaison, perte d'un switch et perte d'alimentation ; ces scénarios n'offrent pas la même résilience.

### 14 — P1 / Renforcer DOE et visa Haskoning

**Avant / ancre exacte :** `Plans de récolement, synoptiques, plan d'adressage IP, rapports de recette, configurations sauvegardées, fiches techniques, notices, comptes utilisateurs remis, garanties. Le DOE est mis à jour à chaque phase et à chaque modification.`

**Après :**
> Le DOE est actualisé à chaque phase et modification : plans de récolement, synoptiques, adressage, rapports de recette, configurations et programmes sources relevant de notre prestation, procédures de sauvegarde et de restauration, licences et durées de droits, fiches techniques, notices, garanties et registre des actifs avec référence, numéro de série et localisation. Les comptes et secrets sont transférés par un canal sécurisé. Les documents destinés à KDC sont fournis en anglais, avec les pièces françaises requises. Le registre des soumissions indique référence, révision, responsable, date de visa et statut ; les corrections de statut 3 ou 4 sont resoumises dans les cinq jours prescrits. Les procédures de reprise après perte du NVR, d'une caméra et de la supervision GTB sont jointes.

### 15 — P1 / Remplacer l'affirmation générale d'expérience par des preuves

**Avant / ancre exacte :** `PROSYB intervient en courants faibles, sûreté et GTB sur des data centers en construction et en exploitation : exigences, rythmes et règles de ces chantiers sont les nôtres.`

**Après :**
> Les références jointes précisent, pour chaque opération de data center présentée, le périmètre réellement exécuté, les dates, les volumes installés, le rôle contractuel de PROSYB et les résultats de réception disponibles. Les CV distinguent l'expérience acquise par les intervenants de celle de l'entreprise. Le chef de projet, son suppléant et les ressources mobilisables par phase sont identifiés dans le plan de charge annexé.

**Condition :** réunir les justificatifs ; si aucune référence PROSYB n'est communicable, présenter seulement l'expérience nominative vérifiable de l'équipe et les moyens effectivement réservés.

## 4. Ce qui manque à la conformité Haskoning / EXYTE

### Dossier de réponse et preuves contractuelles

| Pièce à produire | Fondement / précision | Contenu concret attendu |
|---|---|---|
| Matrice **C/D/E** clause par clause | Demandée au brief ; le SoR §3.5.5 prévoit bien « Comply/Deviate/Exclusion » dans la fiche de soumission, mais ne suffit pas à prouver seul l'exigence d'une matrice complète à l'offre | Document/version/clause, exigence, C/D/E, réponse, référence mémoire/devis/PV, écart, impact prix/délai, responsable et décision. Aucun « C » si fonction non prouvée ; documenter les points ouverts sans inventer une quatrième catégorie officielle. |
| Registre déviations et alternatives | SoR §1.7 et passages sur modifications : approbation écrite et suivi RFI ; §2.52 change control | Switchs EXYTE, quatre micros au lieu de cinq, écran 86 au lieu de 85, F/FTP vs F/STP, intrusion/EPI, massifs, durées des services. Présenter prix de base et variantes comparables, sans cacher les écarts dans les questions finales. |
| **Version FR + EN** | Double offre demandée au brief ; SoR **§3.5.2** impose l'anglais pour les documents lus/visés par KDC, avec exceptions françaises | Mémoire, conformité, offre et annexes cohérentes en deux langues ; traductions et gestion des indices. Dix modèles d'affichage bilingues ne constituent pas une offre EN. |
| **Validité ≥90 jours** | Exigence du brief, non retrouvée telle quelle dans le SoR fourni | Clause explicite à compter de la remise et date d'expiration. Achats à sécuriser : Octet jusqu'au 31/10, CCF jusqu'au 27/10 avec prix révisables, Sonepar AV jusqu'au 31/10 selon brief. La validité PROSYB requiert confirmation des prix ou provision de risque ; ne pas transposer 90 jours aux fournisseurs par simple déclaration. |
| ISO **9001/14001** | Exigence du brief ; ces références exactes n'ont pas été retrouvées dans le SoR fourni | Certificats valides avec périmètre et titulaire. Distinguer PROSYB, sous-traitants et fabricants ; signaler absence et demander acceptation du dispositif qualité/environnement proposé. |
| Registre **EPD** | SoR **§2.7**, si requis par contrat/objectifs environnementaux/réglementation | EPD valides, indicateurs et vérifications, conformité ISO 14025 / EN 15804 ou équivalent reconnu ; anglais ou traduction certifiée selon texte. Identifier produits soumis et disponibilités ; ne pas affirmer une obligation universelle pour tout appareil électronique. |
| Soumissions et études | SoR **§§2.51, 3.5.3–3.5.5, 3.7–3.8** | Registre, planning de visa et resoumission, AF GTB, liste E/S, architecture, règles d'alarme, calculs réseau/stockage/énergie. Prévoir les cycles de revue dans les 15 jours annoncés pour les premières études et avant achats concernés. |
| DOE et exploitation | SoR **§§4.2.4, 4.7, 4.7.3, 6.1** | Registre actifs au format client, licences/programmes/sauvegardes, procédures de reprise CCTV/GTB, fréquence de maintenance, délais/codes alarmes ; planning détaillé de maintenance au moins huit semaines avant réception provisoire selon §6.1.1. |
| Applicabilité du SoR au provisoire | Le SoR couvre le data center complet, pas uniquement cette base vie | Faire acter les exigences transposées au lot temporaire : notamment RAM §3.11 et garanties de conception §4.4 (Security/Controls : 10 ans dans le SoR). Ne pas promettre automatiquement la résilience ou les garanties de l'installation permanente ; ne pas les écarter silencieusement non plus. Comparer avec §13 du mémoire : « 1 an pièces et main-d'œuvre », « 2 ans sur les pièces ». |
| Planning / moyens / approvisionnements | Brief et incohérences internes | Départ et fin par phase, mois d'exploitation, prise d'effet TMA/5G/CARE, réemploi et dépose ; effectifs et suppléants, confirmations écrites de stock/délai et attestation de garantie système ZVK. Renseigner `[ DEV_PSB26xxxx ]` et `[ date ]`. |

### Checklist vidéo annexe A : remplacer les « Oui » non prouvés

Ce tableau est une **checklist de travail reconstituée à partir du brief**, pas une reproduction certifiée de l'annexe originale. Les essais jour/nuit et d'intrusion sont déjà prévus §10 : il manque surtout leurs critères, leur traçabilité et certaines fournitures.

| Contrôle | État du mémoire | Pièce / décision manquante pour fermer le point |
|---|---|---|
| Implantation sur PIC EXYTE, couverture accès et zones sensibles | Plan AVP et plans de principe ; étude promise | PIC à jour, ID caméra, hauteur, focale, cible DORI par zone, portée nocturne, obstacles et masquages ; version visée. Le nombre 28 ne prouve pas l'absence d'angles morts. |
| Caméras fixes / PTZ / IR | Fixes hybrides décrites ; PTZ en option | Justification de chaque technologie et exigence fonctionnelle ; PU PTZ, besoin et couverture approuvés. |
| Intrusion / barrières / périmètre | Analyse vidéo annoncée | Matrice d'événements par voie, limites NVR, détection démontrée sur chaque zone, complément IR et anti-sabotage selon besoin. |
| Supervision et levée de doute | Local iVMS décrit en détail | Démonstration de l'ouverture automatique, caméras voisines, acquittement/commentaires et export du journal ; ces fonctions précises ne sont pas prouvées par une capture reconstituée. |
| Notification garde / astreinte | E-mail EXYTE et poste garde | Test hors heures ouvrées, destinataires/suppléants et procédure d'escalade. Fonctionnement local des alarmes si réseau EXYTE/SMTP indisponible. Distinguer astreinte technique et prestation de levée de doute. |
| Enregistrement / conservation | 15 jours estimés, 20 To non validés | Débit maximal, capacité utile et réserve, compatibilité HDD, effacement, test de relecture, comportement disque défaillant et procédure de remplacement. |
| Comptes nominatifs et traçabilité | Profils définis | Vérifier réellement la restriction « dernières 24 heures », droits d'export/maintenance et logs sur versions retenues ; période de conservation des journaux et procédure de retrait des droits. |
| RGPD / affichage / extraction | Principes présents | Dossier destiné au responsable de traitement : finalités, périmètre, masquages, signalétique, habilitations, procédure de demande/export et validation des durées. Le mémoire présente « limite légale d'un mois » comme règle générale : formulation à faire valider selon le régime applicable, sans la considérer ici juridiquement établie. Désactiver l'audio si non justifié et non validé. |
| Robustesse / vandalisme | IP67 et pose hors portée | Fiches exactes, justification chocs/corrosion, accessoires et boîtes de raccordement adaptés, fixations/tenue au vent et protections surtensions/terre. Ne pas attribuer IK10 à la caméra. |
| Alimentation critique / phase 1 GE | Départs secourus évoqués | Schéma source → alimentation 48 V → PoE → caméra, NVR et poste ; bilan de puissance, autonomie chiffrée validée, essai de perte secteur/GE. Résoudre la couverture initiale si vidéo seulement en phase 3. |
| Autonomie internet / accès distant | Principe local cohérent | Procès-verbal de fonctionnement sans internet ; architecture et autorisation VPN, séparation IXON GTB/vidéo et coût éventuel de service vidéo. |
| Mâts / supports / massifs | Massifs GC conformément au DPGF | Arbitrage écrit CCTP/DPGF, limites de fourniture/pose et responsabilité des calculs ; confirmer 28 mâts et accessoires dans les achats. |
| Maintenance et délais | 4 h / 8 h et préventif mensuel annoncés | Plan d'astreinte financé, stock nominatif, preuves contractuelles des sous-traitants, calendrier des visites et format du rapport mensuel. |
| Essais et DOE | Essais caméra par caméra, nuit et intrusion déjà prévus | Cahier avec résultat attendu par caméra, scénario alarme, vidéo associée, alimentation/réseau dégradés, extraction et signatures. DOE avec plans, architecture, fiches, dossier RGPD, procédures et PV. |
| BPU complet / options | Affirmé mais non fourni dans le TSV | Lignes et prix étude, fixes, PTZ, IR, NVR, supervision/licences/mois, maintenance/mois ; déplacement caméra et astreinte de levée de doute en options identifiées. Le §8 global ne remplace pas ces lignes. |

**Incohérence de plans à lever :** boucle §4 du TSV : Est 1, Est 2, Ouest 1, Ouest 2, **Ouest 3**, alors que les répartiteurs listés et le mémoire visent **Est 3**. Émettre RFI avec plan de repérage ; ne pas acheter une desserte sur une correction implicite.

## 5. Value engineering défendable

Aucun gain financier ferme ne peut être annoncé avec le TSV non valorisé et sans devis originaux. Présenter chaque variante avec conformité, preuve technique, investissement, coût sur toute la durée et décision EXYTE.

| Priorité / piste | Variante défendable | Conditions de validation / économies à démontrer |
|---|---|---|
| **1 — Réduire les erreurs d'achat AV** | Remplacer LOG025 par micros compatibles avant commande ; ensemble écran/support approuvé. Faire comparer un écran 85 pouces avec support homologué à l'ensemble 86 pouces réellement compatible. | Évite rachat et reprise ; comparer panier complet et délai, pas seulement prix écran. Variante quatre micros uniquement après accord et essai acoustique, sinon conserver cinq déportés avec autre architecture. |
| **2 — Disques vidéo compatibles plutôt qu'un 20 To incertain** | Plusieurs disques validés ≤ limite confirmée : par exemple **2 × 12 To** si approuvés, capacité utile sans redondance à vérifier ; variante **3 × 12 To en RAID5 uniquement si NVR compatible**. | Comparer capacité utile et coût. Ne pas supposer le RAID disponible. RAID ne remplace pas sauvegarde d'extraits ; 2 disques agrégés n'offrent pas de continuité après panne. |
| **3 — Plafonner le débit, pas dégrader aveuglément l'image** | H.265 avec profils débit/IPS adaptés à chaque scène ; comparer continu de base et variante événementielle là où acceptée. | Tester scène nocturne et mouvement rapide, maintenir la cible de reconnaissance et la durée de conservation. H.265+ ne garantit pas un débit moyen fixe. Tout changement du mode continu doit être accepté explicitement. |
| **4 — Dimensionner l'analyse intrusion là où elle protège** | Comparer caméras produisant les événements requis nativement à des barrières IR sur secteurs sensibles + vidéo de levée de doute. | Chiffrer les 28 voies nécessaires et les fausses alarmes, maintenance et essais ; ne pas étendre la limite des 2 voies NVR par argument commercial. EPI traité séparément avec statut clair. |
| **5 — Conserver le réseau terrain partagé par VLAN** | Mutualiser les huit switchs terrain pour vidéo, GTB et affichage comme prévu, avec séparation du réseau bureautique EXYTE. | Valider PoE, ports libres, fibre, QoS, filtrage et impact d'une panne. Éviter une seconde fourniture de coffrets déjà SPIE ; pas d'économie sur les protections et l'alimentation nécessaires. |
| **6 — Supprimer le surdimensionnement du poste de garde** | Comparer les switchs locaux 2,5 GbE PoE proposés à un modèle Gigabit administrable suffisant, après inventaire des équipements réellement alimentés en PoE. | Budget PoE, ports, débit d'enregistrement, administration et uplinks doivent rester conformes. Le NVR réseau transporte au plus le débit agrégé dimensionné ; un port 2,5 GbE ne justifie pas à lui seul son surcoût. Pas de prix économisé sans contre-offre. |
| **7 — Navori : limiter l'extension au besoin contractuel** | Base six afficheurs extérieurs ; option diffusion HSE sur dix écrans de réunion si ce service n'est pas exigé ailleurs. Comparer serveur local dédié et ressources locales existantes autorisées. | Le TSV §4 ne démontre pas l'obligation de 16 lecteurs : faire confirmer le besoin. Économie possible lecteurs/licences/switchs mais suppression d'une fonction annoncée, à présenter en variante explicite. Maintenir diffusion locale sans internet. |
| **8 — Supports d'affichage plus simples** | Privilégier supports sous auvents aux totems lorsque visibilité et usages permettent, après validation des six emplacements. | Comparer prix, protection, vent, accès maintenance et coût de déplacement ; ne pas remplacer les totems de contrôle d'accès indispensables par un affichage mal visible. |
| **9 — Réemploi réel et stock ciblé** | Tableau de réemploi des baies/AP/ensembles mobiles ; stock de rechange choisi selon criticité, standardisation des huit switchs de zone et alimentations. | Distinguer 84 poses d'AP du nombre d'AP à acheter, 480 liens cumulés du parc phase 4. Le spare L3 est annoncé inclus §3 mais « option » dans le tableau : choisir un statut, financer stock et configuration de secours pour tenir 8 h. |
| **10 — GTB : coût de possession complet** | Négocier dès la commande extension TMA/5G/CARE jusqu'à la date de fin retenue, éventuellement activations par phase. Garder deux clients concurrents si les usages le permettent. | Ne pas confondre contrat 24 mois et conservation énergétique 24 mois. Vérifier fin de support, accès simultanés, coûts SMS/volume 5G, export des données à la dépose et renouvellements ; comparer sur 28/29 mois réellement contractuels. |
| **11 — Visites préventives coordonnées** | Visite mensuelle multi-domaines et opérations trimestrielles regroupées, avec comptes rendus communs et préparation des pièces. | Conserver fréquences vidéo et tests prescrits, financer temps réel, nacelle et déplacement. L'optimisation vient du regroupement, pas d'une réduction cachée des passages. |

## Décisions à fermer avant remise

1. **Base technique complète :** SSI, propriété des switchs, chaîne intrusion/EPI, stockage compatible, achats AV corrigés et GTB AETHERYS à jour.
2. **Base économique cohérente :** révision fournisseurs, manquants, durée des licences/TMA/5G, astreinte/stock, BPU vidéo et financement des recettes PROSYB (cuivre et OTDR à expliciter).
3. **Dossier de preuve :** matrice et déviations, version anglaise, validité 90 jours, annexes de moyens/références, checklist avec preuves et planning visé. Ne plus écrire « Oui » quand seule une intention est disponible.

L'estimation « environ 436 k€ HT avant AETHERYS » du brief n'est pas un total validé. Ne pas ajouter mécaniquement 28 714 € à cette base sans retirer le poste GTB antérieur et compléter les interfaces/main-d'œuvre. Clarifier aussi la convention financière : **PV = PR × 1,4444 correspond à une marge sur vente de 30,77 %**, et **× 1,3506 à 25,96 %**, pas à une marge sur vente de 20 %. Un objectif de 20 % sur vente donnerait ×1,25 si le PR contient tous les coûts. Les coefficients peuvent intégrer frais/risques : expliciter cette ventilation avant de conclure à une erreur de prix ou de modifier le chiffrage.
