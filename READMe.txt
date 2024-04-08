Objectif
Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant
à travers un ensemble arbitraire de variables, et pouvoir :
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes
de précédence,
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de
précédence.

creation de deux classe :
    -Task : Cette classe est destinée à représenter individuellement chaque tâche .
    -TaskSytem une classe pour rassembler les taches et en creer une systeme.
    -Main pour exécuter le système de tâches.


TaskSystem :

Méthode verifyUniqueNames(self)
-Assure que chaque tâche a un nom unique dans le système.
-La méthode crée une liste de tous les noms de tâches et la compare à un ensemble (unique) de ces noms. Si la longueur de la liste diffère de celle de l'ensemble, cela signifie qu'il y a des doublons.

Méthode verifyTaskNameDep(self)
-Vérifie la cohérence entre les noms des tâches et leurs dépendances.
-Cette méthode vérifie si la clé (nom de tâche) et chaque dépendance existent dans la liste des tâches. Si une incohérence est trouvée, cela donne une erreur.

Méthode draw(self)
-Visualise le graphe des dépendances entre les tâches.
-Utilise networkx pour créer un graphe dirigé, où chaque noeud représente une tâche. Les arcs entre les noeuds représentent les dépendances. Le graphe est ensuite dessiné avec matplotlib.pyplot, affichant les noms des tâches.

Méthode getDependeciesTS(self, task)
-Liste des dépendances d'une tâche donnée
Arguments:
task: L'objet Task pour obtenir les dépendances.
Et retourne la liste des noms des tâches dont la tâche spécifiée dépend.

Méthode getDependencie(self, task)
-Trouve la route de dépendance pour une tâche donnée.
-À travers une série de itérations, cette méthode construit le chemin de dépendances pour la tâche spécifiée, en utilisant l'ordre d'exécution dérivé de la méthode runRoad.

Méthode runseqelementary(self, road)
-Exécute séquentiellement les tâches d'une route spécifique.
-Itère sur la liste des tâches (road) et exécute chaque tâche en appelant sa méthode run.

Méthode runseq(self)
-Exécute toutes les tâches du système de manière séquentielle, en respectant l'ordre défini par les dépendances.
-Utilise runRoad pour obtenir les routes (groupes de tâches pouvant être exécutées séquentiellement sans violer les dépendances) et les exécute une par une en utilisant runseqelementary.

Méthode runsem(self, toeffectue)
-Exécute un groupe de tâches en parallèle.
-Utilise un Semaphore pour limiter le nombre de tâches s'exécutant simultanément et lance un Thread pour chaque tâche. Cette méthode permet une exécution parallèle tout en contrôlant le nombre de tâches actives.

Méthode run(self)
-Exécute toutes les tâches du système en parallèle, tout en respectant leurs dépendances.
-Organise les tâches en routes parallèles avec runRoad et les exécute en parallèle en utilisant runsem.

Méthode runRoad(self)
-Obtient les routes des tâches
-Cette méthode organise les tâches en routes qui peuvent être exécutés en parallèle ou séquentiellement, en respectant toutes les dépendances. Elle prend en compte les tâches déjà effectuées pour dynamiquement ajuster les groupes à chaque itération.

Méthode checkdep(self, task)
-Vérifie et liste les dépendances d'une tâche donnée en fonction des lectures/écritures de données.
-Compare les opérations de lecture d'une tâche aux opérations d'écriture des autres tâches pour identifier les dépendances potentielles basées sur le partage de données.

Méthode createDep(self)
-Génére un dictionnaire de dépendances entre tâches.
-Itère sur chaque tâche, utilise checkdep pour trouver ses dépendances, et construit un dictionnaire mappant chaque tâche à ses dépendances.

Méthode bernsteinIntoEachOverTest(self, tasks)
-Applique le test de Bernstein pour identifier les tâches qui peuvent être exécutées en parallèle sans conflit.
-Examine chaque paire de tâches pour vérifier si elles peuvent s'exécuter en parallèle sans violation de dépendance de données. Retourne deux listes : celles qui passent le test et celles qui ne le passent pas.

Méthode parCost(self, runs=2)
-Compare les performances de l'exécution parallèle et séquentielle.
-Mesure et compare le temps d'exécution pour les modes parallèle et séquentiel sur un nombre spécifié d'itérations (runs). Affiche la différence moyenne de temps pour donner une idée de l'efficacité du parallélisme.

Méthodes printRoad et printRoad2
-Affiche les routes calculées par runRoad.
-Pour printRoad, affiche directement les routes calculées. printRoad2 permet d'afficher des routes spécifiées en argument, offrant une flexibilité pour afficher des configurations de tâches différentes.
-Chaque méthode est conçue pour intégrer les tâches dans un système cohérent où les dépendances sont respectées, offrant à la fois des exécutions séquentielles et parallèles optimisées.

Task: 

Méthode bernstein(self, other_task)
-Détermine si deux tâches sont compatibles selon les conditions de Bernstein, un critère essentiel pour permettre l'exécution parallèle de tâches sans conflit de données.
-La méthode vérifie d'abord si les ensembles de tâches écrites (writes) par les deux tâches se croisent. Si c'est le cas, les tâches ne peuvent pas être exécutées en parallèle car elles tentent d'écrire sur les mêmes ressources.
Ensuite, elle vérifie si une tâche écrit sur une ressource qu'une autre tâche lit, ou inversement. Cela inclut également un potentiel conflit et, par conséquent, ces tâches ne seraient pas compatibles pour une exécution parallèle.
Si aucune de ces conditions de conflit n'est remplie, les tâches sont considérées comme compatibles selon Bernstein, permettant ainsi leur exécution potentiellement parallèle sans risque d'interférence.

Main :

Variables Globales :
Déclaration des variables globales a, b, c, d, et e qui seront modifiées et utilisées par différentes tâches.

Méthode detTestRnd(ts)
-Teste le déterminisme du système de tâches.
-Initialise les variables globales avec des valeurs aléatoires, exécute le système de tâches deux fois avec les mêmes valeurs initiales, et compare les résultats pour déterminer si le système est déterministe (les résultats des deux exécutions sont identiques).


Pour notre projet, la répartition des tâches a été soigneusement planifiée pour s'assurer que chaque membre de l'équipe contribue de manière égale au travail global. Voici comment nous avons organisé notre collaboration :

-Johan : A developper l'idée général et les fonctions principales.
-José : A developper les fonctions parCost, detTestRnd et les vérifications des tasks et Johan a corrigé les problèmes qu'il y pu avoir. Powerpoint + READMe

