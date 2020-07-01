"""
file: html_builder.py
language: python3
author: Annie Tiet
description: build a web page
date: 11/2019
"""

import sys
import turtle
from html_helper import *

valid_colors = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
                'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
                'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat',
                'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite',
                'royalblue', 'yellow', 'indigo ', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray',
                'mediumblue', 'red', 'khaki', 'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise',
                'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise',
                'coral', 'forestgreen', 'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum',
                'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon',
                'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray',
                'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown',
                'blanchedalmond', 'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod',
                'palevioletred', 'fuchsia', 'teal', 'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine',
                'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood', 'rosybrown', 'springgreen', 'purple',
                'olivedrab', 'lightslategrey', 'orange', 'aliceblue', 'mediumaquamarine', 'navy', 'salmon',
                'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple', 'skyblue',
                'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown',
                'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow',
                'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white',
                'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}

valid_hexes = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D',
               'd', 'E', 'e', 'F', 'f'}


@dataclass
class Variables:
    """
    class Variables represents the variables to be replaced in the style.
    field description:
    back_color: color of website's background
    head_color: color of heading
    font_style: font family for the text
    font_color: color of the font
    """
    back_color: str
    head_color: str
    font_style: str
    font_color: str


@dataclass
class Website:
    """
    class Website represents all components used to build the website
    field description:
    title: title of the website
    style: string of style tag
    content: List of Paragraph Objects
    """
    title: str
    style: str
    content: list


def valid_hex(s):
    """
    Determines whether s is a valid hex color. '#XXXXXX'
    :param s: string
    :return: Boolean True or False.
    """
    if len(s) != 7 or s[0] != "#":
        return False
    for i in range(1, 7):
        if s[i] not in valid_hexes:
            return False
    return True


def turtle_adjust():
    """
    Function to move position of turtle downwards 30px from its original location
    :return: None
    """
    turtle.pu()
    turtle.right(90)
    turtle.fd(30)
    turtle.left(90)
    turtle.pd()


def font_drawn():
    """
    With turtle, draws all font style choices for the style.
    :return: None
    """
    turtle.speed(0)
    turtle.setup(450, 400)
    turtle.pu()
    turtle.setpos(-100, 80)
    turtle.write("Arial", move=False, align="left", font=("Arial", 14, "normal"))
    turtle_adjust()
    turtle.write("Comic Sans MS", move=False, align="left", font=("Comic Sans MS", 14, "normal"))
    turtle_adjust()
    turtle.write("Lucida Grande", move=False, align="left", font=("Lucida Grande", 14, "normal"))
    turtle_adjust()
    turtle.write("Tahoma", move=False, align="left", font=("Tahoma", 14, "normal"))
    turtle_adjust()
    turtle.write("Verdana", move=False, align="left", font=("Verdana", 14, "normal"))
    turtle_adjust()
    turtle.write("Helvetica", move=False, align="left", font=("Helvetica", 14, "normal"))
    turtle_adjust()
    turtle.write("Times New Roman", move=False, align="left", font=("Times New Roman", 14, "normal"))
    turtle.hideturtle()
    turtle.done()


def color_loop():
    """
    While loop which prompts for color until valid response is provided.
    :param s: color string
    :return: Inputted color that is valid.
    """
    while True:
        s = input("Choose the name of a color, or in format '#XXXXXX': ")
        if valid_hex(s) or s.lower() in valid_colors:
            return s
        else:
            print("Invalid response. Please enter valid name / hex number.")
            continue


def prompt_style():
    """
    Prompts the user for the font and colors.
    :return: Variables Object
    """
    print("Background Color")
    bg_color = color_loop()
    font_answer = input("You will now choose a font.\nDo you want to see what the fonts look like? [yes] ")
    if font_answer == "yes" or font_answer == "":
        print("Close the window when you have made your choice.")
        font_drawn()
    print("Choose a font by its number.\n0: Arial, size 14\n1: Comic Sans MS, size 14\n2: Lucida Grande, size 14\n"
          "3: Tahoma, size 14\n4: Verdana, size 14\n5: Helvetica, size 14\n6: Times New Roman, size 16")
    while True:
        font_number = int(input(""))
        if font_number < 0 or font_number > 6:
            print("Invalid choice. Please choose a font represented by the numbers 0-6.")
            continue
        else:
            break
    if font_number == 0:
        font_style = "Arial"
    elif font_number == 1:
        font_style = "Comic Sans MS"
    elif font_number == 2:
        font_style = "Lucida Grande"
    elif font_number == 3:
        font_style = "Tahoma"
    elif font_number == 4:
        font_style = "Verdana"
    elif font_number == 5:
        font_style = "Helvetica"
    else:
        font_style = "Times New Roman"
    print("Paragraph Text Color")
    font_color = color_loop()
    print("Heading Color")
    head_color = color_loop()
    return Variables(bg_color, head_color, font_style, font_color)


def style_in(variables):
    """
    Opens style_template.txt and replaces @
    :param variables: Variables object
    :return: String of style tag
    """
    file = open("style_template.txt", "r")
    f = file.read()
    file.close()
    f = f.replace("@BACKCOLOR", variables.back_color)
    f = f.replace("@HEADCOLOR", variables.head_color)
    f = f.replace("@FONTSTYLE", variables.font_style)
    f = f.replace("@FONTCOLOR", variables.font_color)
    return f


