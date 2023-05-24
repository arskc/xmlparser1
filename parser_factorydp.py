import xml.etree.ElementTree as ET
from datetime import datetime
import json
import re

class ADF:
    def __init__(self):
        self.adf_info = {}
        self.tree = None
        self.root = None
        self.lead = None
    
    def ParseADF(self, lead):
        self.lead = lead
        self.tree = ET.parse(lead)
        self.root = self.tree.getroot()
        prospect = Prospect().ParseProspect(self.root)
        id = ID().ParseID(self.root)
        vehicle = Vehicle().ParseVehicles(self.root)
        customer = Customer().ParseCustomer(self.root)
        vendor = Vendor().ParseVendor(self.root)
        provider = Provider().ParseProvider(self.root)
        self.adf_info.update({'prospect': prospect,
                              'id': id,
                              'vehicle': vehicle,
                              'customer': customer,
                              'vendor': vendor,
                              'provider': provider})
        
    def CreateJSONObject(self):
        j = json.dumps(self.adf_info)
        jfile = re.sub(".xml", "", self.lead) + '.json'
        with open(jfile, 'w') as f:
            f.write(j)
            f.close()
        
    def DisplayADF(self):
        print("\n----------------------------------------------------------------------------------------------------------------------\n")
        print(self.adf_info)
        print("\n----------------------------------------------------------------------------------------------------------------------\n")
        print()

class Prospect:
    def __init__(self):
        self.prospect_status = {}

    def ParseProspect(self, root) -> dict:
        prospect = root.find('.//prospect')
        status = prospect.get('status') if prospect is not None else None
        self.prospect_status['status'] = status
        return self.prospect_status

class ID:
    def __init__(self):
        self.info = {}

    def ParseID(self, root) -> dict:
        id = root.find('.//id')
        if id is not None:  
            sequence = id.get('sequence')
            source = id.get('source')
            i = id.text
            self.info.update({'sequence': sequence, 
                                       'source': source, 
                                       'id': i})
        else:
            self.info.update({'sequence': None, 
                                       'source': None})
        return self.info

class Request_Date:
    def __init__(self):
        self.request_date_info = {}

    def ParseRequestDate(self, root) -> dict:
        requestdatenode = root.find('.//requestdate')
        if requestdatenode is not None:
            requestdate = datetime.fromisoformat(requestdatenode.text)
            self.request_date_info.update({'requestdate': requestdate})
        else:
            self.request_date_info.update({'requestdate': None})  

class Vehicle:
    def __init__(self):
        self.vehicle_info = {}

    def ParseVehicles(self, root) -> dict:
        vehiclenode = root.find('.//vehicle')
        if vehiclenode is not None:
            interest = vehiclenode.get('interest')
            status = vehiclenode.get('status')
            id = ID().ParseID(vehiclenode)
            year = vehiclenode.find('year').text if vehiclenode.find('year') is not None else None
            make = vehiclenode.find('make').text if vehiclenode.find('make') is not None else None
            model = vehiclenode.find('model').text if vehiclenode.find('model') is not None else None
            vin = vehiclenode.find('vin').text if vehiclenode.find('vin') is not None else None
            stock = vehiclenode.find('stock').text if vehiclenode.find('stock') is not None else None
            trim = vehiclenode.find('trim').text if vehiclenode.find('trim') is not None else None
            doors = vehiclenode.find('doors').text if vehiclenode.find('doors') is not None else None
            bodystyle = vehiclenode.find('bodystyle').text if vehiclenode.find('bodystyle') is not None else None
            odometer = Odometer().ParseOdometer(vehiclenode)
            condition = vehiclenode.find('condition').text if vehiclenode.find('condition') is not None else None
            colorcombination = ColorCombination().ParseColorCombination(vehiclenode)
            imagetag = ImageTag().ParseImageTag(vehiclenode)
            price = Price().ParsePrice(vehiclenode)
            pricecomments = vehiclenode.find('pricecomments').text if vehiclenode.find('pricecomments') is not None else None
            option = Option().ParseOption(vehiclenode)
            finance = Finance().ParseFinance(vehiclenode)
            comments = vehiclenode.find('comments').text if vehiclenode.find('comments') is not None else None
            self.vehicle_info.update({'interest': interest,
                                      'status': status,
                                      'id': id,
                                      'year': year, 
                                      'make': make, 
                                      'model': model,
                                      'vin': vin,
                                      'stock': stock,
                                      'trim': trim,
                                      'doors': doors,
                                      'bodystyle': bodystyle,
                                      'odometer': odometer,
                                      'condition': condition,
                                      'colorcombination': colorcombination,
                                      'imagetag': imagetag,
                                      'price': price,
                                      'pricecomments': pricecomments,
                                      'option': option,
                                      'finance': finance,
                                      'comments': comments})
        else:
            self.vehicle_info.update({'interest': None,
                                      'status': None,
                                      'id': None,
                                      'year': None, 
                                      'make': None, 
                                      'model': None,
                                      'vin': None,
                                      'stock': None,
                                      'trim': None,
                                      'doors': None,
                                      'bodystyle': None,
                                      'odometer': None,
                                      'condition': None,
                                      'colorcombination': None,
                                      'imagetag': None,
                                      'price': None,
                                      'pricecomments': None,
                                      'option': None,
                                      'finance': None,
                                      'comments': None})
