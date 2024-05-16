from flask import Flask, request, Response
import requests
from datetime import datetime
import json

from bs4 import BeautifulSoup

app = Flask(__name__)



def get_latest_version(package_name, cutoff_date):
    """Get the latest version of a package before the cutoff date using PyPI's JSON API."""
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    package_data = response.json()
    releases = package_data['releases']

    latest_version = None
    latest_release_date = datetime.min

    # Loop through all versions and find the latest one before the cutoff date
    for version, uploads in releases.items():
        for upload in uploads:
            release_date = datetime.strptime(upload['upload_time'][:10], '%Y-%m-%d')
            if release_date <= cutoff_date and release_date > latest_release_date:
                latest_version = version
                latest_release_date = release_date

    return latest_version


def filter_html_to_latest_version(package_name, latest_version):
    """Filter the HTML page to include only up to the latest version."""
    response = requests.get(f'https://pypi.org/simple/{package_name}/')
    soup = BeautifulSoup(response.text, 'html.parser')

    result_html = ''
    for anchor in soup.find_all('a'):
        if latest_version in anchor['href']:
            result_html += str(anchor) + '<br>\n'
            break  # Stop after adding the latest version
        result_html += str(anchor) + '<br>\n'

    return result_html

@app.route('/<date_string>/<package_name>/')
def proxy_pypi_with_cutoff(package_name, date_string):
    try:
        cutoff_date = datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD.", 400
    
    latest_version = get_latest_version(package_name, cutoff_date)
    if not latest_version:
        return "No valid versions found before the cutoff date.", 404
    
    filtered_html = filter_html_to_latest_version(package_name, latest_version)
    return Response(filtered_html, mimetype='text/html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
