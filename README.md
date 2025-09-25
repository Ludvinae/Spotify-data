# Spotify - Problématiques

Ce projet en **Python** a pour objectif de répondre à différentes problématiques liées à l’analyse de données Spotify.

---

## 1) Mesurer le churn (global + par abonnement)  
**Problème :** La direction veut connaître le taux d’attrition global et par type d’abonnement.  

---

## 2) Détecter les utilisateurs “à risque” (règles métier simples)  
**Problème :** Équipe CRM : repérer les comptes à relancer.  

**Règles métier :**
- Taux de *skip* > 30%  
- Taux d’écoute < 100 min par jour  
- Pour les comptes gratuits :  
  - aucune écoute offline  
  - écoute de pub > 20 par semaine  

---

## 3) Revenu estimé (actifs uniquement) + par pays  
**Problème :** Finance : estimer le MRR de base par plan et par pays (utilisateurs non churnés).  

**Prix des abonnements :**
```python
PRICES = {
    "Free": 0.0,
    "Premium": 9.99,
    "Family": 14.99,
    "Student": 4.99
}
```

---

## 4) Identifier les “power users”

**Problème :** Produit : cibler les gros utilisateurs pour bêta-tests.

**Règles métier :**

* Plus de 200 min d’écoute par jour
* Plus de 50 titres écoutés par jour

---

## 5) Moyenne de pubs écoutées par type d’abonnement

**Problème :** Ads / monétisation : comprendre la pression publicitaire.

---

## 6) Mix des devices par pays (dictionnaires imbriqués)

**Problème :** Équipe growth : savoir quels devices dominent selon les marchés.

---

## 7) Segmentation par tranches d’âge

**Problème :** Marketing : comparer les cohortes d’âge.

**Règles métier :**

* < 20 ans
* 20 - 35 ans
* 36 - 50 ans
* 50+ ans

---

## 8) Histogramme manuel de `skip_rate`

**Problème :** Data : observer la distribution du taux de *skip*.

---

## 9) “User 360” (fiche synthèse par ID) — *bonus*

**Problème :** Support / CSM : afficher une fiche compactée pour un ID donné.

**Exemple d’utilisation :**
En ligne de commande, l’utilisateur donne un ID extrait du document, puis on affiche les infos de l’utilisateur.

---

## 10) Sets : valeurs uniques utiles (pays, plans, devices) — *bonus*

**Problème :** Marketing : lister rapidement l’étendue des marchés et supports.

* Liste des devices uniques
* Liste des pays uniques

---

## Focus Prioritaires

Les problématiques clés à traiter en priorité sont :

1. Mesurer le churn (global + par abonnement)
2. Détecter les utilisateurs “à risque”
3. Moyenne de pubs écoutées par type d’abonnement
4. Mix des devices par pays
5. Segmentation par tranches d’âge
6. “User 360” (fiche synthèse par ID) — bonus

---

