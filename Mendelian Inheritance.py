# Integrate required module
import itertools

# Returns all possible combinations of the individual elements from a list; needs import itertools
def pos_combs_combs(cell):
    pos_combs = [''.join(map(str, comb)) for comb in itertools.combinations(cell, count_considered_characterstics)]
    pos_combs = [n for n in pos_combs if len(set(n.lower())) == len(n.lower())]
    return pos_combs

# Sorts List by abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def sort_list(cell):
    cell_sorted = []
    abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for let in abc:
        if let in cell:
            count_allele = cell.count(let)
            for i in range(count_allele):
                cell_sorted.append(let)
    return cell_sorted

# Sorts String by abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def sort_string(cell):
    cell = list(cell)
    cell_sorted = []
    final = ""
    abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for let in abc:
        if let in cell:
            count_allele = cell.count(let)
            for i in range(count_allele):
                cell_sorted.append(let)
    for n in cell_sorted:
        final = final + n
    return final

# Counts the frequency of elements in a list; Output = ["element1", "count1", "element2", ...]
def counter(list):
    output_list = []
    for dot in sorted(set(list), key=list.index):
        output_list.append(dot)
        output_list.append(list.count(dot))
    return output_list

# Counts the uppercase letters in a string (only used for sorting below)
def capital_count(sub):
    return len([ele for ele in sub if ele.isupper()])

# Enters the number of alleles considered
count_considered_characterstics = int(input("Number of characteristics considered: "))

# Enters alleles and allele letters in list
considered_characterstics = []
considered_alleles = []
characterstic_count = 1
allel_count = 1
for characterstic in range(count_considered_characterstics):
    considered_characterstics.append(input(f"Characteristic {characterstic_count}: "))
    for allel in range(2):
        considered_alleles.append(input(f"Allele {allel_count}: "))
        considered_alleles.append(input(f"Allele {allel_count} Letter: "))
        allel_count += 1
    allel_count = 1
    characterstic_count += 1

# Enter cells as letters
cell_1 = input("Cell 1: ")
cell_2 = input("Cell 2: ")

# Sorts cells with the function above by abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
cell_1_sorted = sort_list(cell_1)
cell_2_sorted = sort_list(cell_2)

# Returns all possible combinations of the individual elements from a list using the function above; needs import itertools
pos_combs_cell_1 = pos_combs_combs(cell_1_sorted)
pos_combs_cell_2 = pos_combs_combs(cell_2_sorted)

# Calculates the count of possible combinations
pos_combs_count = 2**count_considered_characterstics

# Merges the possibilities in rows; Shape = [["element1"], ["element2"], ...]
fuselist = []
for k in pos_combs_cell_2:
    for i in pos_combs_cell_1:
        fuselist.append([k+i])

# Brings the list into matplotlib form
finaldata = []
for m in range(len(fuselist))[::pos_combs_count]:
    save = []
    for n in range(pos_combs_count):
        save += fuselist[m+n] 
    finaldata.append(save)

# Use the function above to sort each element by abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
for p in range(len(finaldata)):
    finaldata[p] = [sort_string(f) for f in finaldata[p]]

# Makes the list look better; Example = ["element 1", "element 2", ...]
countlist = []
for p in finaldata:
    for o in p:
        countlist.append(o)
geno_numberlist = counter(countlist)

# Choose between dominant and recessive - Replaces both letters with upper case if dominant and lower case if recessive
phenolist = []
for element in countlist:
    splitted = [element[i:i + 2] for i in range(0, len(element), 2)]
    new_tile = ""
    for tile in splitted:
        upper = 0
        for letter in tile:
            if letter.isupper():
                upper += 1
        if upper != 0:
            new_tile += tile.replace(tile, list(tile)[0].upper())
        else:
            new_tile += tile.replace(tile, list(tile)[0].lower())
    phenolist.append(new_tile)

# Save phenotypes sorted in lists
pheno_numberlist = counter(phenolist) # List of phenotype + count | Example: ["ABC", "27", "AbC", "9", ...]
pheno_just = [] # List of phenotypes | Example: ["ABC", "AbC", ...]
pheno_number = [] # Number of phenotypes as a list | Example: ["27", "9", ...]
for u in pheno_numberlist[::2]:
    pheno_just.append(u)
for u in pheno_numberlist[1::2]:
    pheno_number.append(u)
pheno_just.sort(key=capital_count, reverse=True)
pheno_number.sort(reverse=True)

# Replace allele letters with alleles
improved = []
for i in pheno_just:
    saver = []
    for m in i:    
        m = m.replace(considered_alleles[considered_alleles.index(m)], considered_alleles[considered_alleles.index(m)-1])
        saver.append(m)
    saver = ", ".join(saver)
    improved.append(saver)

# import the modules for the table
import matplotlib.pyplot as plt
import os

# Create the table
def draw_table():
    the_table = plt.table(cellText=finaldata,
                        colWidths=[0.1] * pos_combs_count,
                        rowLabels=pos_combs_cell_2,
                        colLabels=pos_combs_cell_1,
                        loc='center')
    the_table.set_fontsize(pos_combs_count*5)
    the_table.scale(pos_combs_count, pos_combs_count)
    
# Remove coordinate system
def rem_kords():
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.savefig('matplotlib-table.png', bbox_inches='tight', pad_inches=0.05)

# call functions
draw_table()
rem_kords()

# Creation and design of the text file
user = os.getlogin()
file = open(f"C:/Users/{user}/Desktop/file.txt","w")

file.write(f"Characteristics considered ({count_considered_characterstics}): \n")
for i in range(len(considered_alleles))[::4]:
    file.write(f"{considered_characterstics[int(i/4)]}: {considered_alleles[i]} ({considered_alleles[i+1]}), {considered_alleles[i+2]} ({considered_alleles[i+3]})\n")
file.write("\n")
for h in cell_1_sorted:
    file.write(h)
file.write(" x ")
for r in cell_2_sorted:
    file.write(r)
file.write("\n")
file.write("Ratios: \n")
file.write("Genotyperatio: \n")
for j in range(len(geno_numberlist))[::2]:
    genotyperatio = geno_numberlist[j] + ": " + str(geno_numberlist[j+1]) + "/"+ str(pos_combs_count**2)
    file.write(f"{genotyperatio}\n")
file.write("\n")
file.write("Phenotyperatio: \n")
for c in range(len(improved)):
    phenotyperatio = improved[c] + ": " + str(pheno_number[c]) + "/" + str(pos_combs_count**2)
    file.write(f"{phenotyperatio}\n")

file.close()

# Save table to desktop instead of in user
os.replace(f"C:/Users/{user}/matplotlib-table.png", f"C:/Users/{user}/Desktop/matplotlib-table.png")

##########################################
# Made by Welf Baumann and Ole Ahrenhold #
##########################################