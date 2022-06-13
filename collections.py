class Test_collections:
    
    list = [1, 2, 3, 4, 5]
    
    def list_printer(self):
        for i in range(0, len(self.list)):
            print(self.list[i])


            
test1 = Test_collections()
test1.list_printer()
