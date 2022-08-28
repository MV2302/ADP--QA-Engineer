
import requests

url= "https://restful-booker.herokuapp.com/booking"

headers={"Content-type":"application/json"}
data = {
    "firstname" : "Robert",
    "lastname" : "Papel",
    "totalprice" : 89,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2022-09-05",
        "checkout" : "2022-09-05"
    },
    "additionalneeds" : "Toothpaste"
}

r=requests.post(url=url,json=data,headers=headers, verify=True)
print(r.status_code)
print(r.text)


