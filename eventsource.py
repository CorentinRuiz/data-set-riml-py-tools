from github import Github

def rechercher_librairies_event_sourcing(keywords, max_repos=500):
    g = Github("API_KEY")  # Remplacez par votre propre jeton d'accès GitHub

    resultats = []


        # Recherche des dépôts liés à une technologie spécifique liée à l'event sourcing
    repos = g.search_repositories(query=f"{keywords} in:description", sort='stars', order='desc')[:max_repos]

    for repo in repos:
        # Vous pouvez ajouter des critères supplémentaires pour filtrer les dépôts si nécessaire
        resultats.append({
            'nom': repo.full_name,
            'description': repo.description,
            'url': repo.html_url
        })

    return resultats

# Exemple de recherche de librairies d'event sourcing pour des technologies spécifiques (par exemple, Axon, EventStore, Kafka)
resultats = rechercher_librairies_event_sourcing("microservices kafka", max_repos=750)

# Écriture des résultats dans un fichier texte
with open('resultats_librairies_event_sourcing.txt', 'w', encoding='utf-8') as fichier_resultats:
    for repo in resultats:
        fichier_resultats.write(f"Nom du dépôt : {repo['nom']}\n")
        fichier_resultats.write(f"Description : {repo['description']}\n")
        fichier_resultats.write(f"URL : {repo['url']}\n")
        fichier_resultats.write("\n")