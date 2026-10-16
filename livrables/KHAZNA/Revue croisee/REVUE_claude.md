# Revue Claude — mémoire v1.3 (indépendante de Codex)

## Bloquants (risque de note ou de non-conformité)
1. **SSI absent du mémoire alors que le lot 5 SSI est chiffré** (coffret de reports, 4 centrales type 3, 16 DM chantier, 12 diffuseurs, liaisons CR1-C1). Pire : § 12 « Hors de notre prestation » cite « système de sécurité incendie ». Contradiction directe avec la DPGF et la FCI. → Ajouter un chapitre SSI (équipements AVISS CONCEPT 3 / DM 4710R1 / DM étanches 4713R1C / TMS-300, câbles CR1-C1, reports au poste de garde, essais + PV, interface coordinateur SSI, centrales type 4 des îlots hors lot) et corriger § 12 (« hors : SSI des modules / centrales type 4 des îlots »).
2. **Détection intrusion surdéclarée** : la fiche DS-2CD1643G2-LIZSU ne liste que « Motion detection (human & vehicle), video tampering, exception » — pas de franchissement de ligne ni d'intrusion de zone. Le NVR K4 ne fait la protection périmétrique que sur 2 voies 4 MP. Le mémoire (§ 7 + annexe A) promet « franchissement de ligne, intrusion de zone » sur les caméras périmétriques et « analyse du port des EPI ». → Soit variante caméra AcuSense (demande CCF), soit reformuler en « détection de mouvement 2.0 filtrée humain / véhicule par zone » et retirer l'EPI (ou le mettre en option chiffrée).
3. **Stockage vidéo** : 1 seul disque 20 To ; fiche NVR = 16 To max par baie → compatibilité non garantie et point unique de panne. → 2 × 10 To (ou 4 × 8 To), conservation 15 j confirmée par calcul (28 × 3,5 Mbit/s ≈ 1,06 To/j → 15 j ≈ 16 To).
4. **GTB non alignée sur AETHERYS** : WAGO CC100 751-9301 → PFC100 750-8112 + DI16 750-1405 + alim 787-1212 ; supervision Ignition Edge + module SME OPALE ; 2 clients web concurrents ; archivage énergie 24 mois (≥ durée chantier si disque suffisant), états/alarmes 45 j ; routeur IXON 5G + TMA à distance ; ASI et GE en Modbus TCP, centrales en Modbus RS485 ; question n° 6 à retirer.
5. **Accès internet** : le routeur 5G AETHERYS contredit « aucun accès internet direct ». → Le décrire comme lien de télémaintenance VPN sortant, VLAN 910, activable/désactivable par EXYTE, journalisé.

## Incohérences à corriger
- Durées : « 29 mois » (chantier) / « 28 mois » (maintenance DPGF) / TMA AETHERYS 24 mois → harmoniser : 29 mois de chantier, 28 mois d'exploitation-maintenance, TMA GTB prolongée à 28 mois.
- Switch L3 S57244-B0 : typologie dit « 24 ports 1 Gbit/s PoE+ » alors que c'est 24 × SFP 1 Gb + 4 SFP+ (non PoE). « Double alimentation » non vérifiée.
- Fibre « Corning SMF-28 Ultra » : non présente au devis Octet Plus (fiche illisible) → retirer ou « à confirmer ».
- Câble cuivre : F/FTP (Octet Plus) vs F/STP (DPGF) → écrire « F/FTP, blindage par paire + écran global, équivalent ou supérieur au F/STP demandé ».
- Cordons : « S/FTP LSZH » vs devis ACNCORFTPC6A1M « FTP » → aligner.
- Chariot Chief « 50-85" » avec écran 86" → mentionner validation constructeur ou chariot XL.
- Totems ERARD OUTDOOH conçus pour Samsung OH55F → compatibilité OHDX à confirmer (ou totem dédié OHDX).
- Page de garde : N° d'offre et date de remise en placeholder.

## Manques Haskoning / EXYTE
- Matrice de conformité C/D/E clause par clause (R-19) + liste des déviations/alternatives (R-8, R-9).
- Offre finale FR + EN.
- Validité ≥ 90 jours (devis fournisseurs à 27-31/10).
- ISO 9001 / 14001, EPD : dire ce que PROSYB a ou propose.
- Organigramme (R-17) et planning détaillé (R-4) : présents partiellement.

## Value engineering défendable
- Coef GTB : appliquer un coef de sous-traitance (≈ 1,20) sur la partie AETHERYS plutôt que 1,44 → –8 k€ environ sur le lot 7.
- Bornes Wi-Fi : aligner sur le standard EXYTE (évite double contrôleur).
- Spare L3 en option (déjà fait).
