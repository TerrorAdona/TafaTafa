---
name: special-char-filter-chatbot
description: Filtrage automatique des caractères spéciaux dans les réponses du chatbot pour améliorer l'affichage
metadata:
  type: project
---

## Filtrage automatique des caractères spéciaux dans les réponses du chatbot

### Fonctionnalité ajoutée
Toutes les réponses du chatbot sont maintenant analysées et certains caractères spéciaux sont automatiquement supprimés pour améliorer l'affichage et la lisibilité.

### Caractères filtrés
Les caractères suivants sont maintenant supprimés des réponses du chatbot :
- `_` (underscore/souligné)
- `*` (asterisque/étoile)
- `` ` `` (backtick/accent grave)
- `~` (tilde)
- `|` (pipe - déjà présent, converti en saut de ligne)
- `\n` (saut de ligne - déjà présent, conservé pour le formatage)

### Implémentation
Modification dans la fonction `typeWriter()` du fichier `chatbot/templates/chatbot/chat.html` :

```javascript
else if (char === '_' || char === '*' || char === '`' || char === '~') {
    // Remove common special characters used for markdown emphasis
    // Skip displaying these characters
}
```

### Comportement
- Lorsqu'un de ces caractères spéciaux est rencontré dans la réponse du chatbot :
  - Il est tout simplement ignoré et non affiché
  - L'effet de frappe continue normalement avec le caractère suivant
  - Aucun espace vide n'est laissé à la place du caractère supprimé
- Ceci permet de nettoyer automatiquement les réponses qui pourraient contenir de la syntaxe Markdown non désirée

### Exemple
Si le chatbot retourne initialement : `"Ceci est *important_ et ceci \`du code\`~"`
Après filtration, l'affichage sera : `"Ceci est important et du code"`

### Avantages
- Élimine automatiquement les artefacts de formatting Markdown qui pourraient apparaître dans les réponses
- Améliore la lisibilité naturelle du texte affiché
- Fonctionne en complément des autres fonctionnalités :
  - Conversion du '|' en sauts de ligne
  - Effet de frappe réaliste
  - Suppression du curseur après frappe
  - Gestion correcte des sauts de ligne naturels
  - Pas d'écrasement des messages précédents

### Fichiers modifiés
- `chatbot/templates/chatbot/chat.html` - Ajout du filtrage des caractères spéciaux dans l'effet de frappe

Cette fonctionnalité garantit que l'affichage du chatbot reste propre et professionnel, indépendamment de la manière dont le texte est généré côté serveur.