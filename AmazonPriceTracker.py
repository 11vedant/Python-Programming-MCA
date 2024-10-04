from requests_html import HTMLSession

s  = HTMLSession()

r = s.get('https://www.amazon.in/FUJIFILM-Mirrorless-Camera-18-55mm-Black/dp/B0BRY644T2')

r.html.render(sleep=1)
price = r.html.find('#price_inside_buybox')[0].text
print(price) 