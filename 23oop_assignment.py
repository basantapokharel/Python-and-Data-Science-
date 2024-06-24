# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         return self.length*self.breadth
    
#     def perimeter(self):
#         return 2*(self.length+self.breadth)
    
    

# rect1=Rectangle(10,20)
# print(rect1.area())
# print(rect1.perimeter())

# class waterUnits:
#     def __init__(self,heights):
#         self.heights=heights

#     def find_water_units(self):
#         max_water=0
#         left=-1
#         right=-1
#         for i in range(len(self.heights)):
#             for j in range(i+1,len(self.heights)):
#                 length=j-i
#                 height=min(self.heights[i],self.heights[j])
#                 water=length*height
#                 if water > max_water:
#                     left=i
#                     right=j
#                     max_water=water
#         return max_water,left,right




# heights=[1,8,6,2,5,4,8,3,7]

# wu=waterUnits(heights)
# print(wu.find_water_units())




class Shape:
    def area(self,a,b=-1):
        if (b==-1):
            return 3.14*a*a
        else:
            return a*b


    def perimeter(self,a,b=-1):
        if (b==-1):
            return 2*3.14*a
        else:
            return 2*(a+b)
        

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length  
        self.breadth=breadth

    def area(self):
        return(super().area(self.length,self.breadth))
    
    def perimeter(self):
        return(super().perimeter(self.length,self.breadth))
    

    



class circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return(super().area(self.radius))
    
    def perimeter(self):
        return(super().perimeter(self.radius))



r=Rectangle(10,20)
print(r.area())
print(r.perimeter())

c=circle(10)
print(c.area())
print(c.perimeter())