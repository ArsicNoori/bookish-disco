from kavenegar import *
def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('7173686B52674D57332B795079676E787A4961395A6D69446E4E474D524D70573044654C473049476776773D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'{code} کد تایید شما',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)