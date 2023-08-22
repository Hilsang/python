def main():
    with open('text.txt', 'r') as f:
        context = f.readlines()
    print(context)

if __name__ == '__main__':
    main()

