class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()

super_list.append(5)
super_list.append(6)

print(super_list)
print(issubclass(SuperList, list))
