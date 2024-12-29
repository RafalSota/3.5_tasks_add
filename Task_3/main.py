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

#################################################
#Pytanie 1
#Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej answer1.

answer1 = "" # wskaż nazwę modelu jako string
answer1_sales = 0

#print(cars["Toyota"]["Yaris"]["Sales"]["2017"])
for brand_1, models_1 in cars.items():
    for model_1, info_1 in models_1.items():
        if info_1["Sales"]["2017"] > answer1_sales:
            answer1_sales = info_1["Sales"]["2017"]
            answer1 = "\n" + brand_1 + " " + model_1 + " był najlepiej sprzedającym się samochodem w 2017r. Sprzedaż wyniosła: " + str(answer1_sales) + "\n"

print(answer1)

#################################################
#Pytanie 2 v.1 - przez niedoczytanie zakres obejmuje cały okres sprzedaży, tj. 2016, 2017 i 2018r.

answer2 = "" # wskaż producenta jako string
producer_allsales = {}  #słownik producent: liczba sprzedanych szt ze wszystkich lat
producer_total_sales = 0    # liczba sprzedanych szt ze wszystkich lat
producer_allsales_max_sales = 0   #zmienna przetrzymująca liczbę najwięcej sprzedanych szt ze wszystkich lat
producer_allsales_max_brand = "" #zmienna przetrzymująca nazwę producenta, któy sprzedał najwięcej samochodów we wszystkich latach

for brand_2, models_2 in cars.items():
    producer_total_sales = 0
    for model_2, info_2 in models_2.items():
        #print(model_2, (info_2["Sales"].values()))  #sprzedaż danego modelu we wszystkich latach w postaci listy wartości
        #print(model_2, sum(info_2["Sales"].values()))   
        producer_total_sales += sum(info_2["Sales"].values())   #sprzedaż danego modelu jako suma ze szystkich lat
        #print(producer_total_sales)
    producer_allsales[brand_2] = producer_total_sales
    if producer_total_sales > producer_allsales_max_sales:
        producer_allsales_max_sales = producer_total_sales
        producer_allsales_max_brand = brand_2
    
print (f"{producer_allsales_max_brand} sprzedał najwięcej samochodów w całym okresie: {producer_allsales_max_sales} szt\n")

#################################################
#Pytanie 2 v.2 - zakres obejmuje 2018r.
#Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej answer2.

answer2 = "" # wskaż producenta jako string
producer_2018_sales = 0    # liczba sprzedanych szt 2018
producer_2018_max_sales = 0   #zmienna przetrzymująca liczbę najwięcej sprzedanych szt w 2018
producer_2018_max_brand = "" #zmienna przetrzymująca nazwę producenta, któy sprzedał najwięcej samochodów w 2018

for brand_2_2, models_2_2 in cars.items():
    producer_2018_sales = 0
    for model_2_2, info_2_2 in models_2_2.items():
        #print(model_2_2, (info_2_2["Sales"]['2018']))   #sprzedaż danego modelu w 2018r.
        producer_2018_sales += info_2_2["Sales"]["2018"]
        #print(brand_2_2, producer_2018_sales)   
    if producer_2018_sales > producer_2018_max_sales:
        producer_2018_max_sales = producer_2018_sales
        producer_2018_max_brand = brand_2_2
answer2 = producer_2018_max_brand + " sprzedał najwięcej samochodów w 2018r.: " + str(producer_2018_max_sales) + " szt\n"
    
print(answer2)


#################################################
#Pytanie 3
#Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, 
#a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej answer3.

answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria

for brand_3, models_3 in cars.items():
    for model_3, info_3 in models_3.items():
        if info_3["Sales"]["2016"] == 0 and info_3["Sales"]["2017"] > 0:
            answer3.append(model_3)

print(f"W 2016r. nie sprzedawały się, a w 2017r. weszły do sprzedaży modele: {answer3}\n")

#################################################
#Pytanie 4
#Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, 
#jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej answer4.
#dodatkowo zakładam, że jest to model w sprzedaży czyli sprzedaż > 0

answer4 = "" # wskaż nazwę modelu jako string
low_sales = 9999999999999999999999

for brand_4, models_4 in cars.items():
    for model_4, info_4 in models_4.items():
        for year, sales in info_4["Sales"].items():
            current_sales = sales
            current_year = year
            current_model = model_4
            if current_sales < low_sales and current_sales > 0:
                low_sales = current_sales
                low_sales_year = current_year
                answer4 = current_model
print(f"Najniższą roczną sprzedaż miał model {answer4} w roku {low_sales_year} w ilości szt: {low_sales}\n")

#################################################
#Pytanie 5
#O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej answer5. 

answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'
ford_sales_2017 = 0
ford_sales_2018 = 0

for model_5, info_5 in cars["Ford"].items():
    ford_sales_2017 += info_5["Sales"]["2017"]
    ford_sales_2018 += info_5["Sales"]["2018"]
answer5 = round((((ford_sales_2018 - ford_sales_2017) / ford_sales_2017) * 100), 2)
answer5 = "Zmiana procentowa sprzedaży wszystkich modeli Forda w 2018r. w stosunku do 2017r. zmieniła się o " + str(answer5) + "%\n"
print(answer5)