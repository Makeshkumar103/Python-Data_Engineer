driver_name ='goWtham'

print("Driver Name is:", driver_name)
print(driver_name.lower())
print(driver_name.upper())
print(driver_name.capitalize())
print(driver_name.title())


mobile = '9876543210'
masked1 = mobile[-2:]
print(masked1)
masked_mobile = '******' + mobile[6:10]
print("Mobile Number:", masked_mobile) 

mobile = '9876543210'
masked = mobile[:2] + "*****" + mobile[-2:]
print(masked)


song = "shape OF you"
artist = "ed SHEERAN"

formatted = f"{song.title()} - {artist.title()}"
print(formatted)


location = "chennai central"
fixed_loaction = location.replace("Chennai Central","Thambaram")
print(fixed_loaction)

message = 'your uber booking id is:UB12345.Please keep it safe'
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)

promo_msg = "use zomato100 to get 100 off on your first order"
if "zomato100"in promo_msg:
    print('offer applied')

feedback = 'the driver was polite and ride was smooth'
print("position is:", feedback.find('polite'))

name = "gowtham Subramani"
initials="".join([word[0].upper() for word in name.split()])
print(initials)


dierty_input=" airport   "
clean =dierty_input.strip()
print(clean)

word = "the trip was amazing and the car was clean"
word_count = len(word.split())
# word_count = len(word.split('and'))
print(word_count)