def main():
    name = input('name: ')
    string = input('string: ')
    f = open('levels/'+name+'.txt', 'w+')
    f.write(string)
    print('The file ' + name + '.txt has been created with the contents of:\n' + string)
    f.close()
    main()
main()
