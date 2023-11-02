from scrapy.selector import Selector
import requests, re

#response=requests.get('https://www.20dcr.com/book/kuibazhishu2/')
#url= Selector(response=response).xpath('//*[@id="all-chapter"]/div/div[2]/div//a/@href').extract()
#book= Selector(response=response).xpath('/html/body/div/div[5]/div[1]/div[1]/div/div/div[1]/div[2]/h1/a/text()').extract()
#author= Selector(response=response).xpath('/html/body/div/div[5]/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div[1]').extract()

with open("我的治愈系游戏.txt", "w") as file:
    file.write('% '+"我的治愈系游戏"+'\n')
    file.write('% '+"青青树"+'\n\n\n')
    url = '/19/19023/628389001.html'
    for i in range(3024):
        response=requests.get('https://m.biqubook5.com'+url)
        #response.encoding = 'utf-8'

        head = Selector(response=response).xpath('//*[@id="chaptercontent"]/text()[1]').extract()
        body = Selector(response=response).xpath('//*[@id="chaptercontent"]/text()').extract()
        link = Selector(response=response).xpath('//*[@id="pb_next"]').extract()

        title = head[0]
        content = ''
        for j in body[1:-1:]:
            content += '\n'+j.strip('\u3000')
        url = (re.findall('href=\"(.+?)\" id=', link[0]))[0]


        file.write("# "+title+"\n")
        file.write(content+'\n')
