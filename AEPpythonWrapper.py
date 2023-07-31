import json
import pandas as pd
import csv

numberss = 0

with open('schema_xdm_totul.json', encoding="utf8") as f:
    data = json.load(f)
    keys = data.keys()
    values = data.values()
myList = []





dict_now = {}

count = 0
# cheia properties doar una la inceput
for cheie_1, valoare_1 in data.items():
    # accesam toate cheile din properties
    for cheie_2, valoare_2 in data[cheie_1].items():
        # retinem valoarea cheilor intr-o variabila
        string_nou = cheie_2
        for cheie_addProp, val_addProp in valoare_2.items():
            print(val_addProp)
            if cheie_addProp == "additionalProperties":
                for cheie_addProp_2, val_addProp_2 in val_addProp.items():
                    if cheie_addProp_2 == "items":
                        for cheie_addProp_3, val_addProp_3 in val_addProp_2.items():
                            if cheie_addProp_3 == "properties":
                                for cheie_addProp_4, val_addProp_4 in val_addProp_3.items():
                                    string_nou += "." + cheie_addProp_4
                                    for cheie_addProp_5, val_addProp_5 in val_addProp_4.items():
                                        if cheie_addProp_5 == "type":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["type"] = val_addProp_4[cheie_addProp_5]

                                            else:
                                                dict_now[string_nou]["type"] = val_addProp_4[cheie_addProp_5]
                                        if cheie_addProp_5 == "title":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["title"] = val_addProp_4[cheie_addProp_5]

                                            else:
                                                dict_now[string_nou]["title"] = val_addProp_4[cheie_addProp_5]
                                        if cheie_addProp_5 == "description":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["description"] = val_addProp_4[cheie_addProp_5]
                                            else:
                                                dict_now[string_nou]["description"] = val_addProp_4[cheie_addProp_5]
                                    if "title" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["title"] = " "
                                    if "description" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["description"] = " "
                                    if "type" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["type"] = " "

                                    string_nou = cheie_2


            elif cheie_addProp == "properties":
                for cheie_addProp_2, val_addProp_2 in val_addProp.items():
                    if cheie_addProp_2 == "FormTracking":
                        for cheie_addProp_3, val_addProp_3 in val_addProp_2.items():
                            if cheie_addProp_3 == "properties":
                                for cheie_addProp_4, val_addProp_4 in val_addProp_3.items():
                                    string_nou += "." + cheie_addProp_4
                                    for cheie_addProp_5, val_addProp_5 in val_addProp_4.items():
                                        if cheie_addProp_5 == "type":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["type"] = val_addProp_4[cheie_addProp_5]

                                            else:
                                                dict_now[string_nou]["type"] = val_addProp_4[cheie_addProp_5]
                                        if cheie_addProp_5 == "title":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["title"] = val_addProp_4[cheie_addProp_5]

                                            else:
                                                dict_now[string_nou]["title"] = val_addProp_4[cheie_addProp_5]
                                        if cheie_addProp_5 == "description":
                                            if string_nou not in dict_now.keys():
                                                dict_now[string_nou] = {}
                                                dict_now[string_nou]["description"] = val_addProp_4[cheie_addProp_5]
                                            else:
                                                dict_now[string_nou]["description"] = val_addProp_4[cheie_addProp_5]
                                    if "title" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["title"] = " "
                                    if "description" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["description"] = " "
                                    if "type" not in dict_now[string_nou].keys():
                                        dict_now[string_nou]["type"] = " "
                                    string_nou = cheie_2

                    else:
                        string_nou += "." + cheie_addProp_2
                        for cheie_addProp_3, val_addProp_3 in val_addProp_2.items():

                            if cheie_addProp_3 == "type":
                                if string_nou not in dict_now.keys():
                                    dict_now[string_nou] = {}
                                    dict_now[string_nou]["type"] = val_addProp_2[cheie_addProp_3]

                                else:
                                    dict_now[string_nou]["type"] = val_addProp_2[cheie_addProp_3]

                            if cheie_addProp_3 == "title":
                                if string_nou not in dict_now.keys():
                                    dict_now[string_nou] = {}
                                    dict_now[string_nou]["title"] = val_addProp_2[cheie_addProp_3]

                                else:
                                    dict_now[string_nou]["title"] = val_addProp_2[cheie_addProp_3]
                            if cheie_addProp_3 == "description":
                                if string_nou not in dict_now.keys():
                                    dict_now[string_nou] = {}
                                    dict_now[string_nou]["description"] = val_addProp_2[cheie_addProp_3]
                                else:
                                    dict_now[string_nou]["description"] = val_addProp_2[cheie_addProp_3]
                        if "title" not in dict_now[string_nou].keys():
                            dict_now[string_nou]["title"] = " "
                        if "description" not in dict_now[string_nou].keys():
                            dict_now[string_nou]["description"] = " "
                        if "type" not in dict_now[string_nou].keys():
                            dict_now[string_nou]["type"] = " "
                        string_nou = cheie_2

import openpyxl

file = open("doamne.csv", "w")
writer = csv.DictWriter(file, ["path", "title", "type", "description", "schema name"], delimiter=",")
writer.writeheader()
for element, valoare_element in dict_now.items():
    dictionar_nou = valoare_element
    dictionar_nou["path"] = element
    dictionar_nou["schema name"] = "Victor Test"
    writer.writerow(dictionar_nou)
file.close()
tmp_file = pd.read_csv("auxiliar_file.csv",encoding="cp1252")
resultFile = pd.ExcelWriter("FinalResult.xlsx")
tmp_file.to_excel(resultFile, index=True)
resultFile.close()