class Customer:
    def __init__(self):
        self.customer_info = {}

    def ParseCustomer(self, root) -> dict:
        customernode = root.find('.//customer')
        if customernode is not None:
            contact = Contact().ParseContact(customernode)
            id = ID().ParseID(customernode)
            timeframe = TimeFrame().ParseTimeFrame(customernode)
            comments = customernode.find('comments').text if customernode.find('comments') is not None else None
            self.customer_info.update({'contact': contact,
                                       'id': id,
                                       'timeframe': timeframe,
                                       'comments': comments})
        else:
            self.customer_info.update({'contact': None,
                                       'id': None,
                                       'timeframe': None,
                                       'comments': None})

class Vendor:
    def __init__(self):
        self.vendor_info = {}

    def ParseVendor(self, node):
        vendornode = node.find('.//vendor')
        if vendornode is not None:
            id = ID().ParseID(vendornode)
            vendorname = vendornode.find('vendorname').text if vendornode.find('vendorname') is not None else None
            url = vendornode.find('url').text if vendornode.find('url') is not None else None
            contact = Contact().ParseContact(vendornode)
            self.vendor_info.update({'id': id,
                                     'vendorname': vendorname,
                                     'url': url,
                                     'contact': contact})

class Provider:
    def __init__(self):
        self.provider_info = {}

    def ParseProvider(self, node) -> dict:
        providernode = node.find('.//provider')
        if providernode is not None:
            id = ID().ParseID(providernode)
            name = Name().ParseName(providernode)
            service = providernode.find('service').text if providernode.find('service') is not None else None
            url = providernode.find('url').text if providernode.find('url') is not None else None
            email = Email().ParseEmail(providernode)
            phone = Phone().ParsePhone(providernode)
            contact = Contact().ParseContact(providernode)
            self.provider_info.update({'id': id,
                                       'name': name,
                                       'service': service,
                                       'url': url,
                                       'email': email,
                                       'phone': phone,
                                       'contact': contact})
        else:
            self.provider_info.update({'id': None,
                                       'name': None,
                                       'service': None,
                                       'url': None,
                                       'email': None,
                                       'phone': None,
                                       'contact': None})
        return self.provider_info


class Contact:
    def __init__(self):
        self.contact_info = {}

    def ParseContact(self, node) -> dict:
        contactnode = node.find('.//contact')
        if contactnode is not None:
            primarycontact = contactnode.get('primarycontact')
            name = Name().ParseName(contactnode)
            email = Email().ParseEmail(contactnode)
            phone = Phone().ParsePhone(contactnode)
            address = Address().ParseAddress(contactnode)
            self.contact_info.update({'primarycontact': primarycontact,
                                      'name': name,
                                      'email': email,
                                      'phone': phone,
                                      'address': address})
        else:
            self.contact_info.update({'primarycontact': None,
                                      'name': None,
                                      'email': None,
                                      'phone': None,
                                      'address': None})
        return self.contact_info

class Price:
    def __init__(self):
        self.price_parameters = {}
    
    def ParsePrice(self, node) -> dict:
        pricenode = node.find('.//price')
        if pricenode is not None:
            ptype = pricenode.get('type')
            currency = pricenode.get('currency')
            delta = pricenode.get('delta')
            relativeto = pricenode.get('relativeto')
            source = pricenode.get('source')
            price = float(pricenode.text)
            self.price_parameters.update({'type': ptype, 
                                          'currency': currency, 
                                          'delta': delta, 
                                          'relativeto': relativeto, 
                                          'source': source, 
                                          'price': price})
        else:
            self.price_parameters.update({'type': None, 
                                          'currency': None, 
                                          'delta': None, 
                                          'relativeto': None, 
                                          'source': None, 
                                          'price': None})
        return self.price_parameters

