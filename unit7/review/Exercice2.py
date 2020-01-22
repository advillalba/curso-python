import logging
import os
import shutil

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def _init_test_folders_():
    if os.path.isdir('Exercice2Folder'):
        logger.info('Borrando directorio.')
        shutil.rmtree('Exercice2Folder')

    logger.info('Generando estructura de carpetas y ficheros.')

    os.mkdir("Exercice2Folder")
    open("Exercice2Folder/root.txt", "w").close()

    os.mkdir("Exercice2Folder/subfolder1")
    open("Exercice2Folder/subfolder1/a.txt", "w").close()
    open("Exercice2Folder/subfolder1/b.txt", "w").close()
    open("Exercice2Folder/subfolder1/c.csv", "w").close()

    os.mkdir("Exercice2Folder/subfolder2")
    open("Exercice2Folder/subfolder2/d.csv", "w").close()
    os.mkdir("Exercice2Folder/subfolder2/subfolder2-2")
    open("Exercice2Folder/subfolder2/subfolder2-2/e.csv", "w").close()

    os.mkdir("Exercice2Folder/subfolder3")
    open("Exercice2Folder/subfolder3/f.json", "w").close()


def aplanar_directorio(ruta: str):
    logger.info(ruta)
    root_folder = ruta
    _move_files_(ruta, root_folder)


def _move_files_(ruta: str, root_folder: str):
    for file in os.listdir(ruta):
        file = os.path.join(ruta, file)
        logger.info(file)
        if os.path.isdir(file):
            _move_files_(file, root_folder)
            os.rmdir(file)
        else:
            if ruta != root_folder:
                shutil.move(file, root_folder)


_init_test_folders_()
aplanar_directorio('Exercice2Folder')
