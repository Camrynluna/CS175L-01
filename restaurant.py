#CS175L
#Camryn Moschitta

#restaurant

vegetarian=False
vegan=False
gluten_free=False

answer1=input('Is anyone in your party a vegetarian?: ')
if answer1 == 'yes' or answer1 == 'Yes':
    vegetarian = True

answer2=input('Is anyone in your party a vegan?: ')
if answer2 == 'yes' or answer2 == 'Yes':
    vegan = True

answer3=input('Is anyone in your party gluten free?: ')
if answer3 == 'yes' or answer3 == 'Yes':
    gluten_free = True

print("Here are your restauarant choices:")

if vegetarian== False and vegan== False and gluten_free== False:
    print("Joe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
if vegetarian== True and vegan== False and gluten_free== False:
    print("Mama's Fine Italian")
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
if vegetarian== True and vegan== False and gluten_free== True:
    print("Main Street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
if vegetarian== True and vegan== True and gluten_free== True:
    print("Corner Cafe")
    print("Chef's Kitchen")

