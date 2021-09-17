from os import listdir
from os.path import isdir

def read_template():
    with open("index-template.html", mode="r") as fp:
        t = ''.join(fp.readlines())
    return t

def construct_body(dirs, domain="sawogus29.github.io", path="fem-solution"):
    def build_link(x):
        href = f'{domain}/{path}/{x}'
        return f'<a href="{href}">{x}</a>'
    
    return "\n".join(map(build_link, dirs))
        

def main():
    print("enter main")
    print("reading directories")
    dirs = filter(lambda x: isdir(x) and not x.startswith('.'), listdir())
    body = construct_body(dirs)

    print("reading template")
    template = read_template()
    html = template.replace("$body$", body)
    
    with open("index.html", mode="w") as fp:
        #fp.write("<html><body><p>Hello Github Action</p><body></html")
        fp.write(html)
        print("writing file")
    print("exit main")
    
if __name__ == "__main__":
    main()
    
