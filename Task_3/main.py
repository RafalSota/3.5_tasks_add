models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
#brand = []
#model = []
len_list = len(models)
years_sales = {}

if len(models) == len(sales2018) == len(sales2017) == len(sales2016):   #sprawdzenie czy listy mają taką samą długość
    print("\nwielkości poszczególnych list są zgodne")
else:
    print("\nwielkości poszczególnych list nie są zgodne")

for i in range (0,len_list):         
    brand = models[i].split()[0]
    model = models[i].split()[2]
    if brand not in cars:
        cars[brand] = {}
    cars[brand][model] = {
        "Sales": {
            "2016": 0 if sales2016[i] == "NA" else int(sales2016[i].replace(",", "")),
            "2017": 0 if sales2017[i] == "NA" else int(sales2017[i].replace(",", "")),
            "2018": 0 if sales2018[i] == "NA" else int(sales2018[i].replace(",", "")),
    }}

import pprint
pprint.pprint(cars)                  
#print(cars)

