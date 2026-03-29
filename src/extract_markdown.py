import re
from split_md_blocks import *
from block_types import *

def extract_markdown_images(text):
    extracted = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return extracted


def extract_markdown_links(text):
    extracted = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return extracted

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEAD:
            if re.match(r"^#\s+", block):
                return re.sub(r"^#\s+", '', block).strip()
    raise Exception("No header")