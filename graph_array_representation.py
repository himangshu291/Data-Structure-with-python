# class graph:
# def
# # def matrix(self):
#     row = int(input("Enter the number of rows:"))
#     column = int(input("Enter the number of columns:"))
class graph:
    def __init__(self,row,col):
        self.mat=[]
        self.row=row
        self.column=col
         
    def matrix(self):
        # print("Enter the entries row wise:")
        for i in range(self.row):
            a = []
            for j in range(self.column):
                a.append(0)
            self.mat.append(a)
        # print(self.mat)
    
    def adj_for_undirec(self):
        edg=int(input("Enter the number of edges:"))
        for i in range(edg):
            src=int(input("\nEnter the source:"))
            dest=int(input("Enter the destination:"))
            self.mat[src][dest]=1
            self.mat[dest][src]=1        

    def adj_for_direc(self):
        edg=int(input("Enter the number of edges:"))
        for i in range(edg):
            src=int(input("\nEnter the source:"))
            dest=int(input("Enter the destination:"))
            self.mat[src][dest]=1
            
    def undirec_degree(self):
        for i in range(self.row):
            deg=0
            for j in range(self.column):
                if self.mat[i][j]==1:
                    deg+=1
            print(f"\nDegree of {i}:",deg)
    
    def direc_degree(self):
        # indegree_lst=[]
        for i in range(len(self.mat)):
            print(len(self.mat))
            deg=0
            for j in range(len(self.mat)):
                print(len(self.mat))
                if self.mat[j][i]==1:
                    deg=deg+1
            # indegree_lst.append(k)
            print(f"Indegree of {i}:",deg)
        #  for i in range(self.row):
        #     deg=0
        #     for j in range(self.column):
        #         if self.mat[i][j]==1:
        #             deg+=1
        #     print(f"\nDegree of {i}:",deg)
    
    # For printing the matrix
    def display(self):
        print(len(self.mat))
        for i in range(self.row):
            for j in range(self.column):
                print(self.mat[i][j], end=" ")
            print()

ob=graph(int(input("Enter the no. of rows:")),int(input("Enter the no. of columns:")))
ob.matrix()
ob.display()
# ob.adj_for_undirec()
# ob.display()
# ob.undirec_degree()
ob.adj_for_direc()
ob.display()
ob.direc_degree()


