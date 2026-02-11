# mini-projet-pere-noel

Une simulation de la fabrique du Père Noël utilisant les design patterns pour une architecture flexible et robuste.

## Patterns implémentés

Le projet utilise 6 patterns clés :

- Singleton pour une instance unique pour la WorkFacade et le NotificationService.
- Factory avec FactoryGift qui gère la création dynamique des cadeaux (livres, bijoux, ...).
- Abstract Factory qui gère la céation de packs thématiques cohérents (cadeau + livraison adaptée).
- Decorator qui permet d'empiler des options (emballage, ruban, message) sans modifier les classes de base.
- Strategy qui rend interchangeable le mode de livraison (rennes, traineau, drone).
- Observer dans le NotificationService qui prévient automatiquement tous les Lutins.


## Installation et utilisation 
- Prérequis : Python.
- Lancement :
```bash
python main.py
```
### Menu principal

 - Option 1 (Commande personnalisée) : choisir votre cadeau, empilez les décorations (ex: 1,2,3) et sélectionnez un mode de livraison.
 - Option 2 (Pack thématique) : utilise l'Abstract Factory pour générer instantanément un pack complet (traditionnel ou moderne).
  

## Gestion des Erreurs

Le projet inclut des exceptions personnalisées (SantaError, GiftCreationError) pour éviter les crashs si un type de cadeau est inconnu ou si une saisie est invalide.