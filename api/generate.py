import csv
import pandas as pd
import json
from flask import Flask, jsonify, request, send_file
print(csv.__file__)


def get_product_images(color_map):
	product_main_images = {}
	image_index = 0
	for colorItem in color_map:
		if color_map[colorItem]:
			product_main_images[image_index] = color_map[colorItem]
			image_index = image_index+1

	return product_main_images


def get_product_image_pos(color_map):
	product_main_images_index = {}
	image_index = 0
	for colorItem in color_map:
		if color_map[colorItem]:
			product_main_images_index[image_index] = image_index+1
			image_index = image_index + 1

	return ''


def get_csv(request):
	print('generating...')
	for item in request:
		PRODUCT_NAME = item["product_name"]
		NORMALIZED_TITLE = PRODUCT_NAME.replace('_', ' ').title().split("Half", 1)
		TITLE = "| Half".join(NORMALIZED_TITLE)
		COLORS = item["colorsImageMap"]

		# TAGS = "abstract, men, premium, printed, short sleeve, S, M, L, XL, XXL, 3XL"
		TAGS = item["tags"]

		SIZE = item["size"]
		SALE_PRICE = item["sale_price"]
		MRP = item["mrp"]
		ITEM_COST = item["item_cost"]
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
				if COLORS[colorValue]:
					option_size_values[colorIndex] = sizeValue
					option_color_values[colorIndex] = colorValue
					variant_images[colorIndex] = COLORS[colorValue]
					colorIndex = colorIndex + 1
					product_images = get_product_images(COLORS)
					product_image_pos = get_product_image_pos(COLORS)

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

	path = "output/feed.csv"
	# return path
	return send_file(path, as_attachment=True)






