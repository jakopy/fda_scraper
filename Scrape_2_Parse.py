import re
all_files = 22784
#error child  6629
all_drug_names = []
for i in range(6630,all_files,1):
    filename = "data/Page_" + str(i) + ".txt"
    with open(filename) as f:
       data = f.readlines()
    print data
    first_line = data[0]
    drugname = first_line.split("<?xml")[0]
##    print "DRUG NAME: " + drugname.replace("\n","")
##    drugname = drugname.replace("\n","")
    all_drug_names.append(drugname)
    index = 0
    data_clean = []
    for line in data:
        notag = re.sub("<.*?>","",line)
        notag = notag.replace("\n","")
        notag = notag.replace("               ","")
        notag = notag.replace("   ","")
        if "" != notag:
##            if "blood pressure" in notag:
##                print notag
            data_clean.append(notag)
    
    index = 0
    active_ingredients = ["Active Ingredient","Active Ingredients","active ingredients","Active ingredients","Active ingredient"]
    for line in data_clean:
        if line in active_ingredients:
            start_active = index
        if "Purpose" in line:
            start_purpose = index
            end_active = index
        if "Warnings" in line:
            start_warning = index
            end_purpose = index
        if "Uses" in line:
            start_uses = index
            end_warning = index
        if "Directions" in line:
            start_directions = index
            end_uses = index
        if "Inactive ingredients" in line:
            start_inactive = index
            end_directions = index
        if "Questions" in line:
            start_questions = index
            end_inactive = index
        index += 1
##    data_clean[start_active:end_active]
    purpose = data_clean[start_purpose:end_purpose]
    for i in purpose:
        if "high blood pressure" in i:
            print drugname
            print i
##    if "blood pressure" in purpose:
##        print drugname
##        print purpose
##    print "================================="
##for drug in all_drug_names:
filename = "all_drugs.txt"
with open(filename,"w") as f:
    for drug in all_drug_names:
        f.writelines(drug)


##Traceback (most recent call last):
##  File "C:\Users\Jacob Isaacs\Documents\PROJECTS WITH TED\FDA scrape proj\data\large_file\data_parser.py", line 6, in <module>
##    with open(filename) as f:
##IOError: [Errno 2] No such file or directory: 'data/Page_6629.txt'
##    parsed_data = {}
##    for line in data:
##        if "<title" in line:
##            f1 = line.replace("\n","")
##            f2 = f1.split(">")[1]
##            f3 = f2.split("</")[0]
##            section = f3
##            current_section = section
##            parsed_data[current_section] = []
##        #if current title has not yet been incremented, continue to capture paragraphs
##        if "<paragraph>" in line:
##            f1 = line.replace("\n","")
##            f2 = f1.split(">")[1]
##            f3 = f2.split("</")[0]
##            content = f3
##            parsed_data[current_section].append(content)
##        index += 1
##    for section in parsed_data:
##        print section
##        print parsed_data[section]
    


