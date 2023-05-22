import xml.etree.ElementTree as ET

class ParseXML():
    #-------------------------------------------------------Load Document-------------------------------------------------------
    def __init__(self):
        self.prospect_status = []
        self.id_list = []
        self.request_date_list = []
        self.vehicle_list = []
        self.customer_list = []
        self.vendor_list = []
        self.provider_list = []

    #-----------------------------------------------------Parse Information-----------------------------------------------------
    def parse(self, lead):
        self.tree = ET.parse(lead)
        self.root = self.tree.getroot()
        prospect = self.root.find('.//prospect')
        status = prospect.get('status') if prospect is not None else None
        self.prospect_status.append({'status': status})

        id = self.root.find('.//id')
        if id is not None:
            sequence = id.get('sequence')
            source = id.get('source')
            i = id.text
            self.id_list.append({'sequence': sequence, 'source': source, 'id': i})
        else:
            self.id_list.append({'sequence': None, 'source': None})

        req_date = self.root.find('.//requestdate')
        if req_date is not None:
            reqd = req_date.text
            self.request_date_list.append({'request_date': reqd})
        else:
            self.request_date_list.append({'request_date': None})

        vehicle = self.root.find('.//vehicle')
        if vehicle is not None:
            year = vehicle.find('year').text
            make = vehicle.find('make').text
            model = vehicle.find('model').text
            self.vehicle_list.append({'year': year, 'make': make, 'model': model})
        else:
            self.vehicle_list.append({'year': None, 'make': None, 'model': None})

        customer = self.root.find('.//customer')
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
            self.customer_list.append({'firstname': fname, 'middlename': mname, 'lastname': lname, 'email': email, 'phone': phone})
        else:
            self.customer_list.append({'firstname': None, 'middlename': None, 'lastname': None, 'email': None, 'phone': None})

        vendor = self.root.find('.//vendor')
        if vendor is not None:
            vendor_name = vendor.find('vendorname')
            name = vendor_name.text if vendor_name is not None else None
            vendor_contact_name = vendor.find('contact/name')
            contact = vendor_contact_name.text if vendor_contact_name is not None else None
            vendor_contact_email = vendor.find('contact/email')
            email = vendor_contact_email.text if vendor_contact_email is not None else None
            self.vendor_list.append({'vendor_name': name, 'contact_name': contact, 'contact_email': email})
        else:
            self.vendor_list.append({'vendor_name': None, 'contact_name': None, 'contact_email': None})

        provider = self.root.find('.//provider')
        if provider is not None:
            provider_name = provider.find('name')
            name = provider_name.text if provider_name is not None else None
            provider_email = provider.find('email')
            email = provider_email.text if provider_name is not None else None
            provider_url = provider.find('url')
            url = provider_url.text if provider_url is not None else None
            self.provider_list.append({'provider_name': name, 'provider_email': email, 'provider_url': url})
        else:
            self.provider_list.append({'provider_name': None, 'provider_email': None, 'provider_url': None})


    #-------------------------------------------------------Display-------------------------------------------------------
    def displayinfo(self):
        print("Prospect Status:")
        for status in self.prospect_status:
            print(status)

        print("\nID List:")
        for id in self.id_list:
            print(id)

        print("\nRequest Date List:")
        for reqd in self.request_date_list:
            print(reqd)

        print("\nVehicle List:")
        for vehicle in self.vehicle_list:
            print(vehicle)

        print("\nCustomer List:")
        for customer in self.customer_list:
            print(customer)

        print("\nVendor List:")
        for vendor in self.vendor_list:
            print(vendor)

        print("\nProvider List:")
        for provider in self.provider_list:
            print(provider)

        print()


if __name__ == '__main__':
    l1 = 'lead1.xml'
    a = ParseXML()
    a.parse(l1)
    a.displayinfo()
