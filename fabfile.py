from fabric.api import local, lcd


def build():
    # local("jupyter nbconvert docs/**/*.ipynb --to markdown")
    local("copy README.md docs\index.md")
    local("mkdocs build")
    with lcd("..\East196.github.io"):
        local("rd /s /q cs224n")
    local("xcopy site ..\East196.github.io\cs224n\ /s /e")


def serve():
    local("mkdocs serve")


def download():
    url = 'http://web.stanford.edu/class/cs224n/lectures/'
    path = "D:\github\stanford-cs224n-winter-2017\lectures\\"
    try:
        os.makedirs(path)
    except OSError as why:
        print("failed: %s " % str(why))
    base = urllib.parse.urlparse(url)
    html_doc = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_doc, "lxml")
    a_list = soup.select("a")
    for a in a_list:
        href = a['href']
        if href.endswith('.ipynb') or href.endswith(".pdf"):
            if href.startswith("http://"):
                pass
            elif href.startswith("/"):
                href = "%s://%s%s" % (base.scheme, base.netloc, href)
            else:
                href = "%s://%s%s%s" % (base.scheme, base.netloc,
                                        base.path[:base.path.rfind("/") + 1], href)
            print(href)
            sub_base = urllib.parse.urlparse(href)
            sub_path = "%s%s" % (
                path, sub_base.path[sub_base.path.rfind("/"):])
            print(sub_path)
            urllib.request.urlretrieve(href, filename=sub_path)
