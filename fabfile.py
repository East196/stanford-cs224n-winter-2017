from fabric.api import local,lcd


def build():
    local("copy README.md docs\index.md")
    local("mkdocs build")
    with lcd("..\East196.github.io"):
        local("rd /s /q cs224n")
    local("xcopy site ..\East196.github.io\cs224n\ /s /e")


def serve():
    local("mkdocs serve")
