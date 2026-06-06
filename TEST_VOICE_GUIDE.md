# Guide de test de la saisie vocale pour TafaTafa

## Prérequis
1. Navigateur compatible : Google Chrome, Microsoft Edge, ou Opera (Safari partiellement supporté)
2. Microphone fonctionnel et autorisé
3. Connexion internet stable

## Étapes de test

### 1. Vérification initiale
- Ouvrez votre chatbot TafaTafa
- Vous devriez voir un nouveau bouton avec l'icône 🎤 à côté du champ de saisie
- Au survol, le titre devrait afficher "Entrée vocale"

### 2. Test de base
1. Cliquez sur le bouton 🎤
2. Le bouton devrait devenir rouge avec l'icône 🔴 et afficher "Écoute en cours..."
3. Parlez clairement dans votre microphone : "Bonjour, comment allez-vous ?"
4. Après avoir fini de parler, le texte devrait apparaître dans le champ de saisie
5. Le bouton devrait revenir à son état normal (🎤)

### 3. Test avec ponctuation
Essayez de dire :
- "Quel temps fait-il aujourd'hui point d'interrogation"
- "Je veux savoir comment faire une pause virgule puis continuer"
- "Aller à la ligne retour chariot nouveau paragraphe"

### 4. Gestion des erreurs
Testez ces scénarios :
- Refuser l'accès au microphone lorsque le navigateur les demande
- Débrancher votre microphone pendant l'utilisation
- Utiliser un navigateur non compatible (Firefox par exemple)

### 5. Intégration avec l'envoi
1. Utilisez la saisie vocale pour entrer un message
2. Cliquez sur "Envoyer" ou appuyez sur Entrée
3. Vérifiez que le message est bien envoyé au chatbot
4. Confirmez que vous recevez une réponse

## Dépannage

### Le bouton devient rouge mais rien ne s'écrit
1. Vérifiez que votre microphone fonctionne dans d'autres applications
2. Assurez-vous d'avoir autorisé l'accès au microphone lorsque le navigateur le demande
3. Essayez de parler plus près du microphone
4. Vérifiez les paramètres de confidentialité de votre navigateur pour le site

### Le bouton ne change pas d'apparence
1. Rafraîchissez la page (Ctrl+F5)
2. Vérifiez qu'aucune extension ne bloque JavaScript
3. Essayez en mode navigation privée

### Aucun son n'est capté
1. Testez votre microphone sur [ce site de test](https://www.onlinemictest.com/)
2. Vérifiez les paramètres audio de votre système
3. Essayez un autre microphone si disponible

## Conseils pour une meilleure reconnaissance
- Parlez clairement et à un rythme normal
- Évitez les bruits de fond
- Utilisez un casque avec microphone intégré si possible
- Parlez dans un environnement calme
- Pour la ponctuation, dites explicitement "point", "virgule", "point d'interrogation", etc.

## Notes techniques
- La reconnaissance utilise l'API Web Speech avec la langue française (fr-FR)
- La transcription se fait en temps réel mais n'est affichée qu'après fin de phrase
- Aucun donnée vocale n'est envoyée à nos serveurs - tout est traité localement par le navigateur
- Fonctionne uniquement en HTTPS ou localhost (pour des raisons de sécurité)

Si vous rencontrez toujours des problèmes après ces tests, veuillez consulter la console du navigateur (F12 > Console) pour voir les éventuelles erreurs JavaScript.