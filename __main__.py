from lxml import etree
import sys
import argparse
import sf_price_fetcher

def convert_card(card):
    return f"{card.attrib['number']}x {card.attrib['name']}"

def print_list(mainboard, **kwargs):
    print('\n'.join(convert_card(card) for card in mainboard))

def print_pricing(mainboard, order='list'):
    total_price = 0
    data = []
    for card in mainboard:
        count = card.attrib['number']
        name = card.attrib['name']
        price = sf_price_fetcher.fetcher.get(name)
        if order == 'list': # if we're printing in list order, do so as prices are fetched
            print(f'{count}x {name} @${price}')
        else:
            data.append({'count': count, 'name': name, 'price': price})
        total_price += int(count) * float(price)

    if order != 'list':
        data = sorted(data, key=lambda i: i[order])
        datavals = (i.values() for i in data)
        print('\n'.join(f'{count}x {name} @${price}' for count, name, price in datavals))

    print(f'total price: ${round(total_price, ndigits=2)}')

argparser = argparse.ArgumentParser(description='Cockatrice COD file converter.')
argparser.add_argument('-p', '--prices', dest='action', action='store_const',
                       const=print_pricing, default=print_list,
                       help='Fetch and print pricing data as well as total deck price')
argparser.add_argument('-o', '--order', choices=['list', 'name', 'price'],
                       default='list')
argparser.add_argument('filename', type=str)
args = argparser.parse_args()

parser = etree.XMLParser()

with open(args.filename, 'r') as cod_file:
    tree = etree.parse(cod_file, parser)

mainboard = tree.xpath("//zone[@name = 'main']/card")

args.action(mainboard, order=args.order)
