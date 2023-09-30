
#-------------------------ЗАДАЧА-----------------------------#
# Перевод Из мм в м, из м в км (и наоборот)

l = 100 #добавьте проверку на >=0

start = 'm' #  из которого делается перевод
end = 'km' #  в который делается перевод
match start:
    case 'm':
        match end:
            case 'mm':
                pass
            case 'km':
                print(l*1000)
            case _:
                pass
    case 'mm':
        pass
    case 'km':
        pass
    case _:
        pass

