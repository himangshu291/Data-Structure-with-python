import single_linked_list
def reverse(self):
    c=None
    n=self.start
    if n==None:
        self.start=n
        return
    else:
        while n!= None:
            t=n.link
            n.link=c
            c=n
            n=t
        self.start=c

ob=single_linked_list.slinked
ob.reverse()