class Name:
    def __init__(self):
        self.name_info = {}

    def ParseName(self, node) -> dict:
        namenode = node.find('.//name')
        if namenode is not None:
            part = namenode.get('part')
            type = namenode.get('type')
            name = namenode.text
            self.name_info.update({'part': part, 
                                   'type': type, 
                                   'name': name})
        else:
            self.name_info.update({'part': None, 
                                   'type': None, 
                                   'name': None})
        return self.name_info

class Email:
    def __init__(self):
        self.email_info = {}

    def ParseEmail(self, node) -> dict:
        emailnode = node.find('.//email')
        if emailnode is not None:
            preferredcontact = emailnode.get('preferredcontact')
            email = emailnode.text
            self.email_info.update({'preferredcontact': preferredcontact, 
                                    'email': email})
        else:
            self.email_info.update({'preferredcontact': None, 
                                    'email': None})
        return self.email_info

class Phone:
    def __init__(self):
        self.phone_info = {}

    def ParsePhone(self, node) -> dict:
        phonenode = node.find('.//name')
        if phonenode is not None:
            type = phonenode.get('type')
            time = phonenode.get('time')
            preferredcontact = phonenode.get('preferredcontact')
            phone = phonenode.text
            self.phone_info.update({'type': type, 
                                    'time': time, 
                                    'preferredcontact': preferredcontact, 
                                    'phone': phone})
        else:
            self.phone_info.update({'type': None, 
                                    'time': None, 
                                    'preferredcontact': None, 
                                    'phone': None})
        return self.phone_info

class Address:
    def __init__(self):
        self.address_info = {}

    def ParseAddress(self, node) -> dict:
        addressnode = node.find('.//address')
        if addressnode is not None:
            type = addressnode.get('type')
            street = addressnode.find('street').text if addressnode.find('street') is not None else None
            line = addressnode.get('line')
            apartment = addressnode.find('apartment').text if addressnode.find('apartment') is not None else None
            city = addressnode.find('city').text if addressnode.find('city') is not None else None
            regioncode = addressnode.find('regioncode').text if addressnode.find('regioncode') is not None else None
            postalcode = addressnode.find('postalcode').text if addressnode.find('postalcode') is not None else None
            country = addressnode.find('country').text if addressnode.find('country') is not None else None
            self.address_info.update({'type': type, 
                                      'street': {'street': street, 
                                                 'line': line}, 
                                      'apartment': apartment, 'city': city, 
                                      'regioncode': regioncode, 
                                      'postalcode': postalcode, 
                                      'country': country})
        else:
            self.address_info.update({'type': None, 
                                      'street': {'street': None, 
                                                 'line': None}, 
                                      'apartment': None, 'city': None, 
                                      'regioncode': None, 
                                      'postalcode': None, 
                                      'country': None})
        return self.address_info
            
class TimeFrame:
    def __init__(self):
        self. timeframe_info = {}
    
    def ParseTimeFrame(self, node) -> dict:
        timeframenode = node.find('.//timeframe')
        if timeframenode is not None:
            description = timeframenode.find('description').text if timeframenode.find('description') is not None else None
            earliestdate = datetime.fromisoformat(timeframenode.find('earliestdate').text if timeframenode.find('earliestdate') is not None else None)
            latestdate = datetime.fromisoformat(timeframenode.find('latestdate').text if timeframenode.find('latestdate') is not None else None)
            self.timeframe_info.update({'description': description,
                                        'earliestdate': earliestdate,
                                        'latestdate': latestdate})
        else:
            self.timeframe_info.update({'description': None,
                                        'earliestdate': None,
                                        'latestdate': None})
            return self.timeframe_info

class Odometer:
    def __init__(self):
        self.odometer_info = {}

    def ParseOdometer(self, node) -> dict:
        odometernode = node.find('.//odometer')
        if odometernode is not None:
            status = odometernode.get('status')
            units = odometernode.get('units')
            odometer = odometernode.find('odometer').text if odometernode.find('odometer') is not None else None
            self.odometer_info.update({'status': status,
                                       'units': units,
                                       'odometer': odometer})
        else:
            self.odometer_info.update({'status': None,
                                       'units': None,
                                       'odometer': None})
        return self.odometer_info

