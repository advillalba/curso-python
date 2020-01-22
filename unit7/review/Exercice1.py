import logging
import os
import shutil

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def _remove_file_(file, extensiones) -> bool:
    name, ext = os.path.splitext(file)
    deleted = False
    if extensiones is None or ext[1::] in extensiones:
        os.remove(file)
        deleted = True

    return deleted


def eliminar_ficheros(ruta: str, extensiones: [str] = None):
    files = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]
    removed_files = 0
    for file in files:
        remove = _remove_file_(os.path.join(ruta, file), extensiones)
        if remove:
            removed_files += 1

    logger.info('Se han borrado %s ficheros de la ruta: %s', removed_files, ruta)

    if len(files) == removed_files:
        logger.info('El directorio %s esta vacio, se borra', ruta)
        os.rmdir(ruta)


def _init_test_folders_():
    logger.info('Generando estructura de carpetas y ficheros.')
    if os.path.isdir('Exercice1Folder'):
        logger.info('Borrando directorio.')
        shutil.rmtree('Exercice1Folder')


    os.mkdir("Exercice1Folder")
    os.mkdir("Exercice1Folder/subfolder")
    open("Exercice1Folder/a.txt", "w").close()
    open("Exercice1Folder/b.txt", "w").close()
    open("Exercice1Folder/c.csv", "w").close()
    open("Exercice1Folder/subfolder/file.json", "w").close()


_init_test_folders_()
eliminar_ficheros('Exercice1Folder/subfolder', ['json', 'exe'])
eliminar_ficheros('Exercice1Folder', ['txt'])
