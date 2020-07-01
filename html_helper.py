"""
file: html_helper.py
language: python3
author: Annie Tiet
description: helper file for html_builder. Deals with Paragraph objects.
date: 11/2019
"""

from dataclasses import dataclass
from typing import Union

valid_img = {"images/Dubai_Miracle_Garden.jpg", "images/flowers.jpg", "images/garden1.jpg",
             "images/Garden_of_Versailles.jpg", "images/happy-kid.png", "images/logo.jpg", "images/Maze_Dobrzyca.jpg",
             "images/WOW.jpg"}


@dataclass
class Paragraph:
    """
    class Paragraph represents a paragraph for the website.
    field description:
    title: title of paragraph
    content: content of paragraph
    image: image(s) to be added to paragraph if desired.
    """
    title: str
    content: str
    image: list


@dataclass
class Image:
    """
    class Image represents an image
    field description:
    name: image name
    width: percentage
    """
    name: str
    width: Union[int, None]


def make_paragraph(image_width=100):
    """
    Function that prompts paragraph components in wizard mode.
    :return: Paragraph object
    """
    title = input("Title of your paragraph: ")
    content = input("Content of your paragraph (single line) ")
    image = []
    images_choice = input("Do you want to add images? [yes] ")
    if images_choice == "yes" or images_choice == "":
        while True:
            img = input("Image file name: ")
            if img not in valid_img:
                print("Please enter a valid image file from the images subdirectory.")
                continue
            else:
                image.append(Image(img, image_width))
                break
        while True:
            choice_two = input("Do you want to add another image? [yes] ")
            if choice_two == "yes" or choice_two == "":
                while True:
                    another = input("Image file name: ")
                    if another not in valid_img:
                        print("Please enter a valid image file from the images subdirectory.")
                        continue
                    else:
                        image.append(Image(another, image_width))
                        break
            else:
                break
    return Paragraph(title, content, image)


def paragraph_tagging(paragraph):
    """
    Takes Paragraph object and puts information between html tags
    :param paragraph: Paragraph object
    :return: string of html
    """
    html = "<h2>" + paragraph.title + "</h2><p>" + paragraph.content + "</p>"
    for img in paragraph.image:
        html += '<img src="' + img.name + '" width="' + str(img.width) + '%"class="center">'
    return html

