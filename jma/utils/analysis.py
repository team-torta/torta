import xml.etree.ElementTree as ET
import urllib.request

def analysis_xml(uuid):
    url = 'http://www.data.jma.go.jp/developer/xml/data/' + uuid + '.xml'
    req = urllib.request.Request(url)

    # XMLを読み込み
    with urllib.request.urlopen(req) as response:
        XmlData = response.read()
    root = ET.fromstring(XmlData)

    # 気象庁XMLのBodyのネームスペース
    ns = '{http://xml.kishou.go.jp/jmaxml1/body/seismology1/}'

    # 市区町村名、市区町村コード、市区町村の最大震度リスト
    citys_list = []
    for city in root.iter(ns + 'City'):
        name = city.find(ns + 'Name').text
        code = city.find(ns + 'Code').text
        maxint = city.find(ns + 'MaxInt').text
        list = [name, code, maxint]
        citys_list.append(list)

    print(citys_list)
