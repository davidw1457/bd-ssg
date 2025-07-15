import os

from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    title = None
    for l in lines:
        if l.startswith("# "):
            title = l[1:].strip()
            if title and title != "":
                break
    if not title or title == "":
        raise Exception("no title")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = None
    with open(from_path) as f:
        markdown = f.read()
    template = None
    with open(template_path) as f:
        template = f.read()
    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Content }}", markdown_html, 1)
    template = template.replace("{{ Title }}", title, 1)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, 'w') as f:
        f.write(template)
