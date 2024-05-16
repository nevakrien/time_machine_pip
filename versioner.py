import requests
from datetime import datetime

def get_version_before_cutoff(package_name, cutoff_date):
    """Fetches the latest version of a package released before a specific cutoff date."""
    api_url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(api_url)
    data = response.json()
    releases = data['releases']
    
    latest_version = None
    latest_release_date = None

    cutoff_datetime = datetime.strptime(cutoff_date, "%Y-%m-%d")

    for version, uploads in releases.items():
        for upload in uploads:
            release_date = datetime.strptime(upload['upload_time'][:10], "%Y-%m-%d")
            if release_date <= cutoff_datetime:
                if latest_release_date is None or release_date > latest_release_date:
                    latest_version = version
                    latest_release_date = release_date

    return latest_version

if __name__=="__main__":
    # Example usage
    package = 'numpy'
    cutoff = '2020-01-01'
    version = get_version_before_cutoff(package, cutoff)
    if version:
        print(f"The latest version of {package} before {cutoff} is {version}")
    else:
        print(f"No versions of {package} are available before {cutoff}.")
