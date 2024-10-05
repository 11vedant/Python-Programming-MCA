from requests_html import HTMLSession


urls = ['https://www.amazon.in/Samsung-Inches-Wondertainment-UA32T4340BKXXL-Glossy/dp/B09F6S8BT6/ref=sr_1_3?keywords=samsung%2Btv&qid=1687798898&sr=8-3&th=1',
	'https://www.amazon.in/Sony-Bravia-inches-Google-KD-65X74K/dp/B09WN3SRC7/ref=sr_1_5?content-id=amzn1.sym.f0166a2b-0975-4017-be10-7ecf88afb403%3Aamzn1.sym.f0166a2b-0975-4017-be10-7ecf88afb403&keywords=sony+tv&pd_rd_r=a1c7b32f-82b6-450c-a7a5-bfae4a91dc0f&pd_rd_w=m2KpE&pd_rd_wg=dl9zc&pf_rd_p=f0166a2b-0975-4017-be10-7ecf88afb403&pf_rd_r=2S8CTT2CNYDBB8DABP7T&qid=1687801369&sr=8-5',
 	'https://www.amazon.in/dp/B0B6W5Y36R/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0B6W5Y36R&pd_rd_w=JLNhJ&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=ZFQSA6KCBSEX4KHAVVJR&pd_rd_wg=nezhA&pd_rd_r=6fc7f3fc-74b9-40ae-927a-1698c3445e6d&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw']



def getprice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    
    
    product = {
        'title': r.html.xpath('//*[@id="productTitle"]',first=True).text,
        'price': r.html.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]', first = True).text
        
    }
    print(product)
    return product


tvprices = []
for url in urls:
	tvprices.append(getprice(url))

print(len(tvprices))