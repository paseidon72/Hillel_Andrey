class my_vars:
    def __init__(self, t):
        self._temp = t

    @property
    def temperature(self):
        return self._temp

    @temperature.setter
    def temperature(self, t):
        self._temp = t


c = my_vars(500)
print(c.temperature)        # 500

c.temperature = 1    
print(c.temperature)        # 1

#     def my_getter(self):
#         return self._temp
#
#     def my_setter(self, t):
#         if t > -273.15:
#             self._temp = t
#         else:
#             print('Below absolute 0!')
#
#
# v = my_vars(500)
# print(v.my_getter())  # 500
# v.my_setter(-1000)  # 'Below absolute 0!'
# v.my_setter(-270)
# print(v.my_getter())  # -270
