def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
#inner_function() # NameError: name 'inner_function' is not defined,
# ошибка, программа не видит эту функцию,потому что она
# находится в другом пространстве имен(внутри объемлющей область видимости)
test_function()