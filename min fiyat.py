#program is beta pls use komisyon value between 0-100
#its created for small businnes to calculate commission amount
#komisyon miktarı= commission amount
#gelis fiyatı= production value
#satis = min value to sell with no loss
print(" program henüz beta aşamasındadır eğer düzgün ve hatasız bir şekilde kullanmak \nistiyorsanız komisyon değerini 0-100 arasında \n geliş fiyatını ise pozitif şekilde giriniz\n\n")
#explaining something about beta
satis = 0.1

komisyon = input("komisyon miktarı :")
gelis = input("gelis fiyatı :")

while satis-satis*int(komisyon)/100<int(gelis):
    satis += 1
if satis-satis*int(komisyon)/100>int(gelis):
        print(satis ,"tlye zararsız satabilirsin") #u must sell product satis value for no loss
print("\nçıkmak için enter bas") #press enter for exit
input()

#i used while loop for calculate min cost for any product
