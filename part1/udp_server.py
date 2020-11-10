import socket
import logging


logger = logging.getLogger('udp_server')
hdlr = logging.FileHandler('udp_server.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

logger.info("Starting UDP server set up")
UDP_IP = ''
UDP_PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))
logger.info("Socket created & binded")

while True:
    # receive from client
    data_byte, addr = s.recvfrom(1024)
    data = data_byte.decode()
    logger.info('Received Req Msg: %s', data)
    logger.info('Received Req Msg length: %s', len(data))

    # send back to the client
    if data == ('studentmarklist' + '\0') and len(data) is 16:
        response_msg = '0003' + 'George\0\0\0\0\0\0\0\0\0\0' + '0095' + 'Mikeeeeeeeeeeee\0' + '0100' + 'Kelly\0\0\0\0\0\0\0\0\0\0\0' + '0000' + 'Zong\0\0\0\0\0\0\0\0\0\0\0\0' + '0087'
        sent = s.sendto(response_msg.encode(), addr)
        logger.info('Sent Res Msg: %s', response_msg)
    else:
        logger.info("Request Msg not in required format!!")
