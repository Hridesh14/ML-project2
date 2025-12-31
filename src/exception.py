import sys 
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message = f'Error occured in python [{0}] in line number [{1}] errror mesage is [{2}]'.format(
        file_name,exe_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    def str(self):
         return self.error_message


