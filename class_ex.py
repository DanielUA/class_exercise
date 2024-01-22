# class PySolution:
#     def int_to_roman(self, num: int) -> str:
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ""
#         i = 0
#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i +=1 
#         return roman_num
# print(PySolution().int_to_roman(1))
# print(PySolution().int_to_roman(4000))

# class PySolution:
#     def int_to_roman(self, r_num):
#         lookup = [
#             (1000, 'M'),
#             (900, 'CM'),
#             (500, 'D'),
#             (400, 'CD'),
#             (100, 'C'),
#             (90, 'XC'),
#             (50, 'L'),
#             (40, 'XL'),
#             (10, 'X'),
#             (9, 'IX'),
#             (5, 'V'),
#             (4, 'IV'),
#             (1, 'I'),
#         ]
#         resul = ''
#         for (num,roman) in lookup:
#             """ использование функции divmod, которая возвращает 
#             частное и остаток от деления r_num на num. Переменные 
#             d и r_num присваиваются соответственно частному и остатку"""
#             (d, r_num) = divmod(r_num, num)
#             resul += roman * d
#         return resul

# print(PySolution().int_to_roman(1))
# print(PySolution().int_to_roman(500))
# print(PySolution().int_to_roman(755))
# print(PySolution().int_to_roman(1200))
# print(PySolution().int_to_roman(3456))

# class PySolution:
#     def roman_to_int(self, rom_n: str) -> int:
#         rom_val = {
#               'I': 1, 
#               'V': 5, 
#               'X': 10, 
#               'L': 50, 
#               'C': 100, 
#               'D': 500, 
#               'M': 1000
#               }
#         result = 0
#         for el in range(len(rom_n)):
#             """Эта проверка осуществляется для определения, является 
#             ли текущая римская цифра больше предыдущей. Если это так, 
#             то это значит, что мы сталкиваемся с одним из "вычитаемых" 
#             случаев"""
#             if el > 0 and rom_val[rom_n[el]] > rom_val[rom_n[el-1]]:
#                 """Если текущая цифра больше предыдущей, то мы вычитаем 
#                 дважды значение предыдущей цифры (так как она уже была 
#                 добавлена в предыдущем шаге), чтобы скорректировать 
#                 результат."""
#                 result += rom_val[rom_n[el]] - 2 * rom_val[rom_n[el-1]]
#             else:
#                 """Если текущая цифра не больше предыдущей, то просто 
#                 добавляем значение текущей цифры к результату"""
#                 result += rom_val[rom_n[el]]
#         return result
# print(PySolution().roman_to_int('MMMCMLXXXVI'))
# print(PySolution().roman_to_int('MMMM'))
# print(PySolution().roman_to_int('C'))

# class PySolution:
#     def is_valid_parenthese(self, s):
#         stack = []
#         pchar = {"(": ")", "{": "}", "[": "]"}
        
#         for char in s:
#             if char in pchar:
#                 stack.append(char)
#             elif not stack or pchar[stack.pop()] != char:
#                 return False
                
#         return not stack
    
# print(PySolution().is_valid_parenthese("(){}[]"))
# print(PySolution().is_valid_parenthese("()[{)}"))
# print(PySolution().is_valid_parenthese("()"))

# class PySolution:
#     def sub_sets(self, sset, current=[]):
#         if not sset:
#             return [current]
#         return self.sub_sets(sset[1:], current) + \
#             self.sub_sets(sset[1:], current + [sset[0]]) 

# print(PySolution().sub_sets([4,5,6]))

# class py_solution:
#     def twoSum(self, nums, target):
#         lookup = {}
#         for i, num in enumerate(nums):           
#             if target - num in lookup:
#                 res = (lookup[target-num], i)
#                 # print(res)
#                 return res
#             lookup[num] = i

# print("index1=%d, index2=%d" % py_solution().twoSum([10,20,10,40,50,60,70],50))

# class PySolution:
#     def reverse_words(self, s):
#         return " ".join(reversed(s.split()))

# print(PySolution().reverse_words('hello .py'))

# class PySolution:
#     def three_sum(self, nums):
#         nums.sort()
#         result = []
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue

#             left, right = i+1, len(nums)-1

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]

#                 if total < 0:
#                     left += 1
#                 elif total > 0:
#                     right -= 1
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     right -= 1

#                     while left < right and nums[left] == nums[right - 1]:
#                         left += 1
#                     while right < left and nums[right] == nums[right + 1]:
#                         right -= 1

#         return result               

        
# print(PySolution().three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))

# class IOSting:
#     def __init__(self):
#         self.str = ""

#     def get_str(self):
#         self.user_str = str(input("enter your string: "))
    
#     def print_string(self):
#         print(self.user_str.upper())

# str1 = IOSting()

# str1.get_str()
# str1.print_string()

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
    
#     def area(self):
#         return self.width * self.length
 
# new_room = Rectangle(10,10)
# print(new_room.area())

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return self.radius ** 2 * 3.14
    
#     def perimetr(self):
#         return 2 * self.radius * 3.14

# my_circle = Circle(8)
# print(my_circle.area())
# print(my_circle.perimetr())
# print(type(my_circle).__name__)

# class Employee:
#     def __init__(self, emp_name, emp_id, emp_salary, emp_department):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary
#         self.emp_department = emp_department
    
#     def calculate_emp_salary(self, emp_salary, hours_worked):
#         overtime = 0
#         if hours_worked > 50:
#             overtime = hours_worked - 50
#         self.emp_salary = emp_salary + (overtime * (emp_salary / 50))
        
#     def emp_assign_department(self, new_emp_departament):
#         self.emp_department = new_emp_departament

#     def print_employee_details(self):
#         print(f"Name: {self.emp_name} \n id: {self.emp_id}, \
#                \n salary: {self.emp_salary}, \
#                  \n departament:  {self.emp_department}")
        
# employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
# employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
# employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
# employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

# print("Original Employee Details:")
# employee1.print_employee_details()
# employee2.print_employee_details()
# employee3.print_employee_details()
# employee4.print_employee_details()
# employee1.emp_assign_department("OPERATIONS")
# employee4.emp_assign_department("SALES")

# employee2.calculate_emp_salary(45000, 52)
# employee4.calculate_emp_salary(45000, 60)

# print("Updated Employee Details:")
# employee1.print_employee_details()
# employee2.print_employee_details()
# employee3.print_employee_details()
employee4.print_employee_details()
