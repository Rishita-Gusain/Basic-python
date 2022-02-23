class Luhn:
    
    def __init__(self, card_num):
        self.card_num=str(card_num).strip()
        self.card_num=str(card_num).replace(" ","")
    def valid(self):
        if len(self.card_num)<=1:
            return False

        try:
            new_num=[int(i) for i in self.card_num]
        except:
            return False

        for x in range(len(new_num)-2,-1,-2):
            new_value = new_num[x]*2
            if new_value>9:
                new_value-=9
            new_num[x]=new_value
        if sum(new_num)%10==0:
            return True
        else:
            return False

    

