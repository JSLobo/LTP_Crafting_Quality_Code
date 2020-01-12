"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """
    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cousine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done! Return that sorted list.
    return result


import doctest
doctest.testmod()


def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of {str, int}

    Return a list of  [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
        'Queen St. Cafe': 82,
        'Dumplings R Us': 71,
        'Mexican Grill': 85,
        'Deep Fried Everything': 52}
    >>> names = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]

    """


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georgie Porgie'],
                'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                'Malaysian': ['Queen St. Cafe'],
                'Thai': ['Queen St. Cafe'],
                'Chinese': ['Dumplings R Us'],
                'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """


def read_restaurants(filename):
    """ (file) -> (dict, dict, dict)
    Return a tuple of three dictionaries based on the information in the file:
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    file = open(filename, "r")

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {'Canadian': [], 'Pub Food': [], 'Malaysian': [], 'Thai': [], 'Chinese': [], 'Mexican': []}

    count = 1
    for line in file:
        if count % 5 == 1 and line is not "":
            restaurant_name = line.rstrip("\n")
            # print(restaurant_name)
            count = count + 1

        elif count % 5 == 2 and line is not "":
            rating = int((line.rstrip("\n")).rstrip("%"))
            name_to_rating[restaurant_name] = rating
            count = count + 1

        elif count % 5 == 3 and line is not "":
            price = line.rstrip("\n")
            (price_to_names.get(price)).append(restaurant_name)
            count = count + 1

        elif count % 5 == 4 and line is not "":
            cuisines = line.rstrip("\n")
            cuisines_list = get_cuisines_separated(cuisines)
            # print(get_cuisines_separated(cuisines))
            for cuisine in cuisines_list:
                (cuisine_to_names.get(cuisine)).append(restaurant_name)
            count = count + 1

        elif count % 5 == 0 or line is "":
            count = 1

    file.close()
    return name_to_rating, price_to_names, cuisine_to_names


def get_cuisines_separated(cuisines):
    cuisines_list = []
    cuisine = ''
    for ch in cuisines:
        if ch != ',':
            cuisine = cuisine + ch
        elif ch == ',':
            cuisines_list.append(cuisine)
            cuisine = ''

    cuisines_list.append(cuisine)
    return cuisines_list
