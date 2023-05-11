from src.pages.buy_gash import BuyGash
from src.utils import Actions
from src.pages.payment import Payment
from src.pages.creditcard import CreditCard
from src.pages.setOTP import SetOTP
def main():
   environment = "gash5400"
   driver = Actions(environment)
   gash =BuyGash(driver)
   gash.buyGash()
   gash = Payment(driver)
   gash.payment()
   gash =CreditCard(driver)
   gash.setCreditcard()
   gash = SetOTP(driver)
   gash.taishinBank()
   print(driver.read_json_file())
if __name__ == '__main__':
   main()