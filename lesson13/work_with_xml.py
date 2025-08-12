import xml.etree.ElementTree as ET


# Завантаження XML-файлу

tree = ET.parse('data.xml')
root = tree.getroot()

# # Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)
        if subchild.tag == "timingExbytes":
            print("__"*80)
            for exbytes_child in subchild:
                print(exbytes_child.tag, exbytes_child.text)

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        bbo = timing_exbytes.find('bbo')
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: Не знайдено")