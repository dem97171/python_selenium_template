from bs4 import BeautifulSoup
import urllib.request
import requests
import re

baseUrl = 'http://sp.keiba.go.jp'

def loadMonthlyRaceLinks(year, month):
    '''
    地方競馬情報サイト keiba.go.jpの携帯サイト sp.keiba.go.jp から月別検索で帯広ばんえい競馬の year 年 month 月のレース情報へのリンク一覧を取得して返す。
    '''
    monthlyRaceLinks = []
    url = baseUrl + '/KeibaWebSP/MonthlyConveneInfo/S_ConveneNiteiRacecourse?k_jyo=' + urllib.parse.quote('帯広ば') + '&k_year=' + year + '&k_month=' + month
    # print(url)
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    response.close()
    monthlyRaceLinkDoms = soup.find('div', id="tbl-month-program").find_all('a', href=re.compile("^/KeibaWebSP/TodayRaceInfo/S_RaceList*"))
    # print(monthlyRaceLinkDoms)
    for raceLinkDom in monthlyRaceLinkDoms:
        monthlyRaceLinks.append( baseUrl + raceLinkDom.get('href') )
    # print(monthlyRaceLinks)
    return monthlyRaceLinks

# def fetchHorseBsObj(horseUrl):
#     '''
#     beautiful soup4で取得した馬情報ページのDOM情報を返す
#     '''

#     # URLから個別の馬データを取得
#     horseResponse = urllib.request.urlopen(horseUrl)
#     print(horseUrl)
#     horseBs = BeautifulSoup(horseResponse, "html.parser")
#     return horseBs


# def fetchHorseName(horseBs):
#     '''
#     bs4用に取得したDOM情報から馬名を取得して返す。
#     '''
#     horseName = horseBs.find('section', id="box_pg").find('h2', class_='ttl_d').string
#     print(horseName)
#     return horseName

# def fetchHorseInfo(horseBs):
#     '''
#     馬の個別情報を取得
#     '''
#     tdList = horseBs.find('section', id="box_pg").find_all('td')
#     print(tdList)
#     return tdList

# def isExistHorseRecord(horseUrl):
#     '''
#     horseUrlがすでにテーブル上に登録されているかを判定する
#     '''
#     queryObj = {
#         'url': horseUrl
#     }
#     json_data = json.dumps(queryObj).encode("utf-8")
#     headers = {"Content-Type" : "application/json"}
#     requestUrl = "http://localhost:8080/mldataregister/CFAPI/horse_count.cfm"
#     result = requests.post(requestUrl, data=json_data, headers=headers)
#     print(result.json())
#     if(result.json()['exist'] == 'true'):
#         print('return trueeeee')
#         return True
#     else:
#         print('return falseeeee')
#         return False


# def printProgress(index, length):
#     print(str(index) + '/' + str(length))

# def reshapeRegistrationData(horseName, horseInfo, horseUrl):
#     queryObj = {
#         'name': horseName,
#         'father': horseInfo[0].string,
#         'mother': horseInfo[1].string,
#         'mothersfather': horseInfo[2].string,
#         'color': horseInfo[3].string,
#         'sex': horseInfo[4].string,
#         'birthday': horseInfo[6].string,
#         'orner': horseInfo[7].string,
#         'origin': horseInfo[8].string,
#         'url': horseUrl
#     }
#     print(queryObj)
#     return queryObj

# def registerHorse(queryObj):
#     json_data = json.dumps(queryObj).encode("utf-8")
#     headers = {"Content-Type" : "application/json"}
#     requestUrl = "http://localhost:8080/mldataregister/CFAPI/horse.cfm"
#     result = requests.post(requestUrl, data=json_data, headers=headers)
#     print(result.text)


def main():
    year = '2019'   # yyyy
    month = '1'     # 1 ~ 12

    # 開催日程検索（開催場）で2019年1月の帯広の開催日リストのリンク情報を全て取得する
    monthlyRaceLinks = loadMonthlyRaceLinks(year, month)

    # 開催日一覧で、開催レース一覧画面へのリンクを全て取得する。(出馬表、競走成績、払戻金、(変更情報))
    for monthlyRaceLink in monthlyRaceLinks:
        print(monthlyRaceLink)
    sampleUrl = 'http://sp.keiba.go.jp/KeibaWebSP/TodayRaceInfo/S_RaceList?k_raceDate=2019/01/01&k_babaCode=3'


    # 出馬表のデータを取得して取り込む

    # 競走成績のデータを取得して取り込む

    # 払戻金のデータを取得して取り込む

    # 変更情報があれば取得して取り込む



    # linkDoms = fetchLinkDoms()
    # i=0
    # for aTagObj in linkDoms:
    #     horseUrl = baseUrl + '/' + aTagObj.get('href')
    #     horseBs = fetchHorseBsObj(horseUrl)

    #     # 進捗件数表示
    #     i+=1;
    #     printProgress(i, len(linkDoms))

    #     # 登録ずみかどうか判定
    #     if(isExistHorseRecord(horseUrl)):
    #         print("skip")
    #         continue

    #     # 馬名を取得
    #     horseName = fetchHorseName(horseBs)

    #     # 馬情報を取得
    #     horseInfo = fetchHorseInfo(horseBs)

    #     # 登録データ整形
    #     queryObj = reshapeRegistrationData(horseName, horseInfo, horseUrl)

    #     # CFのAPIに登録のリクエストをぶん投げる
    #     registerHorse(queryObj)

    #     time.sleep(10)


main()
