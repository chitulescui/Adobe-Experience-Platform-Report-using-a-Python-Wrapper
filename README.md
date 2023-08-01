# Adobe-Experience-Platform-Report-using-a-Python-Wrapper
Adobe Experience Platform offers us a better way to structure and store the information from a website in terms of tracking.
Instead of using Adobe Launch`s classic tracking methods, we can combine both of the features and map all the data into an XDM Schema
The XDM Schema will be captured in a JSON file, which will provide us all the necessary information in order to create our report.

In order to gain access to the whole data we first have to create a project in Adobe Developer Console, to ensure the connection using JWT authentification method and then create the configuration file for Adobe Experience Platform API via a Python Wrapper. The documentation about the Python Wrapper can be found here: **https://github.com/pitchmuc/aepp/blob/main/docs/getting-started.md**

* **First Step** : Create the configuration file to ensure the connectivity to **Adobe Experience Platform API**
* **Second Step** : Retrieve a JSON file containing whole data via **Python Wrapper** (schema_xdm_totul.json)
* **Third Step**: Parse the data and look for objects`s **path/title/type/description/schema name**
* **Forth Step** : Create an .xlsl document with the same structure as **result.xlsx**
