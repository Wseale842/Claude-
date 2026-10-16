# Prompt de challenge — à coller dans ChatGPT (Mac)

**Pièces à joindre dans ChatGPT** (depuis SharePoint › EXYTE › Data Center KHAZNA › Elec base vie) :
1. `Dossier réponse/Mémoire technique/Memoire_technique_PROSYB_EXYTE_KHAZNA_Courants_faibles_base_vie_v1.2.pdf` (ou la dernière version)
2. `01_DCE BASE VIE CHANTIER v1/3. Chiffrage/FCI_Khazna_CFA_SSI_AV_IT_v3.xlsx`
3. `01_DCE BASE VIE CHANTIER v1/2. Etudes/17. DPGF/` (la DPGF d'origine)
4. `01_DCE BASE VIE CHANTIER v1/2. Etudes/11. SSI/FR02201-ENG-ELEC-DRW-1016-02.pdf`, `13. IT/…1014-01.pptx`, `12. CCTV/…1009-02.pdf` + CCTP lot 03, `14. GTB/…1017-02.pdf`, `7. Plan d'implantation/…1007-02.pdf`
5. `Dossier réponse/Devis fournisseur/` : devis Sonepar 0014640130 (audiovisuel), CCF 313371 (vidéo), AVISS AE2610CO901 (SSI)

---

```
Tu es l'acheteur technique d'EXYTE (entreprise générale) assisté d'un ingénieur courants faibles senior.
Tu évalues l'offre de PROSYB (sous-traitant courants faibles) pour l'électricité provisoire et les courants
faibles de la base vie et du chantier du data center KHAZNA ORY01 à Fouju (77) : VDI/IT, Wi-Fi,
audiovisuel (10 salles de visioconférence, 6 afficheurs extérieurs, diffusion centralisée), vidéoprotection
et détection intrusion (28 caméras Hikvision), reports SSI, GTB/GTE. Exploitation environ 26 mois
(novembre 2026 → décembre 2028), en phases 2, 3 et 4.

Pièces jointes : mémoire technique PROSYB, FCI/DPGF chiffrée, DCE (plans, synoptiques, CCTP lot 03),
devis fournisseurs.

Ta mission : CHALLENGER l'offre sans complaisance. Ne réécris pas le mémoire. Donne-moi :

1. CONFORMITÉ DPGF/DCE — tableau ligne par ligne : ligne DPGF | exigence DCE | réponse PROSYB |
   conforme / écart / manquant | gravité (bloquant, majeur, mineur). Vérifie en particulier :
   - le kit de 5 micros déportés par salle (PROSYB retient 4 Rally Mic Pod : justification recevable ?) ;
   - écran 85" 4K usage pro sur pied mobile, barre visio USB + compatible Microsoft Teams Rooms ;
   - afficheurs 55" IP55 mini, ≥ 1 500 cd/m², 3 muraux antivol + 3 totems lestés couverts ;
   - diffusion centralisée multicast depuis un serveur LOCAL, groupes d'écrans, programmation horaire,
     alertes prioritaires, licences et leur durée sur 26 mois ;
   - reports SSI (synoptique 1016), centrales type 3, DM et diffuseurs chantier ;
   - vidéo : couverture, conservation, RGPD, conformité CCTP lot 03 ;
   - structure de la FCI : trame DPGF respectée à l'identique (lignes, unités, quantités, phases).
2. PRIX — repère les P.U. incohérents ou anormalement bas/hauts (fourniture seule, pose/MO à ajouter),
   les doubles comptes (ex. switchs PoE locaux alors que les switchs de zone sont PoE), les oublis
   (totems, supports antivol, serveur de diffusion, licences au-delà de 12 mois, MO, ports, D3E).
3. TECHNIQUE — risques et points faibles : compatibilité des matériels entre eux (ex. micro d'extension
   MeetUp vs Rally Bar, totem ERARD prévu pour OH55F vs écran OH55D), exploitation 24/7 en extérieur,
   chaleur/soleil, alimentation ondulée, cybersécurité (VLAN, pare-feu), maintenance, repli.
4. SYNOPTIQUES ET PLANS — les synoptiques et plans d'implantation du mémoire sont-ils clairs,
   complets (tous les équipements, liaisons, références de câbles, phases) et cohérents avec le DCE ?
   Liste ce qui manque.
5. QUESTIONS qu'EXYTE poserait en réunion de négociation (10 maximum), classées par priorité.
6. TOP 10 des corrections à faire AVANT remise, actionnables, par ordre d'impact sur la note.

Sois factuel : cite la page ou la ligne du document. Si une information manque, dis-le au lieu
de supposer.
```

---

**Retour** : colle la réponse de ChatGPT dans la conversation Claude ; je trie ce qui est fondé, je corrige le mémoire, la FCI et les plans, et je te dis ce que je rejette et pourquoi.
