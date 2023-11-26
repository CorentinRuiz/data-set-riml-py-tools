from github import Github

def rechercher_depots(keywords, max_repos=500):
    g = Github("API_KEY")  # Remplace par ton propre jeton d'accès GitHub

    # Recherche des dépôts contenant les mots-clés spécifiés avec une limite de max_repos
    repos = g.search_repositories(query=f"{keywords} in:description", sort='stars', order='desc')[:max_repos]

    resultats = []

    for repo in repos:
        try:
            terraform_files = repo.get_contents("") # Modifier le ref si le nom de la branche est différent de "master"
            ansible_present = False
            terraform_present = False

            for file in terraform_files:
                if file.type == 'file' and (file.path.endswith('.tf')):
                    # Identifier les fichiers typiques de Terraform par leur chemin ou leur extension
                    terraform_present = True
                if file.type == 'file' and (file.path.endswith('.ansible') or file.path.endswith('.playbook') or file.path.endswith('.ansiblecfg')):
                    # Identifier les fichiers typiques d'Ansible par leur chemin ou leur extension
                    ansible_present = True

            if ansible_present or terraform_present:
                resultats.append({
                    'nom': repo.full_name,
                    'description': repo.description,
                    'url': repo.html_url
                })
        except Exception as e:
            print(f"Erreur lors de l'accès au dépôt {repo.full_name}: {e}")
            continue

    return resultats

# Exemple de recherche de dépôts GitHub avec des mots-clés spécifiques et vérification des fichiers Ansible et Terraform
resultats = rechercher_depots('microservices ansible', max_repos=300)

# Écriture des résultats dans un fichier texte
with open('resultats_depots_ansible_terraform.txt', 'w', encoding='utf-8') as fichier_resultats:
    for repo in resultats:
        fichier_resultats.write(f"Nom du dépôt : {repo['nom']}\n")
        fichier_resultats.write(f"Description : {repo['description']}\n")
        fichier_resultats.write(f"URL : {repo['url']}\n")
        fichier_resultats.write("\n")
