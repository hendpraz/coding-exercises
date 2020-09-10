def levelOrder(self,root):
    #Write your code here
    if(root==None):
        pass
    else:
        print(root.data, end=' ')
        end = False
        level = 0
        nodes = []
        nodes.append(root.left)
        nodes.append(root.right)
        while(not(end)):
            end = True
            for i in range(len(nodes)):
                if(nodes[i] != None):
                    end = False
                    print(nodes[i].data, end=' ')
            
            if(not end):
                newNodes = []
                for i in range(len(nodes)):
                    if(nodes[i] != None):
                        if(nodes[i].left != None):
                            newNodes.append(nodes[i].left)
                        if(nodes[i].right != None):
                            newNodes.append(nodes[i].right)
                nodes = newNodes

