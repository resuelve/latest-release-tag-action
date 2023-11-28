import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime

token = os.environ.get("INPUT_GITHUB_TOKEN")
pattern = os.environ.get("INPUT_REGEX")

repo = os.environ.get("GITHUB_REPOSITORY")
api_url = os.environ.get("GITHUB_API_URL")

url = f"{api_url}/repos/{repo}/releases"

request = urllib.request.Request(url)

request.add_header("User-Agent", "bot")
request.add_header("Accept", "application/vnd.github+json")
request.add_header("Authorization", f"Bearer {token}")

with urllib.request.urlopen(request) as response:
    # TODO: add error handling for request
    releases = json.loads(response.read().decode("utf-8"))
    filtered = []
    for release in releases:
        if re.search(pattern, release["tag_name"]):
            filtered.append(release)

    filtered = sorted(
        filtered,
        key=lambda x: datetime.fromisoformat(
            x["published_at"][: len(x["published_at"]) - 1]
        ),
        reverse=True,
    )

    if not filtered:
        sys.stderr.write(f"There is no tag that match {pattern}\n")
        sys.exit(1)

    tag_name = filtered[0]["tag_name"]
    with open(os.path.abspath(os.environ.get("GITHUB_OUTPUT")), "a") as f:
        f.write(f"tag={tag_name}")

        sys.stdout.write(f"{tag_name} exported!")
