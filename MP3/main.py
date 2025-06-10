import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from play import Ui_MainWindow  

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)
        self.isPaused = False

        self.ui.pushButton_play.clicked.connect(self.play)
        self.ui.pushButton_play_2.clicked.connect(self.play2)
        self.ui.pushButton_play_3.clicked.connect(self.play3)
        self.ui.pushButton_parar.clicked.connect(self.parar)
        self.ui.pushButton_pausar.clicked.connect(self.pausar)

        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)

    def play (self):
        caminho_musica = os.path.abspath("musicas/Nirvana - Come As You Are (Official Music Video).mp3")
        print("Local da musica:", caminho_musica)

        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")
            else:
                print("Erro: Caminho do arquivo inválido.")

    def play2 (self):
        caminho_musica = os.path.abspath("musicas/Tame Impala - Let It Happen (Official Video).mp3")
        print("Local da musica:", caminho_musica)

        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")
            else:
                print("Erro: Caminho do arquivo inválido.")

    def play3 (self):
        caminho_musica = os.path.abspath("musicas/HINO DO CORINTHIANS.mp3")
        print("Local da musica:", caminho_musica)

        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_musica)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")
            else:
                print("Erro: Caminho do arquivo inválido.")

    def parar (self):
        self.player.stop()
        self.isPaused = False
        print("A música parou!")

    def pausar (self):
        self.player.pause()
        self.isPaused = True
        print("A música pausou!")

    def controlar_volume (self):
        volume = self.ui.horizontalSlider_volume.value()
        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())