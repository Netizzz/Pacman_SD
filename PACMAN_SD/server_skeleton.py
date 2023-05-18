import socket
import logging
import json
from game_mech import GameMech
import constant

# Está no lado do servidor: Skeleton to user interface (permite ter informação
# de como comunicar com o cliente)
class SkeletonServer:

    def __init__(self, gm: GameMech):
        self.gm = gm
        self.s = socket.socket()
        self.s.bind((constant.SERVER_ADDRESS, constant.PORT))
        self.s.listen()

    def process_x_max(self, s_c):
        x = self.gm.x_max
        s_c.send(x.to_bytes(constant.N_BYTES, byteorder="big", signed=True))

    def process_y_max(self, s_c):
        y = self.gm.y_max
        s_c.send(y.to_bytes(constant.N_BYTES, byteorder="big", signed=True))

    def process_add_player(self, s_c):
        data_rcv: bytes = s_c.recv(constant.MESSAGE_SIZE)
        name = data_rcv.decode(constant.COD_STR)
        number = self.gm.add_player(name, 1, 1)
        s_c.send(number.to_bytes(constant.N_BYTES, byteorder="big", signed=True))

    def process_get_obst(self, s_c):
        ob = self.gm.get_obstacles()
        msg = json.dumps(ob)
        dim = len(msg)
        s_c.send(dim.to_bytes(constant.N_BYTES, byteorder="big", signed=True))
        s_c.send(msg.encode(constant.COD_STR))

    def process_get_nr_obst(self, s_c):
        nr_ob = self.gm.get_nr_obstacles()
        s_c.send(nr_ob.to_bytes(constant.N_BYTES, byteorder="big", signed=True))

    def process_get_players(self, s_c):
        pl = self.gm.get_players()
        msg = json.dumps(pl)
        dim = len(msg)
        s_c.send(dim.to_bytes(constant.N_BYTES, byteorder="big", signed=True))
        s_c.send(msg.encode(constant.COD_STR))

    def process_get_nr_players(self, s_c):
        nr_pl = self.gm.get_nr_players()
        s_c.send(nr_pl.to_bytes(constant.N_BYTES, byteorder="big", signed=True))

    def process_player_mov(self, s_c):
        data: bytes = s_c.recv(constant.N_BYTES)
        mov = int.from_bytes(data, byteorder='big', signed=True)
        data: bytes = s_c.recv(constant.N_BYTES)
        nr_player = int.from_bytes(data, byteorder='big', signed=True)
        pos = self.gm.execute(mov, "player", nr_player)
        msg = json.dumps(pos)
        dim = len(msg)
        s_c.send(dim.to_bytes(constant.N_BYTES, byteorder="big", signed=True))
        s_c.send(msg.encode(constant.COD_STR))

    def run(self):
        logging.info("a escutar no porto " + str(constant.PORT))
        socket_client, address = self.s.accept()

        logging.info("o cliente com endereço " + str(address) + " ligou-se!")

        dados: str = ""
        fim = False
        while fim == False:
            data_recv: bytes = socket_client.recv(constant.MESSAGE_SIZE)
            msg = data_recv.decode(constant.COD_STR)
            logging.debug("o cliente enviou: \"" + dados + "\"")

            if msg == constant.X_MAX:
                self.process_x_max(socket_client)
            elif msg == constant.Y_MAX:
                self.process_y_max(socket_client)
            elif msg == constant.ADD_PLAYER:
                self.process_add_player(socket_client)
            elif msg == constant.GET_PLAYERS:
                self.process_get_players(socket_client)
            elif msg == constant.NR_PLAYERS:
                self.process_get_nr_players(socket_client)
            elif msg == constant.GET_OBST:
                self.process_get_obst(socket_client)
            elif msg == constant.NR_OBST:
                self.process_get_nr_obst(socket_client)
            elif msg == constant.PLAYER_MOV:
                self.process_player_mov(socket_client)
            elif msg != constant.END:
                fim = True

        socket_client.close()
        logging.info("o cliente com endereço o " + str(address) + " desligou-se!")

        self.s.close()


logging.basicConfig(filename=constant.LOG_FILE,
                    level=constant.LOG_LEVEL,
                    format='%(asctime)s (%(levelname)s): %(message)s')

"""    def processa_soma(self, s_c):
        dados_recebidos: bytes = s_c.recv(constante.N_BYTES)
        # Receber dois inteiros do cliente!

        value1 = int.from_bytes(dados_recebidos, byteorder='big', signed=True)
        logging.debug("o cliente enviou: \"" + str(value1) + "\"")

        dados_recebidos: bytes = s_c.recv(constante.N_BYTES)
        value2 = int.from_bytes(dados_recebidos, byteorder='big', signed=True)
        logging.debug("o cliente enviou: \"" + str(value2) + "\"")
        # Processa a soma
        soma = self.add_obj.add(value1, value2)
        # Devolver ao cliente o resultado da soma
        s_c.send(soma.to_bytes(constante.N_BYTES, byteorder="big", signed=True))
        # AJUDAS
        # -- int.from_bytes(dados_recebidos, byteorder='big', signed=True)
        # -- to_bytes(constante.N_BYTES, byteorder="big", signed=True)

    def run(self):
        logging.info("a escutar no porto " + str(constante.PORTO))
        socket_client, endereco = self.s.accept()

        logging.info("o cliente com endereço " + str(endereco) + " ligou-se!")

        dados: str = ""
        fim = False
        while fim == False:
            dados_recebidos: bytes = socket_client.recv(constante.TAMANHO_MENSAGEM)
            dados = dados_recebidos.decode(constante.CODIFICACAO_STR)
            logging.debug("o cliente enviou: \"" + dados + "\"")

            if dados == constante.SOMA:
                self.processa_soma(socket_client)
            elif dados == constante.FIM:
                fim = True\
#            if dados != constante.FIM:
#                dados = self.eco_obj.eco(dados)
#                socket_client.send(dados.encode(constante.CODIFICACAO_STR))

        socket_client.close()
        logging.info("o cliente com endereço o " + str(endereco) + " desligou-se!")

        self.s.close()


logging.basicConfig(filename=constante.NOME_FICHEIRO_LOG,
                    level=constante.NIVEL_LOG,
                    format='%(asctime)s (%(levelname)s): %(message)s')
"""