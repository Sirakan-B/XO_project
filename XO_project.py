#функция для отображения
def display_custom(a, b, c):
    print(a)
    print(b)
    print(c)

#функция для отображения выбора
def choosen_position(number, mark):
    global positions
    index = positions.index(number)
    d_positions[index] = mark
    

d_positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
#функция для проверки победы
def win(sym, massive, show_result=False):
    
    if sym == 'X':
        player_tag = 'Player 1'
    else:
        player_tag = 'Player 2'

    if massive[:3] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[3:6] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[6:] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[::3] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[1::3] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[2::3] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[::4] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    elif massive[2:7:2] == [sym, sym, sym]:
        if show_result == True: print(f'Game is over, {player_tag} won!')
        return True
    else:
        return False


# Функция для проверки пользовательского ввода
def validation(mark=""):
    global taken_positions
    choice = "Default"
    choice_is_taken = False
    choice_is_valid = False

    while (choice.isdigit() == False) or (choice_is_taken == True) or (choice_is_valid == False):
        choice = input(f'Выберите позицию, в которую поставить {mark}: ')

        if (choice.isdigit() == True):
            try:
                input_result = int(choice)
            except ValueError:
                input_result=" "
            if input_result in valid_input:
                if input_result not in taken_positions:
                    taken_positions.append(input_result)
                    return input_result
                else:
                    choice_is_taken = True
                    index_of_taken_position = positions.index(input_result)
                    print(f'Выбранная позиция уже занята, там стоит {d_positions[index_of_taken_position]}')
            else:
                choice_is_valid = False
                print('Неверно задана позиция, для выбора позиции используйте цифры от 1 до 9. Ответ должен быть целым числом, без точек, запятых, пробелов и прочих спецсимволов')
        elif ("," in choice) or ("." in choice) or (" " in choice) or ("   "):
            print('Ответ должен быть целым числом, без точек, запятых и пробелов!')
        else:
            print('Неверно задана позиция, для выбора позиции используйте цифры от 1 до 9')

def tactic_x(mark1='X',mark2='O'):
    global d_positions,i, taken_positions,valid_input
    #Первый ход, занимаем центр
    if  d_positions[4] != mark1 and d_positions[4] != mark2: #первый ход Х ставится в центр
        d_positions[4]=mark1
        taken_positions.append(5)
    else: 
        #второй ход для Х
        if i==3:
            for n in corner_positions: #второй ход, ставим Х в любой свободный угол
                if n not in taken_positions:
                      taken_positions.append(n)
                      return choosen_position(n, mark1) 
        else:
            #третий ход, проверяем наличие победы
            
            for n in valid_input:
                
                if n not in taken_positions:
                    
                    next_move_prediction=d_positions[:] 
                    index = positions.index(n)
                    next_move_prediction[index] = mark1
                    if win(mark1,next_move_prediction,False)==True:
                        taken_positions.append(n)
                        return choosen_position(n,mark1)
                    else:
                        pass
                else:
                    pass
            #Проверяем наличие победы ноликов
            for n in valid_input:
                if n not in taken_positions:
                    next_move_prediction=d_positions[:] 
                    index = positions.index(n)
                    next_move_prediction[index] = mark2
                    if win(mark2,next_move_prediction,False)==True:
                        taken_positions.append(n)
                        return choosen_position(n,mark1)
                    else:
                        pass
                    
                else:
                    pass
        #третий ход, определяем угол, в который нужно поставить Х для победы
        for n in corner_positions:
            #ставим крестик в свободный угол
            if n not in taken_positions:
                next_move_prediction=d_positions[:] 
                index = positions.index(n)
                next_move_prediction[index] = mark1
                prediction_taken_positions=taken_positions[:]
                prediction_taken_positions.append(n)
                #ставим нолик, чтобы помешать крестику выиграть 
                for j in valid_input:
                    if j not in prediction_taken_positions:
                        index = positions.index(j)
                        next_move_prediction_2=next_move_prediction[:]
                        next_move_prediction_2[index] = mark1
                        if win(mark1,next_move_prediction_2,False)==True:
                            next_move_prediction[index] = mark2
                            prediction_taken_positions.append(j)
                            break
                        else:
                            pass
                
                #ставим крестик, чтобы выиграть 
                for b in valid_input:
                    if b not in prediction_taken_positions:
                        index = positions.index(b)
                        next_move_prediction_3=next_move_prediction[:]
                        next_move_prediction_3[index] = mark1
                        if win(mark1,next_move_prediction_3,False)==True:
                                taken_positions.append(n)
                                return choosen_position(n,mark1)
                        else:
                            pass    
        #если никакое из условий выше не выполнилось, ставим крестик в любую свободную клетку
        #второй ход для О
        for n in corner_positions:
            if n not in taken_positions:
                taken_positions.append(n)
                return choosen_position(n,mark1) 
        for n in valid_input:
            if n not in taken_positions:
               taken_positions.append(n)
               return choosen_position(n,mark1) 
            
            
                
            

