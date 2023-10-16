import requests
import json

class Service:
   url = "https://jsonplaceholder.typicode.com/users"

   def send(self):
      istek = requests.get(self.url)
      response = istek.json() #bu satır response u json olarak alır.
      return istek.json() # bu satırdaki json.dumps() methodu json veri tipinde aldığı veriyi işlenebilir bir hale dönüştürür.

   def parse_data(self):
      tut = self.send()
      x = tut["email"]
      print(x)

nesne = Service()
nesne.parse_data()