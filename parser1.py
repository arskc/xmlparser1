import xml.etree.ElementTree as ET

tree = ET.parse('x1.xml')
root = tree.getroot()

print("Vehicle Details:")
for vehicle in root.iter('vehicle'):
    year = vehicle.find('year').text
    make = vehicle.find('make').text
    model = vehicle.find('model').text
    print(f"Year: {year}\nBrand: {make}\nModel: {model}\n")

print("Customer Details:")
for customer in root.iter('customer'):
    name = customer.find('contact/name').text
    phone = customer.find('contact/phone').text
    print(f"Name:{name}\nPhone: {phone}\n")

print("Vendor Details:")
for vendor in root.iter('vendor'):
    address = vendor.find('contact/name').text
    print(f"Vendor Contact: {address}\n")
