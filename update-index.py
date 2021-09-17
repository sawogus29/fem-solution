def main():
    print("enter main")
    with open("index.html", mode="w") as fp:
        fp.write("<html><body><p>Hello Github Action</p><body></html")
        print("writing file")
    print("exit main")
    
if __name__ == "__main__":
    main()
    
