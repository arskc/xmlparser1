import xml.etree.ElementTree as ET

#-------------------------------------------------------Load Document-------------------------------------------------------

tree = ET.parse('lead1.xml')
root = tree.getroot()


#-----------------------------------------------------Parse Information-----------------------------------------------------

prospect_status = []
prospect = root.find('.//prospect')
status = prospect.get('status') if prospect is not None else None
prospect_status.append({'status': status})

id_list = []
id = root.find('.//id')
if id is not None:
    sequence = id.get('sequence')
    source = id.get('source')
    i = id.text
    id_list.append({'sequence': sequence, 'source': source, 'id': i})
else:
    id_list.append({'sequence': None, 'source': None})

request_date_list = []
req_date = root.find('.//requestdate')
if req_date is not None:
    reqd = req_date.text
    request_date_list.append({'request_date': reqd})
else:
    request_date_list.append({'request_date': None})

vehicle_list = []
vehicle = root.find('.//vehicle')
if vehicle is not None:
    year = vehicle.find('year').text
    make = vehicle.find('make').text
    model = vehicle.find('model').text
    vehicle_list.append({'year': year, 'make': make, 'model': model})
else:
    vehicle_list.append({'year': None, 'make': None, 'model': None})

customer_list = []
customer = root.find('.//customer')
if customer is not None:
    fname_element = customer.find('contact/name[@part="first"]')
    fname = fname_element.text if fname_element is not None else None
    mname_element = customer.find('contact/name[@part="middle"]')
    mname = mname_element.text if mname_element is not None else None
    lname_element = customer.find('contact/name[@part="last"]')
    lname = lname_element.text if lname_element is not None else None
    email_element = customer.find('contact/email')
    email = email_element.text if email_element is not None else None
    phone_element = customer.find('contact/phone[@type="phone"]')
    phone = phone_element.text if phone_element is not None else None
    customer_list.append({'firstname': fname, 'middlename': mname, 'lastname': lname, 'email': email, 'phone': phone})
else:
    customer_list.append({'firstname': None, 'middlename': None, 'lastname': None, 'email': None, 'phone': None})

vendor_list = []
vendor = root.find('.//vendor')
if vendor is not None:
    vendor_name = vendor.find('vendorname')
    name = vendor_name.text if vendor_name is not None else None
    vendor_contact_name = vendor.find('contact/name')
    contact = vendor_contact_name.text if vendor_contact_name is not None else None
    vendor_contact_email = vendor.find('contact/email')
    email = vendor_contact_email.text if vendor_contact_email is not None else None
    vendor_list.append({'vendor_name': name, 'contact_name': contact, 'contact_email': email})
else:
    vendor_list.append({'vendor_name': None, 'contact_name': None, 'contact_email': None})


#-------------------------------------------------------Display-------------------------------------------------------

#Display
print("Prospect Status:")
for status in prospect_status:
    print(status)

print("\nID List:")
for id in id_list:
    print(id)

print("\nRequest Date List:")
for reqd in request_date_list:
    print(reqd)

print("\nVehicle List:")
for vehicle in vehicle_list:
    print(vehicle)

print("\nCustomer List:")
for customer in customer_list:
    print(customer)

print("\nVendor List:")
for vendor in vendor_list:
    print(vendor)
