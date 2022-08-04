#! usr/bin/env Python
# coding = utf-8

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

file_now = "/users/Arthur/learnPython/learnXML.xml"

tree = ET.ElementTree(file=file_now)
root = tree.getroot()

for ele in root.iter():
    if ele.attrib == {}:
        print ele.tag+":", ele.text
    if ele.attrib != {}:
        print ele.tag, ele.attrib, ele.text
print "\n"

for ele in root.iterfind("book/title"):
    print ele.text
print "\n"

for ele in root.findall("book"):
    title = ele.find('title').text
    author = ele.find('author').text
    year = ele.find('year').text
    price = ele.find('price').text
    print title,"|", author, "|", year, "|", price

#del root[1]
#tree.write("/users/Arthur/learnPython/learnXML.xml")

#for price in root.iter("price"):
#    new_price = float(price.text)+7
#    price.text = str(new_price)
#    price.set("update","up")

ET.SubElement(root, "book")
for ele in root:
    print ele.tag

ET.SubElement(root[len(root)-1], "title")
root[len(root)-1].find('title').text = "PyCharm"


#tree.write(file_now)

