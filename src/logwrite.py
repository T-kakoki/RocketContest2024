import logging
import logging.config

class MyLogging():
    def __init__(self):
        with open('../config/logconfig.ini','r',encoding='utf-8') as f:
            logging.config.fileConfig(f)
        self.logger = logging.getLogger('root')

    def write(self,logmessage,loglevel):
        if loglevel=="DEBUG":
            self.logger.debug(f"{logmessage}")
        elif loglevel=="INFO":
            self.logger.info(f"{logmessage}")
        elif loglevel=="WARNING":
            self.logger.warning(f"{logmessage}")
        elif loglevel=="ERROR":
            self.logger.error(f"{logmessage}")
        elif loglevel=="CRITICAL":
            self.logger.critical(f"{logmessage}")

def main():
    log = MyLogging()
    log.write("k-5","ERROR")

if __name__ == "__main__":
    main()