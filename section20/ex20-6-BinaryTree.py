'''
트리 자료구조
    단 하나의 루트 노드가 있고, 루트 노드에서 하위 노드들이 연결된
    비선형 계층구조이다

이진트리 (Binary Tree)
    모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다
    왼쪽 서브 트리의 값은
'''

class TreeNode:
    def __init__(self, value):
        self.value = value # 노드의 값
        self.left = None # 왼쪽 서브트리 노드
        self.right = None # 오른쪽 서브트리 노드

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root) # 루트노드

    # 전위순회 root -> left -> right
    def preorder_traversal(self,start,traversal):
        if start:
            traversal += (str(start.value) + '#')
            traversal = self.preorder_traversal(start.left, traversal) #5의 left부터 return
            traversal = self.preorder_traversal(start.right, traversal) #5의 right return
        return traversal

    #중위순회 left -> root -> right
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '#')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # 후위순회 left -> right -> value
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + ' ')
        return traversal

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, current_node):
        if not current_node:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)
    '''
    3 7 2 4 8
    
    value = 3
    current_node = TreeNode(5) -> current_node.left = TreeNode(3)
    
    value = 7
    current_node = TreeNode(5) -> current_node.right = TreeNode(7)
    
    value = 2
    current_node = TreeNode(5) -> _insert(2, TreeNode(3), current_node= TreeNode(3))
        그럼 다시 자기 자신을 호출 할때 2와 3을 비교. 
        current_node =TreeNode(3) -> TreeNode(3).left = TreeNode(2)
        left에 2 값이 생김
    
    value = 4
    current_node = TreeNode(3) -> TreeNode(3) = TreeNode(4)
    '''
    def _insert(self, value, current_node):
        if value < current_node.value: #value 와 treenode의 value 비교
            if not current_node.left: #left가 None값이면 True (left값이 있냐 없냐 따짐)
                current_node.left = TreeNode(value) #left 값이 없으면 아래 코드 실행
            else:
                self._insert(value, current_node.left)#자기 자신을 호출하는 함수. 그래서 처음으로 돌아감

        elif value > current_node.value:
            if not current_node.right:
                current_node.right = TreeNode(value)
            else:
                self._insert(value,current_node.right)
        else:
            print('이미 존재하는 값입니다.')

    def delete(self, value):
        if not self.root:
            return
        else:
            self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if not current_node:
            return current_node
        elif value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                min_node = self._find_min(current_node.right)
                current_node.value = min_node.value
                current_node.right = self._delete(min_node.value, current_node.right)

        return current_node

    def _find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

#실행 코드
bt = BinaryTree(5) #루트 노드 4인 이진트리 객체 생성

#값 삽입
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 이진 트리를 전위 순회한 결과 출력
print('전위 순회: ', bt.preorder_traversal(bt.root, ""))

# 이진 트리를 중위 순회한 결과 출력
print('중위 순회: ', bt.inorder_traversal(bt.root, ""))

# 이진 트리를 후위 순회한 결과 출력
print('후위 순회: ', bt.postorder_traversal(bt.root, ""))

# 값 검색
print('값 4가 트리에 존재하는가?', bt.search(4))
print('값 9가 트리에 존재하는가?', bt.search(9))

# 값 삭제
bt.delete(3)
print('값 3을 삭제한 후 주위 순회: ', bt.inorder_traversal(bt.root, ""))