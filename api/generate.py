import csv
import pandas as pd
import json
from flask import Flask, jsonify, request, send_file
print(csv.__file__)


def get_csv(request):
	print('generating...')
	print(request)
	for item in request:
		PRODUCT_NAME = 'GRADIENT_HALF_SLEAVE_COTTON_TSHIRT'
		NORMALIZED_TITLE = PRODUCT_NAME.replace('_', ' ').title().split("Half", 1)
		TITLE = "| Half".join(NORMALIZED_TITLE)
		#TITLE = 'SYLLABARY | Half Sleeve Cotton TShirt'
		COLORS = {
			'BLACK': 'https://cdn.shopify.com/s/files/1/0360/3693/5813/files/GRADIENT_HALF_SLEAVE_COTTON_TSHIRT_BLACK.jpg?v=1586252792',
			'RED': 'https://cdn.shopify.com/s/files/1/0360/3693/5813/files/GRADIENT_HALF_SLEAVE_COTTON_TSHIRT_RED.jpg?v=1586252791',
			'WHITE': 'https://cdn.shopify.com/s/files/1/0360/3693/5813/files/GRADIENT_HALF_SLEAVE_COTTON_TSHIRT_WHITE.jpg?v=1586252791',
			'ROYAL BLUE': 'https://cdn.shopify.com/s/files/1/0360/3693/5813/files/GRADIENT_HALF_SLEAVE_COTTON_TSHIRT_ROYAL_BLUE.jpg?v=1586252791'
		}

		TAGS = "abstract, men, premium, printed, short sleeve, S, M, L, XL, XXL, 3XL"


		SIZE = ['S', 'M', 'L', 'XL', 'XXL', '3XL']
		SALE_PRICE = "599"
		MRP = "699"
		ITEM_COST = "480"
		HANDLE = PRODUCT_NAME.replace('_', '-').lower()

		option_size_values = {}
		option_color_values = {}
		variant_images = {}
		product_images = {}
		product_image_pos = {}
		sizeIndex = 0
		colorIndex = 0
		for sizeValue in SIZE:
		    for colorValue in COLORS:
		    	option_size_values[colorIndex] = sizeValue
		    	option_color_values[colorIndex] = colorValue
		    	variant_images[colorIndex] = COLORS[colorValue]
		    	if len(product_images) != len(COLORS):
		    		product_images[colorIndex] = COLORS[colorValue]
		    		product_image_pos[colorIndex] = colorIndex+1

		    	colorIndex = colorIndex+1

		main_product_json = {
			"handle": HANDLE,
			"title": {"0": TITLE},
			"Body (HTML)": '',
			"Vendor": {"0":"echell"},
			"Type": {"0":"TShirt"},
			"Tags": {"0":TAGS},
			"Published": {"0":"TRUE"},
			"Option1 Name": {"0":"Size"},
			"Option1 Value": option_size_values,
			"Option2 Name": {"0":"Color"},
			"Option2 Value": option_color_values,
			"Option3 Name": "",
			"Option3 Value": "",
			"Variant SKU": "",
			"Variant Grams": "100",
			"Variant Inventory Tracker": "shopify",
			"Variant Inventory Policy": "continue",
			"Variant Fulfillment Service": "manual",
			"Variant Price": SALE_PRICE,
			"Variant Compare At Price": MRP,
			"Variant Requires Shipping": "TRUE",
			"Variant Taxable": "TRUE",
			"Variant Barcode": "",
			"Image Src": product_images,
			"Image Position": product_image_pos,
			"Image Alt Text": "",
			"Gift Card": {"0":"FALSE"},
			"SEO Title": "",
			"SEO Description": "",
			"Google Shopping / Google Product Category": "",
			"Google Shopping / Gender": "",
			"Google Shopping / Age Group": "",
			"Google Shopping / MPN": "",
			"Google Shopping / AdWords Grouping": "",
			"Google Shopping / AdWords Labels": "",
			"Google Shopping / Condition": "",
			"Google Shopping / Custom Product": "",
			"Google Shopping / Custom Label 0": "",
			"Google Shopping / Custom Label 1": "",
			"Google Shopping / Custom Label 2": "",
			"Google Shopping / Custom Label 3": "",
			"Google Shopping / Custom Label 4": "",
			"Variant Image": variant_images,
			"Variant Weight Unit": "g",
			"Variant Tax Code": "",
			"Cost per item": ITEM_COST
		}

		df = pd.read_json(json.dumps(main_product_json))
		df.to_csv('output/1.csv', mode='a', header=False, index=False, line_terminator="\n")

	path = "output/1.csv"
	return send_file(path, as_attachment=True)






