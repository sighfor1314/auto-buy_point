## 網頁自動化-購買點卡 auto-buy_point
### 功能說明
<li>至網站自動購買點數</li>

### 建立account.ini
建立account.ini 儲存使用者資料及信用卡資料
```
['WEBSITES']
environment = <gash_url>

['ACCOUNT-INFO']
phone_number = <phone_number>
email = <email>
paid_method = <paid_method>
coupon = <coupon>
invoiceType = <invoiceType>
purchaser = <purchaser>
carrierType = <carrierType>
barcode = <barcode>

['CREDITCARD']
cardType = <cardType>
account = <account>
year = <year>
month = <month>
CVN = <CVN>
firstName = <firstName>
lastName = <lastName>
```
### main.py
程式起始點，輸入要購買的點數金額後，執行自動購買點數