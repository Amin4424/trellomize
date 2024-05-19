import json
import libs.view as view
import libs.get_input as input
from loguru import logger
from pathlib import Path
import uuid
class Program :
    @staticmethod
    def create_project():
        pass #TODO
    def remove_project():
        pass #TODO
    @staticmethod
    def user_logging_in(username):
        view.logging_in_message(username)
        logger.add('data/logging.log')
        logger.info(username+' just logged in into his/her account')
        Program.menu_after_logging()
    @staticmethod
    def menu_after_logging():
        view.menu_after_log()
        choicesad=input.get_string()