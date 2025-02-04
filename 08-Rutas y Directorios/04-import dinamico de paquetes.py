# Es buena idea cuando los proyect0s empiezan a crecer
# Sobre todo si tenemos que redactar pruebas a estos
paths = [p for p in path.iterdir() if not p.is_dir()]  #


def load(p):
    print(str(p))


list(map(load, paths))
