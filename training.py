import newspaper
import csv
import datetime
csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "bbg_" + csv_date + ".csv"
f = open(csv_file_name, "w")
print(f)
writer = csv.writer（f,lineterminator="¥n"）
csv_header=["記事番号","タイトル","URL","サマリー"]
writer.writerow(csv_header)
url ="https://bloomberg.com"
website = newspaper.build(url)

i =0
for article in website.articles:
    csvlist =[]
    article.download()
    article.parse()
    article.nlp()
    ##print("記事", str(i), ":", article.title)
    ##print(article.url)
    ##print(article.summary, end = "¥n¥n")
    csvlist.append(str(i))
    csvlist.append(article.title)
    csvlist.append(article.url)
    csvlist.append(article.summary)
    write.writerow(csvlist)
       
    if i > 9:
        break
    i= i+1
    f.close()