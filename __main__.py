from lxml import etree
import sys

parser = etree.XMLParser()
filename = sys.argv[1]
with open(filename, 'r') as cod_file:
    tree = etree.parse(cod_file, parser)

mainboard = tree.xpath("//zone[@name = 'main']/card")

def convert_card(card):
    return f"{card.attrib['number']}x {card.attrib['name']}"

print('\n'.join(convert_card(card) for card in mainboard))
