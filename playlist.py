# Reto construir un simulador de playlist de canciones. 

"""
Restricciones:
- Utiliza queues:
- Hay metodos para: añadir canciones y reproducirlas (sería eliminarlas de la queue)
- Se reproducen las canciones en el orden añadido. (FIFO - queue)
"""

class Playlist:
    def __init__(self) -> None:
        self.inbound_songs: list = []
        self.outbound_songs: list = []
        self.inbound_size: int = len(self.inbound_songs)
        self.outbound_size: int = len(self.outbound_songs)

    def enqueue(self, data) -> str:
        self.inbound_songs.append(data)
        self.inbound_size: int = len(self.inbound_songs)
        return "Success inbound"
    
    def dequeue(self) -> any:
        if not self.inbound_songs and not self.outbound_songs:
            return "You haven´t got songs in your playlist"
        else:
            while self.inbound_songs:
                self.outbound_songs.append(self.inbound_songs.pop())
            data = self.outbound_songs.pop()
            self.inbound_size: int = len(self.inbound_songs)
            self.outbound_size: int = len(self.outbound_songs)
            return data
    
    def total_dequeue(self) -> any:
        if not self.inbound_songs and not self.outbound_songs:
            return "You haven´t got songs in your playlist"
        else:
            while self.inbound_songs:
                self.outbound_songs.append(self.inbound_songs.pop())
            data: list = self.outbound_songs.copy()
            while self.outbound_songs:
                print(self.outbound_songs.pop())
            self.inbound_size: int = len(self.inbound_songs)
            self.outbound_size: int = len(self.outbound_songs)

            return data