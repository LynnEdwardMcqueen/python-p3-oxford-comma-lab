def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return " and ".join(items)
    return construct_multi_word_oxford_expression(items)

def construct_multi_word_oxford_expression(items):
    return_string = ""
    for i in range(len(items)):
        if (i < len(items) - 1):
            return_string += items[i] + ", "
        else:
            return_string += "and " + items[i]
        
    return return_string


print(oxford_comma(["Uno"]))
print(oxford_comma(["Dick", "Jane"]))
print(oxford_comma(["You", "Me", "Baby"]))
print(oxford_comma(["George", "Ringo", "Paul", "John"]))