class ColorCombination:
    def __init__(self) -> None:
        self.colorcombination_info = {}

    def ParseColorCombination(self, node) -> dict:
        colorcombinationnode = node.find('.//colorcombination')
        if colorcombinationnode is not None:
            interiorcolor = colorcombinationnode.find('interiorcolor').text if colorcombinationnode.find('interiorcolor') is not None else None
            exteriorcolor = colorcombinationnode.find('exteriorcolor').text if colorcombinationnode.find('exteriorcolor') is not None else None
            preference = int(colorcombinationnode.find('preference').text if colorcombinationnode.find('preference') is not None else None)
            self.colorcombination_info.update({'interiorcolor': interiorcolor,
                                               'exteriorcolor': exteriorcolor,
                                               'preference': preference})
        else:
            self.colorcombination_info.update({'interiorcolor': None,
                                               'exteriorcolor': None,
                                               'preference': None})
        return self.colorcombination_info

class ImageTag:
    def __init__(self):
        self.imagetag_info = {}

    def ParseImageTag(self, node) -> dict:
        imagetagnode = node.find('.//imagetag')
        if imagetagnode is not None:
            width = imagetagnode.get('width')
            height = imagetagnode.get('height')
            alttext = imagetagnode.get('alttext')
            imagetag = imagetagnode.find('imagetag').text if imagetagnode.find('imagetag') is not None else None
            self.imagetag_info.update({'width': width,
                                       'height': height,
                                       'alttext': alttext,
                                       'imagetag': imagetag})
        else:
            self.imagetag_info.update({'width': None,
                                       'height': None,
                                       'alttext': None,
                                       'imagetag': None})
        return self.imagetag_info
    
class Option:
    def __init__(self):
        self.option_info = {}

    def ParseOption(self, node) -> dict:
        optionnode = node.find('.//option')
        if optionnode is not None:
            optionname = optionnode.find('optionname').text if optionnode.find('optionname') is not None else None
            manufacturercode = optionnode.find('manufacturercode').text if optionnode.find('manufacturercode') is not None else None
            stock = optionnode.find('stock').text if optionnode.find('stock') is not None else None
            weighting = optionnode.find('weighting').text if optionnode.find('weighting') is not None else None
            price = Price().ParsePrice(optionnode)
            self.option_info.update({'optionname': optionname,
                                     'manufacturercode': manufacturercode,
                                     'stock': stock,
                                     'weighting': weighting,
                                     'price': price})
        else:
            self.option_info.update({'optionname': None,
                                     'manufacturercode': None,
                                     'stock': None,
                                     'weighting': None,
                                     'price': None})
        return self.option_info

class Amount:
    def __init__(self):
        self.amount_info = {}
    
    def ParseAmount(self, node) -> dict:
        amountnode = node.find('amount')
        if amountnode is not None:
            atype = amountnode.get('type')
            limit = amountnode.get('limit')
            currency = amountnode.get('currency')
            self.amount_info.update({'type': atype,
                                     'limit': limit,
                                     'currency': currency})
        else:
            self.amount_info.update({'type': None,
                                     'limit': None,
                                     'currency': None})
        return self.amount_info

class Balance:
    def __init__(self):
        self.balance_info = {}
    
    def ParseBalance(self, node) -> dict:
        balancenode = node.find('balance')
        if balancenode is not None:
            btype = balancenode.get('type')
            currency = balancenode.get('currency')
            self.balance_info.update({'type': btype,
                                      'currency': currency})
        else:
            self.balance_info.update({'type': None,
                                       'currency': None})
        return self.balance_info

class Finance:
    def __init__(self):
        self.finance_info = {}
    
    def ParseFinance(self, node) -> dict:
        financenode = node.find('.//finance')
        if financenode is not None:
            method = financenode.find('method').text if financenode.find('method') is not None else None
            amount = Amount().ParseAmount(financenode)
            balance = Balance().ParseBalance(financenode)
            self.finance_info.update({'method': method,
                                      'amount': amount,
                                      'balance': balance})
        else:
            self.finance_info.update({'method': None,
                                      'amount': None,
                                      'balance': None})
        return self.finance_info
    
def main():
    lead1 = 'lead1.xml'
    adf = ADF()
    adf.ParseADF(lead1)
    adf.DisplayADF()
    adf.CreateJSONObject()

if __name__ == '__main__':
    main()
