import requests


def check() -> None:
    """ проходит по списку проектов в файле и записывает недоступные проекты в лог-файл """
    
    with open('projects.txt', 'r') as fp:
        with open('log.txt', 'w') as log:
            for line in fp:
                try:
                    response = requests.get(line)
                    
                    if response.status_code != 200:
                        log.write(line)
                        log.write(str(response.status_code))
                except Exception as e:
                    log.write(line)


if __name__ == '__main__':
    check()
