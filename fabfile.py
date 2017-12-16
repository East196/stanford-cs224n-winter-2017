from fabric.api import local


def build():
    local("mkdocs build")
    local("xcopy site ..\East196.github.io\cs224n\ /s /e")


def serve():
    local("mkdocs serve")
