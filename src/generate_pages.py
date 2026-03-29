from markdown_to_html import *
from extract_markdown import *
import os
import sys

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page {from_path} -> {dest_path}")
    with open(from_path, 'r') as f:
        md_content = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    html_string = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(html)


def recursive_generator(dir_path_content, template_path, dest_dir_path, basepath='/'):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for n in os.listdir(dir_path_content):
        from_ = os.path.join(dir_path_content, n)
        to_ = os.path.join(dest_dir_path, n)
        to_index = os.path.join(dest_dir_path, 'index.html')
        if os.path.isfile(from_):
            generate_page(from_, template_path, to_index, basepath)
        else:
            recursive_generator(from_, template_path, to_, basepath)