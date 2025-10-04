from multiprocessing import Value, Array, Manager

counter = Value('i', 0)      # 'i' = integer
data = Array('d', [0.0, 1.0, 2.0])


with Manager() as manager:
    list_one = manager.list()
    dict_one = manager.dict()
    

