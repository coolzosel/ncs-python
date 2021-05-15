from selenium import webdriver
from bs4 import BeautifulSoup

class NaverMovie(object):

    chromedrvier = 'C:/Program Files (x86)/Google/Chrome/chromedriver'
    url = ''

    def scrap(self):
        driver = webdriver.Chrome(self.chromedrvier) #크롬드라이버 받아오기
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser') #html.parser가 lxml파서보다 나중에 나온거
        all_div = soup.find_all('div',{'class':'tit3'})
        for i in [div.a.string for div in all_div]: #div태그의 a태그 string태그 찾아서 포문출력
            print(i)
        driver.close() #드라이버 작동 끝내기

    @staticmethod
    def main():
        naver = NaverMovie()
        naver.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        naver.scrap()

if __name__ == '__main__':
    NaverMovie.main()