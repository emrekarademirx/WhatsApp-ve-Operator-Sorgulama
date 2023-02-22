number = "+905550000000"
is_valid, region, provider, whatsapp = check_phone_number(number)

if is_valid:
    print(f"The number is valid and belongs to {region}.")
    print(f"The service provider is {provider}.")
    if whatsapp:
        print("The number has a WhatsApp account.")
    else:
        print("The number does not have a WhatsApp account.")
else:
    print("The number is not valid.")
