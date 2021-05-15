from bs4 import BeautifulSoup
import  requests

class Wikipedia:

    url = ''

    def scrap(self):
        con = requests.get(self.url)
        soup = BeautifulSoup(con.content, 'lxml')
        # print(soup) #soup 전체 출력하니까 내용 많이 나와서 콘솔창이 더러움...find해서 원하는 것만 찾아주자.
        infoTable = soup.find("table", {"class": "wikitable sortable"})
        infoPrint = [] #출력리스트
        for i in infoTable.find_all('tr'): #tr 태그에 해당하는 거 찾기
            infolist = [] #정보리스트
        for j in i.find_all('td'): #td 태그에 해당하는 거 찾기
            info = j.get_text() #찾은 td 태그 정보 뽑아서 info에 할당
            infolist.append(info) # 리스트에 info 추가
        infoPrint.append(infolist) # 출력리스트에 추가 후 출력
        print(infoPrint)

    @staticmethod
    def main():
        wiki = Wikipedia()
        wiki.url = 'http://dh.aks.ac.kr/Encyves/wiki/index.php/%EC%A1%B0%EC%84%A0_%EC%84%B8%EC%A2%85'
        wiki.scrap()

if __name__ == '__main__':
    Wikipedia.main()