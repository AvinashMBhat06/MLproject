import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error is there in python script namely{file_name} in line number{exc_tb.tb_lineno} error message {str(error)}"
    return error_message

class custom_exception(Exception):
    def __init__(self,error_message,error_detail):
        self.error_message=error_message_detail(error_message,error_detail)
    def __str__(self) -> str:
        return self.error_message

    