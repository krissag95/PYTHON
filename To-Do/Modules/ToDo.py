import time
class Agenda:
    def __init__(self, id_num, name):
        self.__id_num = id_num
        self.__name = name
        self.__entries = []
        self.__date = time.strftime("%d/%m/%Y")
        self.__time = time.strftime("%H:%M")

    def __str__(self):
        return ("({0}, {1}, {2}, {3}, {4})".format(self.__id_num, self.__name, self.__entries, self.__date, self.__time))
    
    def new_entry(self, entry):
        self.__entries.append(entry)
    
    def get_agenda(self):
        #print(' '.join(i for i in self.__entries))
        print((('='*35)+'''\nID {0} - '{1}' - {2}''').format(self.__id_num, self.__name, self.__date))
        count = 1
        for i in self.__entries:
            print(str(count)+' - '+ i)
            count += 1

    def check(self, index):
        if(index > len(self.__entries)):
            print('That entry doesn\'t exist')
            return -1
        self.index = index - 1
        to_change = self.__entries[self.index]
        to_change = to_change[:0] + '* ' + to_change[0:]
        self.__entries[self.index] = to_change 

    def delete(self, index):
        if(index > len(self.__entries)):
            print('That entry doesn\'t exist')
            return -1
        self.index = index - 1
        del self.__entries[self.index]
'''
agenda = Agenda(9,'Por hacer')
agenda.new_entry("Estudiar")
agenda.new_entry("Comer")
agenda.new_entry("Lavar platos")
agenda.new_entry("Jugar TESO")
agenda.new_entry("Regar las plantas")
agenda.new_entry("Barrer la casa")

#agenda.check(1)
agenda.delete(1)
print(str(agenda))
agenda.get_agenda()
'''