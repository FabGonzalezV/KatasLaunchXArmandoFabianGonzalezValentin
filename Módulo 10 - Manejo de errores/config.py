#def main():
 #   try:
   #     configuration = open('config.txt')
  #  except FileNotFoundError:
    #    print("Couldn't find the config.txt file!")




#actualizamos función main
#def main():
#    try:
#        configuration = open('config.txt')

#    except Exception:
#        print("Couldn't find the config.txt file!")    

#if __name__ == '__main__':
#    main()


#volvemos a actualizar main
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")    
#if __name__ == '__main__':
#    main()        

#se actualiza de nuevo el amin para visualizar los errores
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")
#    except IsADirectoryError:
#        print("Found config.txt but it is a directory, couldn't read it")
#    except (BlockingIOError, TimeoutError):
#        print("Filesystem under heavy load, can't complete reading configuration file")
#if __name__ == '__main__':
#    main()        


