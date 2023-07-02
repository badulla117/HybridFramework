import logging

class Logs():
    @staticmethod
    def getLogs():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler(".\\Logs\\MyLogFile.log", mode="w")
        formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger