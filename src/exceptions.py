import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"\nError_File->{file_name} \nERROR_Line->{exc_tb.tb_lineno} \nERROR->{str(error)}"
    return error_message

class custom_exception(Exception):
    def __init__(self,error_message,error_detail):
        self.error_message=error_message_detail(error_message,error_detail)
    def __str__(self) -> str:
        return self.error_message
    

    