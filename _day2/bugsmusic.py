from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugsmusic:

    # 날짜별로 벅스뮤직 크롤링하려고함
    url = ''

    # 크롤링 메소드
    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'lxml') #parser 역할
        cnt_artist = 0
        cnt_title = 0
        # cnt는 카운트

        # attrs는 애트리뷰트/속성
        # find_all은 해당하는 태그/클래스를 찾겠다.(lxml/html상에서)
        for link1 in soup.find_all(name="p", attrs=({"class":"artist"})):
            cnt_artist += 1
            print(str(cnt_artist) + "위")
            print("아티스트 : " + link1.find('a').text)
        print('--------------------------------------')
        for link2 in soup.find_all(name="p", attrs=({"class":"title"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("노래제목 : " + link2.find('a').text)


    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210508&charthour=12'
        bugs.scrap()


if __name__ == '__main__':
    Bugsmusic.main()