import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import message

def check_phone_number(number):
    try:
        parsed_number = phonenumbers.parse(number, "TR")
        if phonenumbers.is_valid_number(parsed_number):
            if phonenumbers.is_possible_number(parsed_number):
                region = geocoder.description_for_number(parsed_number, "tr")
                service_provider = carrier.name_for_number(parsed_number, "tr")
                whatsapp_check = message.is_whatsapp_number(parsed_number)
                return True, region, service_provider, whatsapp_check
            else:
                return False, None, None, None
        else:
            return False, None, None, None
    except phonenumbers.phonenumberutil.NumberParseException:
        return False, None, None, None
