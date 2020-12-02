num = 2

with open('1920adress.txt', encoding='utf-8') as file:
    with open('js1920.txt','w',encoding='utf-8') as a:
        for line in file:
            if num == 1:
                line = line.rstrip('\n')
                text = f"    latlng: new kakao.maps.LatLng({line})\n}},\n"
                a.write(text)
                num += 1
            elif num == 2:
                line = line.rstrip('\n')
                text = f"{{\n    title: '{line}',\n"
                a.write(text)
                num = 1
