class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    
        print(location,house_type,deal_type,price,completion_year)
    
    
    # 매물 정보 표시
    
gangnam=House("강남","아파트","매매","10억","2010년")






