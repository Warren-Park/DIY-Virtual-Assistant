if __name__=="__main__":
    """Run this when a new country-capital pair is given
    You can modify this program to automate the question-response pair production process.
    """
    file = open("country-list.csv")
    text = file.read().split("\n")
    file.close()

    result = ""
    for i in text[1:-1]:
        cache = i.replace('"',"").split(",")
        cache2 = "The capital city of "+cache[0]+"\t"+"The capital city of "+cache[0]+" is "+cache[1]+".\n"
        result+=cache2
    with open("country-list.tsv","w+") as file:
        file.write(result)
