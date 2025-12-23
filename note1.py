from bs4 import BeautifulSoup
import os

path=r"C:\Users\emb-rishguj\Downloads\Polysapce_CP_P3027-HVLSF_DeveloperReview.html"
if os.path.exists(path):
    with open(path, "r") as f:
        html_content = f.read()
    # nrml string type of text--> convert to tree 
    Tree = BeautifulSoup(html_content, "lxml")
    label_p = None
    target_table = None
    # my p tag contains table 1.3...... 
    #searching for all p tags
    for ptag in Tree.find_all("p"):
        
        text = ptag.get_text(strip=True)
        if "Table" and "1.3" and "Run-Time Checks Summary" in text: 
            # if the combined text has "Table1.3.Run-Time Checks Summary" 
            label_p = ptag 
            # marking that we found tag p with the table
            break

    #table next to the p tag that is found
    if label_p:
        target_table = label_p.find_next("table")#checks its sibling


    dict_table=dict()
    if target_table:
        #if table is not empty, copy all the keys and values into dict_table
        whole_table=target_table.find_all("tr")
        for tr in whole_table[1:]:
            text=tr.find_all("td")
            try: 
                value=int(text[1].get_text())
                dict_table[text[0].get_text(strip=True)]=value
            except ValueError:
                if not text[1].get_text():
                    dict_table[text[0].get_text(strip=True)]='Not specified'
                else:
                    dict_table[text[0].get_text(strip=True)]=text[1].get_text(strip=True)
        print(dict_table)
        
    else:
        print("Table Not found.")
else:
    print("File not found")
