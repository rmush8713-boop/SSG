import re

def extract_markdown_images(text):
    extracted = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return extracted


def extract_markdown_links(text):
    extracted = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted
