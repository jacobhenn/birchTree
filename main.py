import json
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
    recipe = getRecipe(inputList[1])

    for item in recipe:
        item = item.split(' ')
        print(item)
        item[0] = int(item[0])
        print(item)
        item[0] = str(item[0] * inputList[2])
        print(item)
        ' '.join(item)
        print(item)

    exec(getLevel() + '.update({inputList[1] : ' + str(recipe) + '})')


# lr <branchName>:
#   print all the requirements in <branchName>
def lr():
    print(getLevel())
    testVar = 'test'
    exec('%s = %d' % (testVar, getLevel())) 
    print(testVar)

    for item in exec(getLevel()):
        print('\n'.join(item))


# run <command>
#   runs <command> as though it were python code
def run():
    exec(inputList[1])


# start the REPL
takeInput()
