from github import Github

def rechercher_depots(keywords, max_repos=500):
    g = Github("API_KEY")  # Remplace par ton propre jeton d'accès GitHub

    # Recherche des dépôts contenant les mots-clés spécifiés avec une limite de max_repos
    repos = g.search_repositories(query=f"{keywords} in:description", sort='stars', order='desc')[:max_repos]

    resultats = []

    for repo in repos:
        kubernetes_files = repo.get_contents("")  # Modifier le ref si le nom de la branche est différent de "master"
        kubernetes_present = False

        for file in kubernetes_files:
            if file.type == 'file' and ("/k8s/" in file.path or file.path.endswith('.yaml') or file.path.endswith('.yml') or file.path.endswith('.k8s')):
                # Identifier les fichiers typiques de Kubernetes par leur chemin ou leur extension YAML ou .k8s
                kubernetes_present = True
                break

        if kubernetes_present:
            resultats.append({
                'nom': repo.full_name,
                'description': repo.description,
                'url': repo.html_url
            })

    return resultats

# Exemple de recherche de dépôts GitHub avec des mots-clés spécifiques et vérification des fichiers Kubernetes
resultats = rechercher_depots('microservices', max_repos=750)

# Écriture des résultats dans un fichier texte
with open('resultats_depots_kubernetes.txt', 'w', encoding='utf-8') as fichier_resultats:
    for repo in resultats:
        fichier_resultats.write(f"Nom du dépôt : {repo['nom']}\n")
        fichier_resultats.write(f"Description : {repo['description']}\n")
        fichier_resultats.write(f"URL : {repo['url']}\n")
        fichier_resultats.write("\n")
