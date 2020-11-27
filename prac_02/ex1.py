
my_text = "Anya Josephine Marie Taylor Joy"

names = my_text.split()

for index, name in enumerate(names):
    print("Index {} contains {} with {} in length.".format(index, name, len(name)))