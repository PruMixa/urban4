def introspection_info(obj):
  info = {}
  info['type'] = type(obj).__name__
  info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]
  info['methods'] = [method for method in dir(obj) if method.startswith('__')]
  info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'None'

  return info

#Пример
class MyCustomClass:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print(f"Hello, my name is {self.name}")

my_object = MyCustomClass("Alice", 30)

number_info = introspection_info(42)
print(f"Информация о числе: {number_info}")

custom_info = introspection_info(my_object)
print(f"Информация о custom объекте: {custom_info}")