import json
import yaml
import recipeModule

tree = json.loads(open('C:/Users/windo/Desktop/Stuff/Projects/Minecraft/birchTree/tree.txt', 'r').read().replace('\'', '\"'))

inputList = []

# The function that sustains the REPL
def takeInput():
    global inputList

    inputList = input('[birchTree] ').split(' ')

    exec(inputList[0] + '()')

    takeInput()


# pr <itemName>:
#   print the ingredients used to craft <itemName>.
def pr():
    print(recipeModule.ingredients(inputList[1]))
    print(recipeModule.formatRecipe(recipeModule.ingredients(inputList[1])))


# x:
#   save the tree and exit the program
def x():
    open('C:/Users/windo/Desktop/Stuff/Projects/Minecraft/birchTree/tree.txt', 'w').write(str(tree))
    exit()


# xws:
#   exit the program without saving changes
def xws():
    exit()


# new <branchName>:
#   create a new branch on the project tree called <projectName>
def new():
    tree['birchTree'].update({inputList[1] : {}}) 


# rm <branchName>:
#   remove the branch named <branchName>
def rm():
    try:
        del(tree['birchTree'][inputList[1]])
    except:
        print('E2: Not a valid branch name')


# pt:
#   prints the current tree in raw form
def pt():
    print(tree)


# rq <itemNumber> <itemName> <branchName>:
#   specify that the project <branchName> requires <itemNumber> of <itemName>
def rq():
    # Initiate all of the arg names for easy reading
    args_itemNumber = inputList[1]
    args_itemName = inputList[2]
    args_branchName = inputList[3]

    # Fetch the ingredients of <itemName>
    ingredientList = recipeModule.ingredients(args_itemName)

    # Handle E1
    if ingredientList == 'E1':
        print('E1: Not a valid item name')
        takeInput()

    # Multiply the ingredients list by <itemNumber>
    ingredientList = [[item[0] * int(args_itemNumber), item[1]] for item in ingredientList]
    
    # Establish a variable '<itemNumber> <itemName>'
    number_name = ' '.join([args_itemNumber, args_itemName])

    # Add a key-val pair of <branchName> : ingredientList
    try:
        tree['birchTree'][args_branchName].update({number_name : ingredientList})
    except:
        print('E2: Not a valid branch name')
        takeInput()


# lr <branchName>:
#   print all the requirements in <branchName>
def lr():
    # Initiate the arg name for easy reading
    args_branchName = inputList[1]

    # requirementsList = 


# run <command>
#   runs <command> as though it were python code
def run():
    exec(inputList[1])


# start the REPL
takeInput()