def content_conversion(file):
    """
    Function that takes a file and creates dictionary entries for each paragraph using its title as the key.
    :param file: filename
    :return: Content component of website object
    """
    f = open(file).read().strip()
    s = ""
    for line in f:
        s += line  # making one big string
    lst = s.split("\n!new_paragraph\n")  # split into list of paragraphs
    dct = {}
    paragraphs = []
    keys = []
    dict_pic = {}
    for p in lst:  # paragraph in list of paragraphs
        paragraphs.append(p.split("\n"))
    # paragraphs is a list of lines
    for paragraph in range(1, len(paragraphs)):
        pics = []
        for line in paragraphs[paragraph]:
            temp = find_images(line)
            if temp is not None:
                pics.append(temp)
        dict_pic[paragraph] = pics
    for i in range(1, len(paragraphs)):
        dct[paragraphs[i][0][7:]] = paragraphs[i][1:]
        keys.append(paragraphs[i][0][7:])
    for element in dct:
        dct[element] = mend_lines(dct[element])
    content = []
    for para_title in keys:
        body = dct[para_title]
        content.append(Paragraph(para_title, body, dict_pic[keys.index(para_title)+1]))
        # key to dict_pic is the paragraph number. find by finding index of title in keys list ( + 1 because starts
        # counting at zero ).
        print(Paragraph(para_title, body, dict_pic[keys.index(para_title)+1]))
    return content



def website_title(file):
    """
    Splits the file by paragraphs. Since first line is always the title of the web page, returns first item in the list.
    :param file: file
    :return: string. Title
    """
    f = open(file).read().strip()
    s = ""
    for line in f:
        s += line  # one big string
    lst = s.split("\n!new_paragraph\n")
    f.close()
    return lst[0]


def find_images(lst):
    """
    Splits line into set of words and creates an Image object if the first word is '!image'.
    :param lst: line
    :return: Image object or None
    """
    split = lst.split()
    if len(split) == 0:     # empty line
        pass
    elif split[0] == "!image":
        if len(split) is 3:
            name = split[1]
            width = split[2]
            return Image(name, width)
        else:
            name = split[1]
            return Image(name, None)


def mend_lines(lst):
    """
    Combines the list of lines into one large string that will become the content of a paragraph. Does not concatenate
    lines with beginning with '!'
    :param lst: list of lines
    :return: string of paragraph content
    """
    s = ""
    for line in lst:
        if line is "" or line[0] == '!':
            pass
        else:
            s += line + " "
    return s


def ignoring_image(lst):  # line
    """
    Builds Image object
    :param lst: string that begins with !image
    :return: Image
    """
    if len(lst) is 3:
        name = lst[1]
        width = lst[2]
        return Image(name, width)
    else:
        name = lst[1]
        return Image(name, None)


def website_creation(title, content):
    """
    Creates html file titled index when program runs in wizard mode.
    :param title: string that will be the name of the html file
    :param content: string that will become the content of the html file
    :return: title.html
    """
    index = open(title + '.html', 'w')
    index.write(content)
    index.close()
    print("Your file has been saved as " + title + ".html")
    return index


def main():
    if len(sys.argv) > 1:  # website mode
        style = style_in(prompt_style())
        for i in range(1, len(sys.argv)):  # make website for every parameter
            components = Website(website_title(sys.argv[i]), style, content_conversion(sys.argv[i]))
            # html_skeleton is the string that will become the content of the html file.
            html_skeleton = "<!DOCTYPE HTML><html><head><title>" + components.title + "</title>" + components.style + \
                            "</head><body><h1>" + components.title + '</h1><hr /><p align = "center" >'
            for j in range(1, len(sys.argv)):   # making links to connect pages if multiple files have been entered.
                name = sys.argv[j][:len(sys.argv[i]) - 4]   # removes the '.txt' part to get the name
                html_skeleton += '<a href="' + name + '.html">' + name + '</a> --'
            html_skeleton += "</p>"     # closing link paragraph
            for paragraph in content_conversion(sys.argv[i]):   # making tags for all paragraphs
                html_skeleton += paragraph_tagging(paragraph)
            html_skeleton += "</body></html>"
            website_creation(sys.argv[i][:len(sys.argv[i]) - 4], html_skeleton)  # creates html file
    else:  # wizard mode
        title = str(input("What is the title of your website? "))
        style = style_in(prompt_style())
        paragraphs_bank = [make_paragraph()]  # all paragraph objects here
        while True:  # loop to add multiple paragraphs to list if desired
            more_paragraphs = input("Do you want to add another paragraph to your website? [yes] ")
            if more_paragraphs == "yes" or more_paragraphs == "":
                paragraphs_bank.append(make_paragraph())
            else:
                break
        components = Website(title, style, paragraphs_bank)
        html_skeleton = "<!DOCTYPE HTML><html><head><title>" + components.title + "</title>" + components.style + \
                        "</head><body><h1>" + components.title + "</h1><hr />"
        for paragraph in paragraphs_bank:
            html_skeleton += paragraph_tagging(paragraph)
        html_skeleton += "</body></html>"
        website_creation("index", html_skeleton)


if __name__ == "__main__":
    main()