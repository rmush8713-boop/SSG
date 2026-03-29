from split_md_blocks import *
from block_types import *
from split_nodes import *
from htmlnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    result = []
    for block in blocks:
        b = block_to_block_type(block)
        match b:
            case BlockType.PG:
                result.append(pg_wrap(block))
            case BlockType.CODE:
                result.append(code_wrap(block))
            case BlockType.HEAD:
                result.append(header_wrap(block))
            case BlockType.QUOTE:
                result.append(quote_wrap(block))
            case BlockType.UNORD:
                result.append(unord_wrap(block))
            case BlockType.ORD:
                result.append(ord_wrap(block))
            case _:
                raise Exception("Dodelay code eblan")
    return ParentNode('div', result)

def code_wrap(block):
    c = block.split('\n')
    c = c[1:-1]
    c = "\n".join(c)
    return ParentNode('pre', [LeafNode("code", c)])

def pg_wrap(block):
    result = []
    nodes = text_to_textnodes(re.sub(r'\s+', ' ', block).strip())
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return ParentNode('p', result)

def header_wrap(block):
    h =  len(re.match(r"^(#{1,6})\s.+", block).group(1))
    p = f'h{h}'
    result = []
    nodes = text_to_textnodes(re.sub(r"(#{1,6})\s", '', block))
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return ParentNode(p, result)

def quote_wrap(block):
    result = []
    nodes = text_to_textnodes(re.sub(r"^>\s+", '', block, flags=re.MULTILINE))
    for node in nodes:
        result.append(text_node_to_html_node(node))
    return ParentNode('blockquote', result)

def unord_wrap(block):
    splited = (re.sub(r"^-\s+", '', block, flags=re.MULTILINE)).split('\n')
    r = []
    for s in splited:
        r.append(LeafNode("li", s))
    return ParentNode('ul', r)

def ord_wrap(block):
    splited = (re.sub(r"^\d.\s+", '', block, flags=re.MULTILINE)).split('\n')
    r = []
    for s in splited:
        r.append(LeafNode("li", s))
    return ParentNode('ol', r)
