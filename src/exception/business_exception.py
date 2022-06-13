class BusinessException(Exception):

    def __init__(self, template_msg: str, *args: any):
        super(BusinessException, self).__init__(
            template_msg.format(*args) if len(args) > 0 else template_msg
        )
