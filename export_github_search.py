import csv
from github import Github, Auth

# Replace with your Personal Access Token
#GITHUB_TOKEN = "YOUR_TOKEN_HERE"
# https://github.com/grimbough/anaconda-download-stats
# condastats overall  a2wsgi-feedstock acachecontrol-feedstock
# https://github.com/seandavi/BiocPkgTools

# Search parameters
SEARCH_QUERY = 'org:conda-forge path:recipe/meta.yaml "YOUR_USERNAME_HERE"'
#gh api --paginate  "search/code?q=org:conda-forge+'YOUR_USERNAME_HERE'"   --jq '.items[].repository.full_name'

def main():
    auth = Auth.Token(GITHUB_TOKEN)
    g = Github(auth=auth)
    print("Searching...")
    results = g.search_code(query=SEARCH_QUERY)
    total = results.totalCount
    print(f"Found {total} results")
    
    with open('conda_forge_recipes.csv', 'w', newline='') as csvfile:
        fieldnames = ['repository', 'file_path', 'html_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for file in results:
            writer.writerow({
                'repository': file.repository.full_name,
                'file_path': file.path,
                'html_url': file.html_url
            })
            print(f"{file.repository.full_name},{file.path},{file.html_url}")

    print("Export complete: conda_forge_recipes.csv")

if __name__ == "__main__":
    main()
