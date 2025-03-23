class AddMixin():
    #此类为添加东西的类
    def addliquid(self,liquid,nums,temp):
        #此方法用于加液体
        self.liquid=liquid
        self.volume=nums
        if temp=="cold":
            self.temperature="cold"
        elif temp=="hot":
            self.temperature="hot"
        return f"add {self.temperature} {self.liquid} {self.volume} ML"