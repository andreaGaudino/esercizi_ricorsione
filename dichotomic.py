def dichotomic(input_list, val):

    if len(input_list)==1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        i = len(input_list) // 2
        return dichotomic(input_list[:i], val) or dichotomic(input_list[i:], val)

if __name__ == '__main__':
    sequenza = [3,5,1,7,8,9,12,3,4,9,7,5]
    valore = 5
    print(dichotomic(sequenza, valore))
    print(dichotomic(sequenza, 10))