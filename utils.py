import yaml
import logging


def get_api_info():
    with open("configuration.yaml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            api_id = config['api_id']
            api_hash = config['api_hash']
            return api_id, api_hash
        except yaml.YAMLError as exc:
            print(exc)


def get_logger(class_name, logger_level):
    # create logger
    logger = logging.getLogger(class_name)
    # create console handler
    ch = logging.StreamHandler()
    if (logger_level == "INFO"):
        logger.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    elif (logger_level == "DEBUG"):
        logger.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    elif (logger_level == "WARN"):
        logger.setLevel(logging.WARNING)
        ch.setLevel(logging.WARNING)
    else:
        print(f"Unable to set logger level {logger_level}")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    return logger
