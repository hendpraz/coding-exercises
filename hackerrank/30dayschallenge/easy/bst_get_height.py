def getHeight(self,root):
    #Write your code here
    if(root == None) or ((root.left==None) and (root.right == None)):
        return 0
    else:
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))