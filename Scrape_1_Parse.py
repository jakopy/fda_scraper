import json

all_titles = {}
pages_missed = []
for i in range(0,905,1):
    num=i
    try:
        filename = "data_scrape_1/page_" + str(num) +".txt"
        with open(filename,"r") as f:
            data = f.read()
            information = json.loads(data)
            for i in information["data"]:
                setid = i["setid"]
                title = i["title"]
                if title not in all_titles:
                    all_titles[title]=setid
    except Exception as e:
        pages_missed.append(i)
    
for i in pages_missed:
    print "page" +str(i) + " was missed"


filename = "drugs_set_ids.txt"
count = 0
with open(filename,'w') as f:
    for title in all_titles:
        setid = all_titles[title]
        f.write(setid.encode('utf-8') + '\n')

f.close()
