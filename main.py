from os import system, name, remove


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


fileName = ''  #faila nosaukuma definesana
text = ''  #teksts kas bus faila
temp = 'temp'  #mainigais lai varetu realizet faila saglabasanu/nesaglabasanu
while fileName != 'q':  #lai izietu no programmas
  st = 0
  result = 0
  text = ''  #mainigo atjauninasana
  clear()
  fileName = input("Write path/name of file you want to create/open, or 'q'- to exit program: ")
  while fileName == 'temp' or fileName == '':  #lai nebutu problemas ar faila saglabasanu/nesaglabasanu
    clear()
    if fileName == 'temp':
      print("You can't name file like that, because it is reserved by program")
    fileName = input("Write path/name of file you want to create/open, or 'q'- to exit program: ")
    fileName1 = fileName  #faila nosaukuma ievade
  if fileName == 'q':  #lai izietu no programmas
    break
  try:  #ja jus ievadat faila nosaukumu, bet sistemā nav faila ar tadu nosaukumu, tad programma izveido failu ar tadu nosaukumu
    f = open(fileName, 'r')  #faila atversana
    f.close()  #faila aizversana
    while result != 1:
      try:
        f = open(fileName, 'r')
        buf = f.read()  #lai varetu rediget failu
        print(buf, end='')  #lai redzetu faila tekstu
        f.close()
        f = open(temp, 'w')  #'temp' faila atversana lai varetu realizet faila saglabasanu/nesaglabasanu
        f.write(buf)
        f.close()
        result = 1
      except:
        fileName1 = input("Program can't open this file, write other's file name\path or 'q' to leave program: ")
        f = open(temp, 'w')
        f.close()

  except:  #ja jus ievadat faila nosaukumu, bet sistemā nav faila ar tadu nosaukumu, tad programma izveido failu ar tadu nosaukumu
    f = open(fileName, 'w')
    buf = ''
    f.close()
    st = 1
    f = open(temp, 'w')
    f.close()
  if fileName == 'q':  #lai izietu no programmas
    break
  while text != 'q':  #lai izietu no faila
    clear()
    print("'d' - to remove character\n'q' - to exit file\n")
    print('File:', fileName,'\n')  #lai lietotajs redzetu ar kuru failu vins strada
    #try:  #ja tas nav pirma failu atversana un 'temp' fails jau eksiste, tad fails atveras uz 'read'
    f = open(temp, 'r')
    buf = f.read()
    print(buf, end='')
    f.close()
    f = open(temp, 'w')
    f.write(buf)
    f.close()
    text = input()
    if text == 'q':
      f.close()
      while True:
        saveFile = input("Would you like to save file 'y'/'n': " )  # faila saglabasana
        if saveFile == 'y' or saveFile == 'n':
          break
      if saveFile == 'y':
        f = open(fileName, 'w')
        f.write(buf)
        f.close()
        remove(temp)
      elif saveFile == 'n' and st == 1:
        remove(temp)
        remove(fileName)
      elif saveFile == 'n' and st == 0:
        remove(temp)
    elif text == 'd':
      f = open(temp, 'w')
      buf = buf[:-1]
      f.write(buf)
      clear()
      f.close()
    else:
      f = open(temp, 'a')
      f.write(text + '\n')
      f.close()
