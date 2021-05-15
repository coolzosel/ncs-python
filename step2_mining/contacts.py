class Contacts:
    # 이닛메소드가 아닌 필드영역에 스팅타입 작성
    name = ''
    phone = ''
    email = ''
    address = ''

    # 프린트문 대신 리턴으로 문장 출력(string 메소드 간소화)
    def __str__(self):
        return f'이름: {self.name} \n' \
               f'전화번호: {self.phone} \n' \
               f'이메일: {self.email} \n' \
               f'주소: {self.address} \n'

class ContactsService:
    # 기능 단위로 구분하기 위해 서비스 클래스 생성 (여기에다 기능 메소드들 몰아줌)
    # 그리고 @staticmethod 태그 지우고 메소드들 인자값에 self 삽입 (main 메소드 제외)
    def set_contact(self):
        # obj에 Contact클래스 할당/값 받아옴
        obj = Contacts()
        obj.name = input("이름: ")
        obj.phone = input("전화번호: ")
        obj.email = input("메일: ")
        obj.address = input("주소: ")
        return obj


    def get_contacts(self, ls):
        for i in ls:
            print(i)


    def del_contact(self, ls, name):
        for i, j in enumerate(ls):  # enumerate: 인자 안에서 검색 = ls 안에서 j 검색. i = index
            if j.name == name:
                del ls[i]


    def print_menu(self):
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴선택 : ")
        return int(menu)


    @staticmethod
    def main():
        ls = []
        # service 객체 생성, 서비스 클래스 할당
        service = ContactsService()
        while 1:
            menu = service.print_menu()
            if menu == 1:
                t = service.set_contact()
                ls.append(t)
            elif menu == 2:
                service.get_contacts(ls)
            elif menu == 3:
                name = input("삭제할 이름: ")
                service.del_contact(ls, name)
            elif menu == 4:
                break


# 서비스클래스를 실행해야 기능 실행이 되겠쥬? ContactsService.main() 실행
if __name__ == '__main__':
    ContactsService.main()
