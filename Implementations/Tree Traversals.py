


def InOrder(root):
    if root.left:
        InOrder(root.left)
    print(root.value,end=' ')
    if root.right:
        InOrder(root.right)

def PreOrder(root):
    print(root.value,end=' ')
    if root.left:
        PreOrder(root.left)
    if root.right:
        PreOrder(root.right)
        
def PostOrder(root):
    if root.left:
        PostOrder(root.left)        
    if root.right:
        PostOrder(root.right)   
    print(root.value,end=' ')
    