import re
from htmlnode import *
from textnode import *
from extract_markdown import *
from inline_markdown import *
from block import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    div = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            new_block = block.replace("\n", " ")
            children = text_to_children(new_block)
            node = ParentNode("p", children)
            div.append(node)

        elif block_type == BlockType.HEADING:
            difference = len(block) - len(block.lstrip("#"))        
            new_block = block[difference + 1:]
            children = text_to_children(new_block)
            node = ParentNode(f"h{difference}", children)
            div.append(node)

        elif block_type == BlockType.CODE:       
            new_block = block[4:-3]
            new_html = text_node_to_html_node(TextNode(new_block, TextType.TEXT))
            node = ParentNode("pre", [ParentNode("code", [new_html])])
            div.append(node)

        elif block_type == BlockType.QUOTE:
            joint_text = []
            for line in block.split("\n"):       
                new_line = line[1:]
                joint_text.append(new_line.strip())
            final_text = " ".join(joint_text)
            children = text_to_children(final_text)
            node = ParentNode("blockquote", children)
            div.append(node)

        elif block_type == BlockType.UN_LIST:
            all_li_nodes = []
            for line in block.split("\n"):       
                new_line = line[2:]
                children = text_to_children(new_line)
                all_li_nodes.append(ParentNode("li", children))
            node = ParentNode("ul", all_li_nodes)
            div.append(node)

        elif block_type == BlockType.ORD_LIST:
            all_li_nodes = []
            for line in block.split("\n"):       
                new_line = line.split(". ", 1)[1]
                children = text_to_children(new_line)
                all_li_nodes.append(ParentNode("li", children))
            node = ParentNode("ol", all_li_nodes)
            div.append(node)

    return ParentNode("div", div)


def text_to_children(block):
    new_block = text_to_textnodes(block)
    new_nodes = []
    for node in new_block:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes
