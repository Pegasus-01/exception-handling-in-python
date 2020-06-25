def main():
   try:
       myfile = open("file.txt" , 'r')
       print("success in reading")
   except IOError:
       print("file does not exist")



if __name__ == '__main__':
    main()