print('Принцип работы доски: ниже представлены номера позиций,в которые можно поставить Х или О, для подстановки необходимо использовать цифры на клавиатуре (Num Pad)')
corner_positions=[7,9,1,3]

positions = [7, 8, 9, 4, 5, 6, 1, 2, 3]

display_custom(positions[:3], positions[3:6], positions[6:])
i = 0
taken_positions = []
valid_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]

side_choosen=False
side_is_valid = False
side=0
choice="Default"
while side_choosen==False:
    while (choice.isdigit() == False) or (side_is_valid == False):
        choice = input(f'Выберите сторону, чтобы играть за Х, нажмите 1. Чтобы играть за О, нажмите 2: ')
        if (choice.isdigit() == True):
            try:
                input_result = int(choice)
            except ValueError:
                input_result=" "
            
            if input_result==1:
                    side_is_valid=True
                    side_choosen=True
                    side=1
            elif input_result==2:
                    side_is_valid=True
                    side_choosen=True
                    side=2
            else:
                choice_is_valid = False
                print('Неверно задана позиция, для выбора позиции используйте цифры 1 или 2. Ответ должен быть целым числом, без точек, запятых, пробелов и прочих спецсимволов')
        elif ("," in choice) or ("." in choice) or (" " in choice) or ("   "):
            print('Ответ должен быть целым числом, без точек, запятых и пробелов!')
        else:
            print('Неверно задана позиция, для выбора позиции используйте цифры 1 или 2')    

#Цикл игрок играет за X, комп за O
if side==1:
    while (i < 9) and (win('X',d_positions, False) == False) and (win('O',d_positions, False) == False):
    
        i += 1
        choosen_position_x = validation('X')
        choosen_position(choosen_position_x, 'X')
        print(f'Текущее состояние доски, ходов сделано {i}')
        display_custom(d_positions[:3], d_positions[3:6], d_positions[6:])
    
        if (i != 9) and (win('X',d_positions) == False):
            i += 1
            tactic_x('O','X') #первый аргумент - наш символ, второй аргумент - символ противника
            print(f'Машина сделала выбор, ход {i}')
            display_custom(d_positions[:3], d_positions[3:6], d_positions[6:])
        else:
            pass
elif side==2:
    #Цикл игрок играет за O, комп за X
    while (i < 9) and (win('X',d_positions, False) == False) and (win('O',d_positions, False) == False):
    
        i += 1
        tactic_x('X','O') #первый аргумент - наш символ, второй аргумент - символ противника
       
        print(f'Машина сделала выбор, ход {i}')
        display_custom(d_positions[:3], d_positions[3:6], d_positions[6:])
        #choosen_position_x = validation('X')
        #choosen_position(choosen_position_x, 'X')
    
        if (i != 9) and (win('X',d_positions) == False):
            i += 1
            choosen_position_o = validation('O')
            choosen_position(choosen_position_o, 'O')
        else:
            pass
        print(f'Текущее состояние доски, ходов сделано {i}')
        display_custom(d_positions[:3], d_positions[3:6], d_positions[6:])




win('X',d_positions, True)
win('O',d_positions, True)
if win('X',d_positions) == False and win('O',d_positions) == False:
    print(f'Game is over, nobody won!')





