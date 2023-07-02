'''
연결리스트 (linked list)
    저장된 각 데이터가 (데이터) + (다음 데이터의 포인터(주소값))로 이루어진 것으로
    한 방향으로만 탐색 가능한 구조

    정해진 인덱스 번호 없음
        head에 data,next 포함
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next # next에 값이 안 들어가면 None으로 침

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        '''
            7 3 9 1 6
        7 추가
            Node = (7, None)
            head = new_node 따라서 위에 있는 node가 head 됨
            
        3 추가
            Node = (3, None)
            head는 값이 있기에 self.head는 실행 안됨
            current 때문에 위에 있는 7의 Node가 (7, 3의 주소값)이 됨
            
        9 추가
            Node = (9, None)
            head는 겂이ㅣ 있기에 self.head는 실행 안됨
            current는 7을 바라보고 있음. 그치만 current.next는 None이 아니기에 (값이 있음)
            그래서 current은 7에서 3을 타깃으로 바꿈.
            그래서 Node = (3, 9의 주소값)이 되는거임
        
        the same happens as adding new numbers to this lest
        '''

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next #그치만 current.next은 none이기에 실행이 안됨

        current.next = new_node

    def insert_node(self, find_data, insert_data): #find_data = 9, insert_data = 99
        if self.head is None:
            return
        '''
        7
        3
        99 (9의 주소값)
        9
        1
        6
        
        
        '''
        if self.head.data == find_data:
            self.head = Node(insert_data, self.head)
            # (99, 9의 주소 값)

        current = self.head
        while current.next is not None:
            if current.next.data == find_data: # none이 아니니 다음 데이터와 find_data 비교
                new_node = Node(insert_data, current.next) #9의 주소값을 넣음
                current.next = new_node

                return

            current = current.next

        self.add_node(insert_data)

    def delete_node(self, del_data):
        if self.head is None:
            return
        '''
Head    7 (3의 주소값)
        3 (99의 주소값)
        99 (9의 주소값)
        9 (1의 주소값)
        1 (6의 주소값)
        6, None
        
        del_data = 1
        current = 9노드
        
        7 (3의 주소값)
        3 (99의 주소값)
        99 (9의 주소값)
        9 (6의 주소값)
        6, None
        
        none, none이기에 그냥 없애버림
        


        '''

        if self.head.data == del_data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None: #del_data가 아니면 계속 돌아감
            if current.next.data == del_data:
                current.next = current.next.next #값이 아니라 참조값
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end='\n')
            current = current.next

#실행 코드
linked_list = LinkedList()
linked_list.add_node(7)
linked_list.add_node(3)
linked_list.add_node(9)
linked_list.add_node(1)
linked_list.add_node(6)

linked_list.insert_node(9,99)

linked_list.delete_node(1)

linked_list.print_list()