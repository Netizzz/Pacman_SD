import socket
import constant
import json
from typing import Union


class StubClient:

    def __init__(self):
        self.s: socket = socket.socket()
        self.s.connect((constant.SERVER_ADDRESS, constant.PORT))

    def get_obstacles(self) -> dict:
        """
        Protocolo:
        -- Envia tipo de msg 'get obst'
        -- Recebe dimensão do objeto dicionário
        -- Recebe objeto dicionário com todos os obstaculos
        :return:
        """
        msg = constant.GET_OBST
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        dim = int.from_bytes(data, byteorder='big', signed=True)
        rec: bytes = self.s.recv(dim)
        obst = json.loads(rec)
        return obst

    def get_nr_obstacles(self):
        msg = constant.NR_OBST
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        nr = int.from_bytes(data, byteorder='big', signed=True)
        return nr

    def get_players(self) -> dict:
        """
        Protocolo:
        -- Envia type de msg 'get players'
        -- Receber dimensão do objeto dicionário
        -- Recebe objeto dicionário com todos os jogadores
        :return:
        """
        msg = constant.GET_PLAYERS
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        dim = int.from_bytes(data, byteorder='big', signed=True)
        rec: bytes = self.s.recv(dim)
        players = json.loads(rec)
        return players

    def get_nr_players(self):
        msg = constant.NR_PLAYERS
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        nr = int.from_bytes(data, byteorder='big', signed=True)
        return nr

    def add_player(self, name: str) -> int:
        """
        Protocolo:
        - enviar msg com o nome associado ao pedido 'add player'
        - enviar o nome do jogador
        - receber o número do jogador
        :param name:
        :return:
        """
        msg = constant.ADD_PLAYER
        self.s.send(msg.encode(constant.COD_STR))
        msg = name
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        number = int.from_bytes(data, byteorder='big', signed=True)

        return number

    def dimensions_size(self) -> tuple:
        """
        Protocolo:
        - enviar msg com nome associado ao pedido max_x e max_y.
        - servidor retorna dois inteiros com essa informação.

        :return:
        """
        msg = constant.X_MAX
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        x_max = int.from_bytes(data, byteorder='big', signed=True)
        msg = constant.Y_MAX
        self.s.send(msg.encode(constant.COD_STR))
        data: bytes = self.s.recv(constant.N_BYTES)
        y_max = int.from_bytes(data, byteorder='big', signed=True)
        return (x_max, y_max)

    # pos = gm.execute(M_UP, "player", self.number)

    def execute(self, mov: int, type: str, player: int) -> tuple:
        """
        Protocolo:
        -- Envia o tipo de msg 'player mov'
        -- Envia o movimento
        -- Envia o nr do jogador
        -- Recebe a nova posição do jogador (túpulo) que é estrutura de dados complexa.
        ----- recebo primeiro a dimensão da estrutura de dados
        ----- recebo a estrutura (tuple)
        :param mov:
        :param type:
        :param player:
        :return: new player position
        """
        msg = constant.PLAYER_MOV
        self.s.send(msg.encode(constant.COD_STR))
        self.s.send(mov.to_bytes(constant.N_BYTES, byteorder="big", signed=True))
        self.s.send(player.to_bytes(constant.N_BYTES, byteorder="big", signed=True))
        data: bytes = self.s.recv(constant.N_BYTES)
        dim = int.from_bytes(data, byteorder='big', signed=True)
        rec: bytes = self.s.recv(dim)
        tuple = json.loads(rec)
        return tuple


"""
    def add(self, value1: int, value2: int) -> Union[int, None]:

        msg = constante.SOMA
        self.s.send(msg.encode(constante.CODIFICACAO_STR))
        self.s.send(value1.to_bytes(constante.N_BYTES, byteorder="big", signed=True))
        self.s.send(value2.to_bytes(constante.N_BYTES, byteorder="big", signed=True))
        dados_recebidos: bytes = self.s.recv(constante.N_BYTES)
        return int.from_bytes(dados_recebidos, byteorder='big', signed=True)
        #if msg != constante.FIM:
        #    dados_recebidos: bytes = self.s.recv(constante.TAMANHO_MENSAGEM)
        #    return dados_recebidos.decode(constante.CODIFICACAO_STR)
        #else:
        #    self.s.close()
    """