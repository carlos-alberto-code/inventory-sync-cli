from domain.service.SenderServicePort import SenderServicePort


class WhatsappSenderServiceAdapter(SenderServicePort):

    def send(self):
        ...