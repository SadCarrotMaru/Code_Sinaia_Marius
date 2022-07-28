def count_code(str):
    poz = 0
    count = 0
    poz = str.find("co",poz)
    while poz >= 0:
        poz2 = str.find("e",poz+1)
        if poz2 == poz+3: count = count + 1
        poz = str.find("co",poz+1)
    return count

print(count_code('cozexxcope'))


