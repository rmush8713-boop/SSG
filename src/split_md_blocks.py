
def markdown_to_blocks(markdown):
    result = []
    text = markdown.strip().split("\n\n")
    for i in text:
        if i != '':
            result.append(i.strip())
        
    return result


