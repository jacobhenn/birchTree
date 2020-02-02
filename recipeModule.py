import json

def uniqueElementsIn(inputList):
    return(list(set(inputList)))

def itemLabel(jsonParsed):
    firstIngredient = list(jsonParsed['ingredients'][0].keys())[0]
    return(firstIngredient)
    

def ingredients(itemName):
    # Generate a file name based off of the item name
    fileName = 'C:/Users/windo/Desktop/Stuff/Projects/Minecraft/birchTree/recipes/' + itemName + '.json'

    # Read the file as json
    try:
        jsonRaw = open(fileName, 'r').read()
    except:
        jsonRaw = ''
        print('E1: Not a valid item name')
        return

    jsonParsed = json.loads(jsonRaw)

    # Find which of four variations the file is formatted in
    recipeType = jsonParsed['type'].replace('minecraft:crafting_', '')
    if recipeType == 'shapeless':
        keyVersion = itemLabel(jsonParsed)

    # If the format is one of the shapeless variety, form a material list
    if recipeType == 'shapeless':
        rawIngredients = []
        numberedIngredients = []

        for value in jsonParsed['ingredients']:
            rawIngredients.append(value[keyVersion])

        for value in uniqueElementsIn(rawIngredients):
            numberedIngredients.append([rawIngredients.count(value), value.replace('minecraft:', '')])

        return(numberedIngredients)

    # If the format is one of the shaped variety, form a material list
    elif recipeType == 'shaped':
        numberedIngredients = []
        pattern = list(''.join(jsonParsed['pattern']))

        # For all the keys in the pattern
        for value in uniqueElementsIn(pattern):
            numberedIngredients.append([pattern.count(value), value])

        return(numberedIngredients)

def formatRecipe(rawRecipe):
    formattedRecipe = []
    for item in rawRecipe:
        formattedRecipe.append(str(item[0]) + ' ' + item[1])

    return('\n'.join(formattedRecipe))
