def merge_lists_to_dict(list1, list2):
    combined_data = zip(list1, list2)
    result_dict = dict(combined_data)
    return result_dict


products = ["Book", "Pen", "Notebook", "Pencil"]
prices = [150, 30, 80, 20]


product_dictionary_keyword = merge_lists_to_dict(list1=products, list2=prices)
print(f"Dictionary using keyword arguments: {product_dictionary_keyword}")


product_dictionary_mixed = merge_lists_to_dict(products, list2=prices)
print(f"Dictionary using mixed arguments: {product_dictionary_mixed}")