
#нужно сохранить на новый branch
#добаить на главну

products = {
    
    "shop": "Alexa&Co",
    "project": 
    "deals": [
        {
            'id':'74826894',
            'status': 'Принят',
            'name': 'Test Test Test',
            'delivery': 'Test Test Test',
            'payment type': 'Наложенный платеж',
            'payment status': 'Не оплачен',
            'cart': [
                {
                    'id': '10001003',
                    'count': '1',
                    'price_sku': '54'
                }
            ]

        },
        {
            'id':'74826904',
            'status': 'Принят',
            'name': 'Test Test Test',
            'delivery': 'Test Test Test',
            'payment type': 'Наложенный платеж',
            'payment status': 'Не оплачен',
            'cart': [
                {
                    'id': '10001005',
                    'count': '2',
                    'price_sku': '500'
                },
                {
                    'id': '10001003',
                    'count': '10',
                    'price_sku': '54'
                },
                {
                    'id': '10001010',
                    'count': '1',
                    'price_sku': '100'
                }
            ]
        },
        {
            'id':'74827003',
            'status': 'Принят',
            'name': 'Test Test Test',
            'delivery': 'Test Test Test',
            'payment type': 'Онлайн оплата / Visa / LiqPay',
            'payment status': 'Оплачен',
            'cart': [
                {
                    'id': '10001040',
                    'count': '5',
                    'price_sku': '40'
                }
            ]
        },
        {
            'id':'74827043',
            'status': 'Отмена. Нет в наличии.',
            'name': 'Test Test Test',
            'delivery': 'Test Test Test',
            'payment type': 'Наложенный платеж',
            'payment status': 'Не оплачен',
            'cart': [
                {
                    'id': '10001001',
                    'count': '1',
                    'price_sku': '399'
                }
            ]
        },
        {
            'id':'74827053',
            'status': 'Отмена. Купил на другом сайте.',
            'name': 'Test Test Test',
            'delivery': 'Test Test Test',
            'payment type': 'Наложенный платеж',
            'payment status': 'Не оплачен',
            'cart': [
                {
                    'id': '10001044',
                    'count': '1',
                    'price_sku': '14099'
                }
            ]
        }
    ]
}
#Первый вывод:количество всех заказов
new_list_for_summa=[]
for ide in products["deals"]:
    cart_in_ide=ide['cart']
    for cart_ide in cart_in_ide:
        sum_zakaz_id=cart_ide['count']
        new_list_for_summa.append(int(sum_zakaz_id))      
summa_all_zakaz=sum(new_list_for_summa)
print("Итоговая сумма заказов за",products["date"],":",summa_all_zakaz)
#количество и сумма потенциально успешных заказов
new_list_for_unit=[]
new_list_for_winner2=[]
new_list_for_neunit=[]
new_list_for_newinner2=[]

for id_dic in products["deals"]:
    status_dic=id_dic['status']
    #для принятых заказов(грн и сумма)
    if status_dic== "Принят":
        cart_dic=id_dic['cart']
        for k  in cart_dic :
            sum_zakaz = k['count']
            new_list_for_unit.append(int(sum_zakaz))
        for y in cart_dic:
            cost=y['price_sku']
            new_list_for_winner2.append(int(cost))
    #для отмененных заказов (грн и сумма)
    else: 
        cart_dic=id_dic['cart']
        for g  in cart_dic :
            sum_nezakaz = g['count']
            new_list_for_neunit.append(int(sum_nezakaz))
        for y in cart_dic:
            cost=y['price_sku']
            new_list_for_newinner2.append(int(cost))
together_ua_unit=[]
together_ua_neunit=[]
#для принятых
for to in range(0,len(new_list_for_unit)):
    r=new_list_for_unit[to]*new_list_for_winner2[to]
    together_ua_unit.append(r)
summa_winner_zakaz=sum(new_list_for_unit)
summa_ua=sum(together_ua_unit)
#для отклоненных
for no in range(0,len(new_list_for_neunit)):
    r=new_list_for_neunit[no]*new_list_for_newinner2[no]
    together_ua_neunit.append(r)
summa_newinner_zakaz=sum(new_list_for_neunit)
summa_neua=sum(together_ua_neunit)
print("Итоговая бюджет ПРИНЯТЫХ заказов за",products["date"],":",summa_ua,"грн")
print("Итоговая сумма ПРИНЯТЫХ заказов за",products["date"],":",summa_winner_zakaz)

print("Итоговая бюджет ОТМЕНЕННЫХ заказов за",products["date"],":",summa_neua,"грн")
print("Итоговая сумма ОТМЕНЕННЫХ заказов за",products["date"],":",summa_newinner_zakaz)



