def merge_lists_to_dict(list1, list2):
    combined_data = zip(list1, list2)
    result_dict = dict(combined_data)
    return result_dict

products = ["eggs", "apple", "Coke", "Milk"]
prices = [150, 30, 80, 20]

product_dictionary_kword = merge_lists_to_dict(list1=products, list2=prices)
print(f"Dictionary using keyword arguments: {product_dictionary_kword}")

product_dictionary_full = merge_lists_to_dict(products, list2=prices)
print(f"Dictionary using mixed arguments: {product_dictionary_full}")