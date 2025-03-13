import json
import logging as logmodule
import logging.config
import os
from jsonschema import validate

FORMAT ='%(asctime)s %(module)s %(levelname)s: %(message)s'
DATEFMT =  '%m/%d/%Y %I:%M:%S %p'

SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "JSON schema for Python logging.config.dictConfig",
    "type": "object",
    "required": ["version"],
    "properties": {
        "version": {"type": "integer", "enum": [1]},
        "formatters": {
            "type": "object",
            "patternProperties": {
                "^[a-zA-Z0-9._-]+$": {
                    "type": "object",
                    "properties": {
                        "format": {"type": "string"},
                        "datefmt": {"type": "string"}
                    },
                    "additionalProperties": False
                }
            }
        },

        "filters": {
            "type": "object",
            "patternProperties": {
                "^[a-zA-Z0-9._-]+$": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"}
                    },
                    "additionalProperties": False
                }
            }
        },

        "handlers": {
            "type": "object",
            "patternProperties": {
                "^[a-zA-Z0-9._-]+$": {
                    "type": "object",
                    "required": ["class"],
                    "properties": {
                        "class": {"type": "string"},
                        "level": {"type": "string"},
                        "formatter": {"type": "string"},
                        "filters": {
                            "type": "array",
                            "items": {"type": "string"},
                            "uniqueItems": True
                        }
                    }
                }
            }
        },

        "loggers": {
            "type": "object",
            "patternProperties": {
                "^[a-zA-Z0-9._-]+$": {
                    "type": "object",
                    "properties": {
                        "level": {"type": "string"},
                        "propagate": {"type": "boolean"},
                        "filters": {
                            "type": "array",
                            "items": {"type": "string"},
                            "uniqueItems": True
                        },
                        "handlers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "uniqueItems": True
                        }
                    }
                }
            }
        },

        "root": {
            "type": "object",
            "properties": {
                "level": {
                    "type": "string",
                    "enum": ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
                },
                "filters": {
                    "type": "array",
                    "items": {"type": "string"},
                    "uniqueItems": True
                },
                "handlers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "uniqueItems": True
                }
            }
        },

        "incremental": {"type": "boolean"},
        "disable_existing_loggers": {"type": "boolean"}
    }
}



class Logger:

    @staticmethod
    async def console():
        """
        Creates normal console logging
        """
        logFormatter = logging.Formatter(FORMAT)
        rootLogger = logging.getLogger()
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)
        return rootLogger
    
    @staticmethod
    def initialize(filename: str):
        """
        Loads the python logging configuration a json file that
        should be compliant with Python Log Json config
        :param filename: The path to the config .json file for logging
        :return:
        """
        if not os.path.exists(filename):
            raise Exception("Configuration file cannot be found: {0}".format(filename))
        config_dict = None
        with open(filename) as f:
            config_dict = json.load(f)
        validate(instance=config_dict, schema=SCHEMA)
        logging.config.dictConfig(config_dict)
        return logmodule

    @staticmethod
    async def validate(source: dict):
        """
        Reads a source dictionary logging configuration
        json and validates against the standard Python
        Json Logging configuration
        :param source: The source dictionary to be analyzed
        :return:
        """

        # Validating logging
        validate(instance=source, schema=SCHEMA)
