from textnode import *
from extract_markdown import *

def split_nodes_delimiter(node_list, delimiter, text_type):
    result = []
    for node in node_list:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        new_list = []
        h1 = node.text.split(delimiter)
        if len(h1) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range(len(h1)):
            if h1[i] == "":
                continue
            if i % 2 == 1:
                new_list.append(TextNode(h1[i], text_type))
            else:
                new_list.append(TextNode(h1[i], TextType.TEXT))
        result.extend(new_list)
    return result




def split_nodes_image(node_list):
    result = []
    for node in node_list:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        new_list = []
        splitters = []
        splitted = extract_markdown_images(node.text)
        for i in splitted:
            splitters.append(f"![{i[0]}]({i[1]})")
        if len(splitters) > 0:
            reee = '(' + '|'.join(map(re.escape, splitters)) + ')'
            split = re.split(reee, node.text)
            for s in split:
                if s in splitters:
                    u = extract_markdown_images(s)
                    new_list.append(TextNode(u[0][0], TextType.IMAGE, u[0][1]))
                else:
                    if s != "":
                        new_list.append(TextNode(s, TextType.TEXT))
        else:
            result.append(node)
        if len(new_list) > 0:
            result.extend(new_list)
    return result


def split_nodes_link(node_list):
    result = []
    for node in node_list:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        new_list = []
        splitters = []
        splitted = extract_markdown_links(node.text)
        for i in splitted:
            splitters.append(f"[{i[0]}]({i[1]})")
        if len(splitters) > 0:
            reee = '(' + '|'.join(map(re.escape, splitters)) + ')'
            split = re.split(reee, node.text)
            for s in split:
                if s in splitters:
                    u = extract_markdown_links(s)
                    new_list.append(TextNode(u[0][0], TextType.LINK, u[0][1]))
                else:
                    if s != "":
                        new_list.append(TextNode(s, TextType.TEXT))
        else:
            result.append(node)
        if len(new_list) > 0:
            result.extend(new_list)
    return result



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes