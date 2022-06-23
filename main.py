import requests
import json


def get_data():
    cookies = {
        '__lhash_': '71978255bb52b6fc056cfcbc5c30a901',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MAIN_PAGE_VARIATION_1': '1',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20890904811',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '_ym_d': '1655382192',
        '_ym_uid': '1639339296644021785',
        'advcake_session_id': '9f3523b3-1ad9-2922-1928-1f0783a8cecb',
        'advcake_track_id': 'c7500614-7927-a13e-94d1-97552f44ea20',
        'tmr_lvidTS': '1639339292804',
        'tmr_lvid': '205a34fec132792ffda518c21b99efd3',
        'AF_SYNC': '1655382200141',
        'afUserId': 'cff34d6c-8597-4bce-ad79-d7d54228d9f1-p',
        'flocktory-uuid': '321fb21f-afde-4bae-88ef-3ca2e3edf9fd-8',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqQiVgLREZO3t2bkRsIigmDWlwSidxemkzdGl5ETMwCX9BDh5wCUFdTiIbKWEaQglADxh4GkJrHmBJXihIRk5/Kh4Uf20nTw8SXD4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0ZydjE9aSBnSF8lP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYBDKyXA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqQiVgLREZO3t2bkRsIigmDWlwSidxemkzdGl5ETMwCX9BDh5wCUFdTiIbKWEaQglADxh4GkJrHmBJXihIRk5/Kh4Uf20nTw8SXD4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0ZydjE9aSBnSF8lP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYBDKyXA==',
        'deviceType': 'desktop',
        'cfidsgib-w-mvideo': 'WKO2nVacvBgWCPxb2z8XxgwHk8ZvlneocHNzI651CyrjfYlP1hlIcxrMJC4GhDHttis3lBk/SJZeQfBfYFVYrr1LNmve/7QHfnsUFgj8tMAfCFgq+PfUPd7bjo50lQj/YywHTQdLfhK4mTcDUzO/LhQUBtfYBwfPjct7',
        'gsscgib-w-mvideo': '3Fo5ToOULrU9GHh09XARUPoFBWjFtp5O1oyujsd4cIX/ctEJqxT1XwIhz/kORbp2TKHFBwM0GdKJLa0ioi+w9WO6uJMrHLUZB/XC65mE+IBTaELSVT+N3y5sXCMNu20Y4j6eYoW4e5gLEHHghJJ+nvM9LfkdI1k3eCprlAEafLSFgxkeFP6BGdyN8rb2GKGGnAnmgtirbP8apWBVXhmW3BJ3quUMqdLSUrsl9TVwdmC2QxR0UzxjrEm4YhRyWA==',
        'cfidsgib-w-mvideo': 'WKO2nVacvBgWCPxb2z8XxgwHk8ZvlneocHNzI651CyrjfYlP1hlIcxrMJC4GhDHttis3lBk/SJZeQfBfYFVYrr1LNmve/7QHfnsUFgj8tMAfCFgq+PfUPd7bjo50lQj/YywHTQdLfhK4mTcDUzO/LhQUBtfYBwfPjct7',
        'gsscgib-w-mvideo': '3Fo5ToOULrU9GHh09XARUPoFBWjFtp5O1oyujsd4cIX/ctEJqxT1XwIhz/kORbp2TKHFBwM0GdKJLa0ioi+w9WO6uJMrHLUZB/XC65mE+IBTaELSVT+N3y5sXCMNu20Y4j6eYoW4e5gLEHHghJJ+nvM9LfkdI1k3eCprlAEafLSFgxkeFP6BGdyN8rb2GKGGnAnmgtirbP8apWBVXhmW3BJ3quUMqdLSUrsl9TVwdmC2QxR0UzxjrEm4YhRyWA==',
        'fgsscgib-w-mvideo': 'Qkfo526303186fb67e2081fac6836f9832b1e80f',
        'fgsscgib-w-mvideo': 'Qkfo526303186fb67e2081fac6836f9832b1e80f',
        'cfidsgib-w-mvideo': 'WiYCleNWTOjRIzKM2PscvdYbPooxqSc0TbQagVMcD6fjIptX9KJEyxy69AU0ZzuFTBS5Gl6R8RVBSAVz7GZkwGor1LHZZk7JPWR1aOACH26VhYe+vB02+qFEFZDOoYmw5mpklk9fkC5JDo8XF00zkXg+QkqwdROcFARm',
        'CACHE_INDICATOR': 'false',
        '__ttl__widget__ui': '1655382554921-960269f56d46',
        'flacktory': 'no',
        'MVID_ENVCLOUD': 'primary',
        'SMSError': '',
        'authError': '',
        '_gid': 'GA1.2.1654334014.1655941768',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        '_ym_isad': '1',
        'mindboxDeviceUUID': '328ce476-af5f-4686-bd42-e91ea3f9c670',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22328ce476-af5f-4686-bd42-e91ea3f9c670%22%7D',
        '_ga': 'GA1.2.2020476695.1655382188',
        'tmr_detect': '1%7C1655941775370',
        '_ga_BNX5WPP3YK': 'GS1.1.1655941767.4.1.1655941786.41',
        '_ga_CFMZTSS5FM': 'GS1.1.1655941767.4.1.1655941786.0',
        'tmr_reqNum': '150',
        'JSESSIONID': 'qBFFvzqQ40812STZcPFKrfDmvW0j29brK1MTKv10fzv6cZqk6p6h!-1760608468',
        'bIPs': '-826759811',
        'ADRUM_BT': 'R:78|g:25412e80-3ecb-459e-af2f-12d2b094b255254757',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=71978255bb52b6fc056cfcbc5c30a901; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MAIN_PAGE_VARIATION_1=1; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20890904811; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; _ym_d=1655382192; _ym_uid=1639339296644021785; advcake_session_id=9f3523b3-1ad9-2922-1928-1f0783a8cecb; advcake_track_id=c7500614-7927-a13e-94d1-97552f44ea20; tmr_lvidTS=1639339292804; tmr_lvid=205a34fec132792ffda518c21b99efd3; AF_SYNC=1655382200141; afUserId=cff34d6c-8597-4bce-ad79-d7d54228d9f1-p; flocktory-uuid=321fb21f-afde-4bae-88ef-3ca2e3edf9fd-8; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqQiVgLREZO3t2bkRsIigmDWlwSidxemkzdGl5ETMwCX9BDh5wCUFdTiIbKWEaQglADxh4GkJrHmBJXihIRk5/Kh4Uf20nTw8SXD4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0ZydjE9aSBnSF8lP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYBDKyXA==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqQiVgLREZO3t2bkRsIigmDWlwSidxemkzdGl5ETMwCX9BDh5wCUFdTiIbKWEaQglADxh4GkJrHmBJXihIRk5/Kh4Uf20nTw8SXD4zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0ZydjE9aSBnSF8lP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQVRYBDKyXA==; deviceType=desktop; cfidsgib-w-mvideo=WKO2nVacvBgWCPxb2z8XxgwHk8ZvlneocHNzI651CyrjfYlP1hlIcxrMJC4GhDHttis3lBk/SJZeQfBfYFVYrr1LNmve/7QHfnsUFgj8tMAfCFgq+PfUPd7bjo50lQj/YywHTQdLfhK4mTcDUzO/LhQUBtfYBwfPjct7; gsscgib-w-mvideo=3Fo5ToOULrU9GHh09XARUPoFBWjFtp5O1oyujsd4cIX/ctEJqxT1XwIhz/kORbp2TKHFBwM0GdKJLa0ioi+w9WO6uJMrHLUZB/XC65mE+IBTaELSVT+N3y5sXCMNu20Y4j6eYoW4e5gLEHHghJJ+nvM9LfkdI1k3eCprlAEafLSFgxkeFP6BGdyN8rb2GKGGnAnmgtirbP8apWBVXhmW3BJ3quUMqdLSUrsl9TVwdmC2QxR0UzxjrEm4YhRyWA==; cfidsgib-w-mvideo=WKO2nVacvBgWCPxb2z8XxgwHk8ZvlneocHNzI651CyrjfYlP1hlIcxrMJC4GhDHttis3lBk/SJZeQfBfYFVYrr1LNmve/7QHfnsUFgj8tMAfCFgq+PfUPd7bjo50lQj/YywHTQdLfhK4mTcDUzO/LhQUBtfYBwfPjct7; gsscgib-w-mvideo=3Fo5ToOULrU9GHh09XARUPoFBWjFtp5O1oyujsd4cIX/ctEJqxT1XwIhz/kORbp2TKHFBwM0GdKJLa0ioi+w9WO6uJMrHLUZB/XC65mE+IBTaELSVT+N3y5sXCMNu20Y4j6eYoW4e5gLEHHghJJ+nvM9LfkdI1k3eCprlAEafLSFgxkeFP6BGdyN8rb2GKGGnAnmgtirbP8apWBVXhmW3BJ3quUMqdLSUrsl9TVwdmC2QxR0UzxjrEm4YhRyWA==; fgsscgib-w-mvideo=Qkfo526303186fb67e2081fac6836f9832b1e80f; fgsscgib-w-mvideo=Qkfo526303186fb67e2081fac6836f9832b1e80f; cfidsgib-w-mvideo=WiYCleNWTOjRIzKM2PscvdYbPooxqSc0TbQagVMcD6fjIptX9KJEyxy69AU0ZzuFTBS5Gl6R8RVBSAVz7GZkwGor1LHZZk7JPWR1aOACH26VhYe+vB02+qFEFZDOoYmw5mpklk9fkC5JDo8XF00zkXg+QkqwdROcFARm; CACHE_INDICATOR=false; __ttl__widget__ui=1655382554921-960269f56d46; flacktory=no; MVID_ENVCLOUD=primary; SMSError=; authError=; _gid=GA1.2.1654334014.1655941768; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; _ym_isad=1; mindboxDeviceUUID=328ce476-af5f-4686-bd42-e91ea3f9c670; directCrm-session=%7B%22deviceGuid%22%3A%22328ce476-af5f-4686-bd42-e91ea3f9c670%22%7D; _ga=GA1.2.2020476695.1655382188; tmr_detect=1%7C1655941775370; _ga_BNX5WPP3YK=GS1.1.1655941767.4.1.1655941786.41; _ga_CFMZTSS5FM=GS1.1.1655941767.4.1.1655941786.0; tmr_reqNum=150; JSESSIONID=qBFFvzqQ40812STZcPFKrfDmvW0j29brK1MTKv10fzv6cZqk6p6h!-1760608468; bIPs=-826759811; ADRUM_BT=R:78|g:25412e80-3ecb-459e-af2f-12d2b094b255254757',
        'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-set-application-id': '14d4b8d3-e4c8-4775-8f20-52ee3d96acca',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyLQotC+0LLQsNGA0Ysg0YHQviDRgdC60LjQtNC60L7QuSIsIi04Iiwi0JHQvtC70LXQtSA1JSJd',
            'WyLQotC+0LvRjNC60L4g0LIg0L3QsNC70LjRh9C40LgiLCItOSIsItCU0LAiXQ==',
        ],
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_isd.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

    # ###################################################################

    with open('5_result.json') as file:
        result = json.load(file)

    for item in result:
        item_name = item.get('name')
        item_basePrice = item.get('item_basePrice')
        item_salePrice = item.get('item_salePrice')
        item_bonus = item.get('item_bonus')
        discount = item_basePrice - item_salePrice
        print(f"\nНазвание {item_name}\nСтарая цена:{item_basePrice}\nНовая цена:{item_salePrice} (Скидка: {discount})\nБонусы за покупку:{item_bonus}")


def main():
    get_data()
    get_result()


if __name__ == '__main__':
   main()