#!/usr/bin/env python3
"""Publish a markdown article to Substack from the command line."""

import json
import os
import sys
from datetime import date

from substack import Api
from substack.post import Post

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(SCRIPT_DIR, ".substack-config.json")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("Missing .substack-config.json. Create it with:")
        print(json.dumps({
            "cookie": "your substack.sid cookie value",
            "publicationUrl": "https://yourname.substack.com"
        }, indent=2))
        sys.exit(1)
    with open(CONFIG_FILE) as f:
        return json.load(f)


def parse_article(filepath):
    with open(filepath) as f:
        lines = f.read().split("\n")

    # First non-empty line is the title
    title = ""
    body_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped:
            # Remove markdown bold ** and heading #
            title = stripped.strip("*").strip("#").strip()
            body_start = i + 1
            break

    # Skip separator lines (--- or empty) after title
    while body_start < len(lines):
        stripped = lines[body_start].strip()
        if stripped == "---" or stripped == "":
            body_start += 1
        else:
            break

    body_markdown = "\n".join(lines[body_start:]).strip()
    return title, body_markdown


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 publish.py <article-file>")
        print("Example: python3 publish.py agents")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        alt = os.path.join(SCRIPT_DIR, filepath)
        if os.path.exists(alt):
            filepath = alt
        else:
            print(f"File not found: {filepath}")
            sys.exit(1)

    config = load_config()
    title, body_markdown = parse_article(filepath)

    print(f"Title: {title}")
    print(f"Body: {len(body_markdown)} chars")
    print("Connecting to Substack...")

    api = Api(
        cookies_string=f"substack.sid={config['cookie']}",
        publication_url=config["publicationUrl"],
    )

    user_id = api.get_user_id()
    post = Post(title=title, subtitle="", user_id=user_id)
    post.from_markdown(body_markdown, api=api)

    print("Creating draft...")
    draft = api.post_draft(post.get_draft())
    draft_id = draft.get("id")
    print(f"Draft created (id: {draft_id})")

    print("Publishing...")
    api.prepublish_draft(draft_id)
    api.publish_draft(draft_id)

    slug = draft.get("slug", "")
    url = f"{config['publicationUrl']}/p/{slug}"
    print(f"Published: \"{title}\"")
    print(f"URL: {url}")

    # Append to published/index.md
    index_file = os.path.join(SCRIPT_DIR, "published", "index.md")
    filename = os.path.basename(filepath)
    summary = body_markdown[:60].replace("\n", " ").replace("|", "/")
    today = date.today().isoformat()
    with open(index_file, "a") as f:
        f.write(f"| {today} | [{title}]({filename}) | {summary}... |\n")


if __name__ == "__main__":
    main()
