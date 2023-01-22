from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir':'D:\ot'})

print('Сколько нужно спарсить фото?')
summa = int(input())

print('По какому запросу?')
zapros = str(input())

google_crawler.crawl(keyword= zapros, max_num = summa)