from lxml import etree
import sys
import argparse
import sf_price_fetcher

def convert_card(card):
    return f"{card.attrib['number']}x {card.attrib['name']}"

def print_list(mainboard):
    print('\n'.join(convert_card(card) for card in mainboard))

def print_pricing(mainboard):
    total_price = 0
    for card in mainboard:
        count = card.attrib['number']
        name = card.attrib['name']
        price = sf_price_fetcher.fetcher.get(name)
        print(f'{count}x {name} @${price}')
        total_price += int(count) * float(price)
    print(f'total price: ${round(total_price, ndigits=2)}')

argparser = argparse.ArgumentParser(description='Cockatrice COD file converter.')
argparser.add_argument('-p', '--prices', dest='action', action='store_const',
                       const=print_pricing, default=print_list,
                       help='Fetch and print pricing data as well as total deck price')
argparser.add_argument('filename', type=str)
args = argparser.parse_args()

parser = etree.XMLParser()

with open(args.filename, 'r') as cod_file:
    tree = etree.parse(cod_file, parser)

mainboard = tree.xpath("//zone[@name = 'main']/card")

args.action(mainboard)
