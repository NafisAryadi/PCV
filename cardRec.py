#################################################
# M. Izdiar Alnafisi Aryadi - 5024211015 - PCV(B)
# Card Recognition with Python3
#################################################
#Import library dan modul yang nantinya digunakan dalam program
#################################################

import numpy as np
import cv2
import copy
import time
from keras.models import load_model

class CardRec():
    def __init__(self,input_cam):
        self.cam = input_cam

        self.LabelKelasNum=("Kartu Tutup",
            "Club 2",
            "Club 3",
            "Club 4",
            "Club 5",
            "Club 6",
            "Club 7",
            "Club 8",
            "Club 9",
            "Club 10",
            "Club J",
            "Club Q",
            "Club K",
            "Club A",
            "Heart 2",
            "Heart 3",
            "Heart 4",
            "Heart 5",
            "Heart 6",
            "Heart 7",
            "Heart 8",
            "Heart 9",
            "Heart 10",
            "Heart J",
            "Heart Q",
            "Heart K",
            "Heart A",
            "Diamond 2",
            "Diamond 3",
            "Diamond 4",
            "Diamond 5",
            "Diamond 6",
            "Diamond 7",
            "Diamond 8",
            "Diamond 9",
            "Diamond 10",
            "Diamond J",
            "Diamond Q",
            "Diamond K",
            "Diamond A",
            "Spade 2",
            "Spade 3",
            "Spade 4",
            "Spade 5",
            "Spade 6",
            "Spade 7",
            "Spade 8",
            "Spade 9",
            "Spade 10",
            "Spade J",
            "Spade Q",
            "Spade K",
            "Spade A")

        self.card_value = {"Kartu Tutup" : 0,
            "Club 2" : 2,
            "Club 3" : 3,
            "Club 4" : 4,
            "Club 5" : 5,
            "Club 6" : 6,
            "Club 7" : 7,
            "Club 8" : 8,
            "Club 9" : 9,
            "Club 10" : 10,
            "Club J" : 10,
            "Club Q" : 10,
            "Club K" : 10,
            "Club A" : 11,
            "Heart 2" : 2,
            "Heart 3" : 3,
            "Heart 4" : 4,
            "Heart 5" : 5,
            "Heart 6" : 6,
            "Heart 7" : 7,
            "Heart 8" : 8,
            "Heart 9" : 9,
            "Heart 10" : 10,
            "Heart J" : 10,
            "Heart Q" : 10,
            "Heart K" : 10,
            "Heart A" : 11,
            "Diamond 2" : 2,
            "Diamond 3" : 3,
            "Diamond 4" : 4,
            "Diamond 5" : 5,
            "Diamond 6" : 6,
            "Diamond 7" : 7,
            "Diamond 8" : 8,
            "Diamond 9" : 9,
            "Diamond 10" : 10,
            "Diamond J" : 10,
            "Diamond Q" : 10,
            "Diamond K" : 10,
            "Diamond A" : 11,
            "Spade 2" : 2,
            "Spade 3" : 3,
            "Spade 4" : 4,
            "Spade 5" : 5,
            "Spade 6" : 6,
            "Spade 7" : 7,
            "Spade 8" : 8,
            "Spade 9" : 9,
            "Spade 10" : 10,
            "Spade J" : 10,
            "Spade Q" : 10,
            "Spade K" : 10,
            "Spade A" : 11}

        self.avbl_card = ["Kartu Tutup",
            "Club 2",
            "Club 3",
            "Club 4",
            "Club 5",
            "Club 6",
            "Club 7",
            "Club 8",
            "Club 9",
            "Club 10",
            "Club J",
            "Club Q",
            "Club K",
            "Club A",
            "Heart 2",
            "Heart 3",
            "Heart 4",
            "Heart 5",
            "Heart 6",
            "Heart 7",
            "Heart 8",
            "Heart 9",
            "Heart 10",
            "Heart J",
            "Heart Q",
            "Heart K",
            "Heart A",
            "Diamond 2",
            "Diamond 3",
            "Diamond 4",
            "Diamond 5",
            "Diamond 6",
            "Diamond 7",
            "Diamond 8",
            "Diamond 9",
            "Diamond 10",
            "Diamond J",
            "Diamond Q",
            "Diamond K",
            "Diamond A",
            "Spade 2",
            "Spade 3",
            "Spade 4",
            "Spade 5",
            "Spade 6",
            "Spade 7",
            "Spade 8",
            "Spade 9",
            "Spade 10",
            "Spade J",
            "Spade Q",
            "Spade K",
            "Spade A"]

        self.urutan = ['Scan Kartu','Komputer', 'Player1', 'Player2']
        self.turnCounter = 0
        self.turn = "Scan Kartu"

        self.GameState = 0
        self.kartu_player1 = []
        self.state_player1 = ""
        self.value_player1 = 0
        self.score_player1 = 0
        self.temp_list_plyr1 = []
        self.kartu_player2 = []
        self.state_player2 = ""
        self.value_player2 = 0
        self.score_player2 = 0
        self.temp_list_plyr2 = []
        self.kartu_komputer = []
        self.state_komputer = ""
        self.value_komputer = 0
        self.score_komputer = 0
        self.temp_list_komp = []
        self.kartu_dealer = []
        self.value_dealer = 0
        self.score_dealer = 0
        self.temp_list_deal = []

        self.temp_last_komp = ""
        self.temp_last_plyr1 = ""
        self.temp_last_plyr2 = ""
        self.temp_last_komp = ""

        self.state_round = "Play"

    #################################################
    #fungsi start / restart game blackJack
    #################################################
    def BlackJackStart(self):
        print("~ ~ ~ BlackJack START ~ ~ ~")
        self.avbl_card = ["Kartu Tutup",
        "Club 2",
        "Club 3",
        "Club 4",
        "Club 5",
        "Club 6",
        "Club 7",
        "Club 8",
        "Club 9",
        "Club 10",
        "Club J",
        "Club Q",
        "Club K",
        "Club A",
        "Heart 2",
        "Heart 3",
        "Heart 4",
        "Heart 5",
        "Heart 6",
        "Heart 7",
        "Heart 8",
        "Heart 9",
        "Heart 10",
        "Heart J",
        "Heart Q",
        "Heart K",
        "Heart A",
        "Diamond 2",
        "Diamond 3",
        "Diamond 4",
        "Diamond 5",
        "Diamond 6",
        "Diamond 7",
        "Diamond 8",
        "Diamond 9",
        "Diamond 10",
        "Diamond J",
        "Diamond Q",
        "Diamond K",
        "Diamond A",
        "Spade 2",
        "Spade 3",
        "Spade 4",
        "Spade 5",
        "Spade 6",
        "Spade 7",
        "Spade 8",
        "Spade 9",
        "Spade 10",
        "Spade J",
        "Spade Q",
        "Spade K",
        "Spade A"]

        self.GameState = 0
        self.turnCounter = 0
        self.turn = "Scan Kartu"

        self.kartu_player1 = []
        self.state_player1 = ""
        self.value_player1 = 0
        self.score_player1 = 0
        self.temp_list_plyr1 = []
        self.kartu_player2 = []
        self.state_player2 = ""
        self.value_player2 = 0
        self.score_player2 = 0
        self.temp_list_plyr2 = []
        self.kartu_komputer = []
        self.state_komputer = ""
        self.value_komputer = 0
        self.score_komputer = 0
        self.temp_list_komp = []
        self.kartu_dealer = []
        self.value_dealer = 0
        self.score_dealer = 0
        self.temp_list_deal = []

        self.state_round = "Play"

    #################################################
    #fungsi mengakhiri round
    #################################################
    def roundEnd(self):
        self.state_round = "End"

    #################################################
    #fungsi untuk berpindah ke round selanjutnya
    #################################################
    def BlackJackRound(self):
        self.GameState += 1
        self.turnCounter = 0
        self.turn = "Scan Kartu"
        self.state_round = "play"

        self.kartu_player1 = []
        self.value_player1 = 0
        self.temp_list_plyr1 = []
        self.kartu_player2 = []
        self.value_player2 = 0
        self.temp_list_plyr2 = []
        self.kartu_komputer = []
        self.value_komputer = 0
        self.temp_list_komp = []
        self.kartu_dealer = []
        self.value_dealer = 0
        self.temp_list_deal = []

    #################################################
    #fungsi untuk mengakhiri game
    #################################################
    def BlackJackEnd(self):
        self.GameState = 5

    #################################################
    #fungsi untuk mengganti giliran
    #################################################
    def changeTurn(self):
        self.turnCounter += 1
        self.state_komputer = ""
        self.state_player1 = ""
        self.state_player2 = ""
        if self.turnCounter <=3:
            self.turn = self.urutan[self.turnCounter]
        else:
            self.turnCounter = 0

    #################################################
    #fungsi return state player hit
    #################################################
    def hitMe(self):
        if self.turn == "Player1":
            self.temp_last_plyr1 = self.kartu_player1[-1]
            self.state_player1 = 'Hit'
        else:
            self.temp_last_plyr2 = self.kartu_player2[-1]
            self.state_player2 = "Hit"

    #################################################
    #fungsi return state player stand
    #################################################
    def standMe(self):
        if self.turn == "Player1":
            self.state_player1 = 'Stand'
        else:
            self.state_player2 = 'Stand'

    #################################################
    #fungsi menentukan game state
    #################################################
    def BlackJackState(self):
        if self.GameState == 0:
            return "Start"
        elif self.GameState >= 5:
            return "End"
        else:
            return "Play"

    #################################################
    #fungsi logika komputer
    #################################################
    def KompLogic(self):
        if (('Club 10' in self.kartu_komputer or 'Heart 10' in self.kartu_komputer or 'Diamond 10' in self.kartu_komputer or 'Spade 10' in self.kartu_komputer) or ('Club J' in self.kartu_komputer or 'Heart J' in self.kartu_komputer or 'Diamond J' in self.kartu_komputer or 'Spade J' in self.kartu_komputer) or ('Club Q' in self.kartu_komputer or 'Heart Q' in self.kartu_komputer or 'Diamond Q' in self.kartu_komputer or 'Spade Q' in self.kartu_komputer) or ('Club K' in self.kartu_komputer or 'Heart K' in self.kartu_komputer or 'Diamond K' in self.kartu_komputer or 'Spade K' in self.kartu_komputer)) and ('Club A' in self.kartu_komputer or 'Heart A' in self.kartu_komputer or 'Diamond A' in self.kartu_komputer or 'Spade A' in self.kartu_komputer):
            self.state_komputer = 'Stand'
        elif self.value_komputer <= 11:
            self.temp_last_komp = self.kartu_komputer[-1]
            self.state_komputer = 'Hit'
        elif self.value_komputer >= 17:
            self.state_komputer = 'Stand'
        elif (self.value_komputer >= 13 and self.value_komputer < 17) and self.value_dealer <=6:
            self.state_komputer = 'Stand'
        elif (self.value_komputer >= 13 and self.value_komputer < 17) and self.value_dealer >=6:
            self.temp_last_komp = self.kartu_komputer[-1]
            self.state_komputer = 'Hit'
        elif self.value_komputer == 12 and (self.value_dealer == 2 or self.value_dealer == 3):
            self.state_komputer = 'Stand'
        elif self.value_komputer == 12 and (self.value_dealer > 3 and self.value_dealer <= 6):
            self.state_komputer = 'Stand'
        elif self.value_komputer == 12 and self.value_dealer >= 7:
            self.temp_last_komp = self.kartu_komputer[-1]
            self.state_komputer = 'Hit'
        else:
            pass

    #################################################
    #fungsi untuk menambah score dari value
    #################################################
    def scoring(self):
        if self.value_komputer > 21:
            self.score_komputer += 0
        if self.value_player1 > 21:
            self.score_player1 += 0
        if self.value_player2 > 21:
            self.score_player2 += 0

        if self.value_komputer == 21:
            self.score_komputer += 2
        if self.value_player1 == 21:
            self.score_player1 += 2
        if self.value_player2 == 21:
            self.score_player2 += 2

        if (self.value_komputer >= self.value_dealer or self.value_dealer > 21) and (self.value_komputer >= self.value_player1 or self.value_player1 > 21) and (self.value_komputer >= self.value_player2 or self.value_player2 > 21)  and self.value_komputer <21 :
            self.score_komputer += 2
        if (self.value_player1 >= self.value_dealer or self.value_dealer > 21) and (self.value_player1 >= self.value_komputer or self.value_komputer > 21) and (self.value_player1 >= self.value_player2 or self.value_player2 > 21) and self.value_player1 <21 :
            self.score_player1 += 2
        if (self.value_player2 >= self.value_dealer or self.value_dealer > 21) and (self.value_player2 >= self.value_komputer or self.value_komputer > 21) and (self.value_player2 >= self.value_player1 or self.value_player1 > 21) and self.value_player2 <21 :
            self.score_player2 += 2

    #################################################
    #fungsi hitung value player
    #################################################
    def hitungValue(self,list_kartu):
        hasil = 0
        for i in list_kartu:
            hasil += self.card_value[i]
        if hasil > 21 and ('Club A' in list_kartu or 'Heart A' in list_kartu or 'Diamond A' in list_kartu or 'Spade A' in list_kartu):
            return hasil - 10
        else:
            return hasil

    #################################################
    #fungsi cek templist
    #################################################
    def cekTempList(self,temp_list):
        if temp_list == ['Kartu Tutup','Kartu Tutup','Kartu Tutup','Kartu Tutup','Kartu Tutup']:
            return 'Kartu Tutup'

        elif temp_list == ['Club 2','Club 2','Club 2','Club 2','Club 2']:
            return 'Club 2'
        elif temp_list == ['Club 3','Club 3','Club 3','Club 3','Club 3']:
            return 'Club 3'
        elif temp_list == ['Club 4','Club 4','Club 4','Club 4','Club 4']:
            return 'Club 4'
        elif temp_list == ['Club 5','Club 5','Club 5','Club 5','Club 5']:
            return 'Club 5'
        elif temp_list == ['Club 6','Club 6','Club 6','Club 6','Club 6']:
            return 'Club 6'
        elif temp_list == ['Club 7','Club 7','Club 7','Club 7','Club 7']:
            return 'Club 7'
        elif temp_list == ['Club 8','Club 8','Club 8','Club 8','Club 8']:
            return 'Club 8'
        elif temp_list == ['Club 9','Club 9','Club 9','Club 9','Club 9']:
            return 'Club 9'
        elif temp_list == ['Club 10','Club 10','Club 10','Club 10','Club 10']:
            return 'Club 10'
        elif temp_list == ['Club J','Club J','Club J','Club J','Club J']:
            return 'Club J'
        elif temp_list == ['Club Q','Club Q','Club Q','Club Q','Club Q']:
            return 'Club Q'
        elif temp_list == ['Club K','Club K','Club K','Club K','Club K']:
            return 'Club K'
        elif temp_list == ['Club A','Club A','Club A','Club A','Club A']:
            return 'Club A'

        elif temp_list == ['Heart 2','Heart 2','Heart 2','Heart 2','Heart 2']:
            return 'Heart 2'
        elif temp_list == ['Heart 3','Heart 3','Heart 3','Heart 3','Heart 3']:
            return 'Heart 3'
        elif temp_list == ['Heart 4','Heart 4','Heart 4','Heart 4','Heart 4']:
            return 'Heart 4'
        elif temp_list == ['Heart 5','Heart 5','Heart 5','Heart 5','Heart 5']:
            return 'Heart 5'
        elif temp_list == ['Heart 6','Heart 6','Heart 6','Heart 6','Heart 6']:
            return 'Heart 6'
        elif temp_list == ['Heart 7','Heart 7','Heart 7','Heart 7','Heart 7']:
            return 'Heart 7'
        elif temp_list == ['Heart 8','Heart 8','Heart 8','Heart 8','Heart 8']:
            return 'Heart 8'
        elif temp_list == ['Heart 9','Heart 9','Heart 9','Heart 9','Heart 9']:
            return 'Heart 9'
        elif temp_list == ['Heart 10','Heart 10','Heart 10','Heart 10','Heart 10']:
            return 'Heart 10'
        elif temp_list == ['Heart J','Heart J','Heart J','Heart J','Heart J']:
            return 'Heart J'
        elif temp_list == ['Heart Q','Heart Q','Heart Q','Heart Q','Heart Q']:
            return 'Heart Q'
        elif temp_list == ['Heart K','Heart K','Heart K','Heart K','Heart K']:
            return 'Heart K'
        elif temp_list == ['Heart A','Heart A','Heart A','Heart A','Heart A']:
            return 'Heart A'

        elif temp_list == ['Diamond 2','Diamond 2','Diamond 2','Diamond 2','Diamond 2']:
            return 'Diamond 2'
        elif temp_list == ['Diamond 3','Diamond 3','Diamond 3','Diamond 3','Diamond 3']:
            return 'Diamond 3'
        elif temp_list == ['Diamond 4','Diamond 4','Diamond 4','Diamond 4','Diamond 4']:
            return 'Diamond 4'
        elif temp_list == ['Diamond 5','Diamond 5','Diamond 5','Diamond 5','Diamond 5']:
            return 'Diamond 5'
        elif temp_list == ['Diamond 6','Diamond 6','Diamond 6','Diamond 6','Diamond 6']:
            return 'Diamond 6'
        elif temp_list == ['Diamond 7','Diamond 7','Diamond 7','Diamond 7','Diamond 7']:
            return 'Diamond 7'
        elif temp_list == ['Diamond 8','Diamond 8','Diamond 8','Diamond 8','Diamond 8']:
            return 'Diamond 8'
        elif temp_list == ['Diamond 9','Diamond 9','Diamond 9','Diamond 9','Diamond 9']:
            return 'Diamond 9'
        elif temp_list == ['Diamond 10','Diamond 10','Diamond 10','Diamond 10','Diamond 10']:
            return 'Diamond 10'
        elif temp_list == ['Diamond J','Diamond J','Diamond J','Diamond J','Diamond J']:
            return 'Diamond J'
        elif temp_list == ['Diamond Q','Diamond Q','Diamond Q','Diamond Q','Diamond Q']:
            return 'Diamond Q'
        elif temp_list == ['Diamond K','Diamond K','Diamond K','Diamond K','Diamond K']:
            return 'Diamond K'
        elif temp_list == ['Diamond A','Diamond A','Diamond A','Diamond A','Diamond A']:
            return 'Diamond A'

        elif temp_list == ['Spade 2','Spade 2','Spade 2','Spade 2','Spade 2']:
            return 'Spade 2'
        elif temp_list == ['Spade 3','Spade 3','Spade 3','Spade 3','Spade 3']:
            return 'Spade 3'
        elif temp_list == ['Spade 4','Spade 4','Spade 4','Spade 4','Spade 4']:
            return 'Spade 4'
        elif temp_list == ['Spade 5','Spade 5','Spade 5','Spade 5','Spade 5']:
            return 'Spade 5'
        elif temp_list == ['Spade 6','Spade 6','Spade 6','Spade 6','Spade 6']:
            return 'Spade 6'
        elif temp_list == ['Spade 7','Spade 7','Spade 7','Spade 7','Spade 7']:
            return 'Spade 7'
        elif temp_list == ['Spade 8','Spade 8','Spade 8','Spade 8','Spade 8']:
            return 'Spade 8'
        elif temp_list == ['Spade 9','Spade 9','Spade 9','Spade 9','Spade 9']:
            return 'Spade 9'
        elif temp_list == ['Spade 10','Spade 10','Spade 10','Spade 10','Spade 10']:
            return 'Spade 10'
        elif temp_list == ['Spade J','Spade J','Spade J','Spade J','Spade J']:
            return 'Spade J'
        elif temp_list == ['Spade Q','Spade Q','Spade Q','Spade Q','Spade Q']:
            return 'Spade Q'
        elif temp_list == ['Spade K','Spade K','Spade K','Spade K','Spade K']:
            return 'Spade K'
        elif temp_list == ['Spade A','Spade A','Spade A','Spade A','Spade A']:
            return 'Spade A'

    #################################################
    #fungsi filter gambar dengan output hasil threshold
    #################################################
    def filterGambar(self,Gmb):
        GmbGray =cv2.cvtColor(Gmb, cv2.COLOR_BGR2GRAY)
        GmbThd = cv2.adaptiveThreshold(GmbGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,23,8)
        kernel = np.array((3,3))
        GmbDil = cv2.dilate(GmbThd, kernel, iterations= 2)
        GmbEro = cv2.erode(GmbDil, kernel, iterations= 1)
        return GmbEro

    #################################################
    #fungsi wrap gambar untuk di crop
    #################################################
    def WrapKartu(self,Gmb,kontur, approx):
        x, y, w, h = cv2.boundingRect(approx)
        #print(x,y,w,h)
        ujung_awal = approx.reshape(4, 2).astype(np.float32)
        ujung_baru = np.float32([[0,0], [w,0], [w,h], [0,h]])
        matrix_trans = cv2.getPerspectiveTransform(ujung_awal, ujung_baru)
        warpGmb = cv2.warpPerspective(Gmb, matrix_trans, (w,h))
        return cv2.flip(warpGmb,1)


    #################################################
    #fungsi menampilkan floating text
    #################################################
    def tampilText(self,Gmb,sText,pos):
        font        = cv2.FONT_HERSHEY_SIMPLEX
        posf        = pos
        fontScale   = .7
        fontColor   = (0,0,255)
        thickness   = 2
        lineType    = 2
        cv2.putText(Gmb,sText,
            posf,
            font,
            fontScale,
            fontColor,
            thickness,
            lineType)
        return copy.deepcopy(Gmb)

    #################################################
    #fungsi utama program
    #################################################
    def mainFunc(self):
        ret, frame = self.cam.read()
        background = np.ones((480, 640, 3), dtype=np.uint8) * 255
        side_screen = np.ones((160, 640, 3), dtype=np.uint8) * 255
        mdCard = load_model("C:\PCV\CardRec\weightCard.h5")
        GmbFiltered = self.filterGambar(frame)
        GmbCanny =cv2.Canny(GmbFiltered,50,150)
        ConGmb, hierarki = cv2.findContours(GmbCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #time.sleep(0.2)
        for i in ConGmb:
            area = cv2.contourArea(i)
            eps = 0.02 * cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i, eps, True)
            if len(approx) ==4:
                if area > 10000 and area < 100000 :
                    x, y, w, h = cv2.boundingRect(i)
                    center_x = x + w // 2
                    center_y = y + h // 2
                    if center_x < frame.shape[1] // 2 and center_y < frame.shape[0] // 2:
                        hasil_warp_kiri = self.WrapKartu(GmbFiltered, i, approx)
                        cv2.imshow("kiri", hasil_warp_kiri)
                        cv2.drawContours(frame,[approx],-1,(0,0,255),2)

                        Lhasil_warp_kiri=[]
                        hasil_warp_kiri = cv2.cvtColor(hasil_warp_kiri, cv2.COLOR_GRAY2BGR)
                        imgWarp_kiri = cv2.resize(hasil_warp_kiri,(128,128))
                        imgWarp_kiri = imgWarp_kiri.astype('float32')/255
                        Lhasil_warp_kiri.append(imgWarp_kiri)
                        Lhasil_warp_kiri = np.array(Lhasil_warp_kiri)

                        # Predict
                        hs_kiri = mdCard.predict(Lhasil_warp_kiri,verbose = 0)
                        nCard_kiri = np.max(np.where(hs_kiri== hs_kiri.max()))
                        self.tampilText(frame, self.LabelKelasNum[nCard_kiri],(10,20))

                        #input ke list
                        self.temp_list_deal.append(self.LabelKelasNum[nCard_kiri])
                        if len(self.temp_list_deal) > 5:
                            self.temp_list_deal.pop(0)
                        if self.cekTempList(self.temp_list_deal) in self.avbl_card:
                            self.kartu_dealer.append(self.cekTempList(self.temp_list_deal))
                            self.avbl_card.remove(self.cekTempList(self.temp_list_deal))
                        self.value_dealer = self.hitungValue(self.kartu_dealer)
                        print('kartu_dealer = ',self.kartu_dealer)

                    elif center_x < frame.shape[1] // 2 and center_y >= frame.shape[0] // 2:
                        hasil_warp_kiribwh = self.WrapKartu(GmbFiltered, i, approx)
                        cv2.imshow("kiribwh", hasil_warp_kiribwh)
                        cv2.drawContours(frame,[approx],-1,(0,0,255),2)

                        Lhasil_warp_kiribwh=[]
                        hasil_warp_kiribwh = cv2.cvtColor(hasil_warp_kiribwh, cv2.COLOR_GRAY2BGR)
                        imgWarp_kiribwh = cv2.resize(hasil_warp_kiribwh,(128,128))
                        imgWarp_kiribwh = imgWarp_kiribwh.astype('float32')/255
                        Lhasil_warp_kiribwh.append(imgWarp_kiribwh)
                        Lhasil_warp_kiribwh = np.array(Lhasil_warp_kiribwh)

                        # Predict
                        hs_kiribwh = mdCard.predict(Lhasil_warp_kiribwh,verbose = 0)
                        nCard_kiribwh = np.max(np.where(hs_kiribwh== hs_kiribwh.max()))
                        self.tampilText(frame, self.LabelKelasNum[nCard_kiribwh],(10,(frame.shape[0] // 2) + 20))

                        #input ke list
                        self.temp_list_plyr1.append(self.LabelKelasNum[nCard_kiribwh])
                        if len(self.temp_list_plyr1) > 5:
                            self.temp_list_plyr1.pop(0)
                        if self.cekTempList(self.temp_list_plyr1) in self.avbl_card:
                            self.kartu_player1.append(self.cekTempList(self.temp_list_plyr1))
                            self.avbl_card.remove(self.cekTempList(self.temp_list_plyr1))
                        self.value_player1 = self.hitungValue(self.kartu_player1)
                        print('kartu_player1 = ',self.kartu_player1)

                    elif center_x >= frame.shape[1] // 2 and center_y < frame.shape[0] // 2:
                        hasil_warp_kanan = self.WrapKartu(GmbFiltered, i, approx)
                        cv2.imshow("kanan", hasil_warp_kanan)
                        cv2.drawContours(frame,[approx],-1,(0,0,255),2)

                        Lhasil_warp_kanan=[]
                        hasil_warp_kanan = cv2.cvtColor(hasil_warp_kanan, cv2.COLOR_GRAY2BGR)
                        imgWarp_kanan = cv2.resize(hasil_warp_kanan,(128,128))
                        imgWarp_kanan = imgWarp_kanan.astype('float32')/255
                        Lhasil_warp_kanan.append(imgWarp_kanan)
                        Lhasil_warp_kanan = np.array(Lhasil_warp_kanan)

                        # Predict
                        hs_kanan = mdCard.predict(Lhasil_warp_kanan,verbose = 0)
                        nCard_kanan = np.max(np.where(hs_kanan== hs_kanan.max()))
                        self.tampilText(frame, self.LabelKelasNum[nCard_kanan],((frame.shape[1] // 2) + 10,20))

                        #input ke list
                        self.temp_list_komp.append(self.LabelKelasNum[nCard_kanan])
                        if len(self.temp_list_komp) > 5:
                            self.temp_list_komp.pop(0)
                        if self.cekTempList(self.temp_list_komp) in self.avbl_card:
                            self.kartu_komputer.append(self.cekTempList(self.temp_list_komp))
                            self.avbl_card.remove(self.cekTempList(self.temp_list_komp))
                        self.value_komputer = self.hitungValue(self.kartu_komputer)
                        print('kartu_komputer = ',self.kartu_komputer)

                    else:
                        hasil_warp_kananbwh = self.WrapKartu(GmbFiltered, i, approx)
                        cv2.imshow("kananbwh", hasil_warp_kananbwh)
                        cv2.drawContours(frame,[approx],-1,(0,0,255),2)

                        Lhasil_warp_kananbwh=[]
                        hasil_warp_kananbwh = cv2.cvtColor(hasil_warp_kananbwh, cv2.COLOR_GRAY2BGR)
                        imgWarp_kananbwh = cv2.resize(hasil_warp_kananbwh,(128,128))
                        imgWarp_kananbwh = imgWarp_kananbwh.astype('float32')/255
                        Lhasil_warp_kananbwh.append(imgWarp_kananbwh)
                        Lhasil_warp_kananbwh = np.array(Lhasil_warp_kananbwh)

                        # Predict
                        hs_kananbwh = mdCard.predict(Lhasil_warp_kananbwh,verbose = 0)
                        nCard_kananbwh = np.max(np.where(hs_kananbwh== hs_kananbwh.max()))
                        self.tampilText(frame, self.LabelKelasNum[nCard_kananbwh],((frame.shape[1] // 2) + 10,(frame.shape[0] // 2) + 20))

                        #input ke list
                        self.temp_list_plyr2.append(self.LabelKelasNum[nCard_kananbwh])
                        if len(self.temp_list_plyr2) > 5:
                            self.temp_list_plyr2.pop(0)
                        if self.cekTempList(self.temp_list_plyr2) in self.avbl_card:
                            self.kartu_player2.append(self.cekTempList(self.temp_list_plyr2))
                            self.avbl_card.remove(self.cekTempList(self.temp_list_plyr2))
                        self.value_player2 = self.hitungValue(self.kartu_player2)
                        print('kartu_player2 =',self.kartu_player2)

        if self.BlackJackState() == "Start":
            #print("Press n to start round 1")
            self.tampilText(side_screen, "M. Izdiar Alnafisi Aryadi",(10,20))
            self.tampilText(side_screen, "5024211015 - PCV B",(10,50))

            self.kartu_dealer = []
            self.value_dealer = 0
            self.kartu_komputer = []
            self.value_komputer = 0
            self.kartu_player1 = []
            self.value_player1 = 0
            self.kartu_player2 = []
            self.value_player2 = 0
            time.sleep(3.0)
            self.BlackJackRound()
        elif self.BlackJackState() == "Play":
            print("Round "+str(self.GameState))
            self.tampilText(side_screen, "ROUND " + str(self.GameState),(10,20))

            if self.turnCounter == 0:
                self.tampilText(side_screen,"Scan 1 dealer card, 2 Komputer card,", (10,50))
                self.tampilText(side_screen,"2 Player 1 card and 2 Player 2 card",(10,70))
                if len(self.kartu_dealer) >= 1 and len(self.kartu_komputer) >= 2 and len(self.kartu_player1) >= 2 and len(self.kartu_player2) >= 2:
                    self.changeTurn()

            elif self.state_round == 'End':
                if self.value_dealer < 17:
                    self.tampilText(side_screen,"Turn Ended", (10,50))
                    self.tampilText(side_screen, "Scan more card until dealer",(10,80))
                    self.tampilText(side_screen, "card's value is above 16",(10,100))
                else:
                    self.scoring()
                    time.sleep(10)
                    self.BlackJackRound()

            else:
                self.tampilText(side_screen,"Turn : "+ self.turn, (10,50))
                self.tampilText(side_screen, "Press h to Hit",(10,80))
                self.tampilText(side_screen, "Press s to Stand",(10,100))

                if self.turnCounter == 1:
                    self.KompLogic()
                    time.sleep(5)
                    if self.state_komputer == 'Hit':
                        self.tampilText(side_screen, "Komputer want to Hit, Scan a card",(10,150))
                        if self.kartu_komputer[-1] != self.temp_last_komp:
                            self.changeTurn()
                    elif self.state_komputer == 'Stand':
                        self.tampilText(side_screen, "Komputer Stand",(10,150))
                        time.sleep(3)
                        self.changeTurn()

                elif self.turnCounter == 2:
                    if self.state_player1 == 'Hit':
                        self.tampilText(side_screen, "Player 1 want to Hit, Scan a card",(10,150))
                        if self.kartu_player1[-1] != self.temp_last_plyr1:
                            self.changeTurn()
                    elif self.state_player1 == 'Stand':
                        self.tampilText(side_screen, "Player 1 Stand",(10,150))
                        time.sleep(3)
                        self.changeTurn()

                elif self.turnCounter == 3:
                    if self.state_player2 == 'Hit':
                        self.tampilText(side_screen, "Player 2 want to Hit, Scan a card",(10,150))
                        if self.kartu_player2[-1] != self.temp_last_plyr2:
                            self.changeTurn()
                    elif self.state_player2 == 'Stand':
                        self.tampilText(side_screen, "Player 2 Stand",(10,150))
                        time.sleep(3)
                        self.changeTurn()


        elif self.BlackJackState() == "End":
            print("Game Ended")
            if self.score_komputer == self.score_player1 and self.score_komputer == self.score_player2:
                self.tampilText(side_screen,"Match Draw (no winner)", (150,20))

            elif self.score_komputer >= self.score_player1 and self.score_komputer >= self.score_player2:
                if self.score_komputer == self.score_player1:
                    self.tampilText(side_screen,"Winner : Komputer and Player 1", (150,20))
                elif self.score_komputer == self.score_player2:
                    self.tampilText(side_screen,"Winner : Komputer and Player 2", (150,20))
                else:
                    self.tampilText(side_screen,"Winner : Komputer", (150,20))

            elif self.score_player1 >= self.score_komputer and self.score_player1 >= self.score_player2:
                if self.score_player1 == self.score_komputer:
                    self.tampilText(side_screen,"Winner : Player 1 and Komputer", (150,20))
                elif self.score_player1 == self.score_player2:
                    self.tampilText(side_screen,"Winner : Player 1 and Player 2", (150,20))
                else:
                    self.tampilText(side_screen,"Winner : Player 1", (150,20))

            elif self.score_player2 >= self.score_player1 and self.score_player2 >= self.score_komputer:
                if self.score_komputer == self.score_player2:
                    self.tampilText(side_screen,"Winner : Komputer and Player 2", (150,20))
                elif self.score_player1 == self.score_player2:
                    self.tampilText(side_screen,"Winner : Player 1 and Player 2", (150,20))
                else:
                    self.tampilText(side_screen,"Winner : Player 2", (150,20))

        #Game window
        self.tampilText(background, "Dealer ( "+ str(self.value_dealer)+" )",(10,20))
        for teksto in range(len(self.kartu_dealer)):
            self.tampilText(background, self.kartu_dealer[teksto],(10,50+(30*teksto)))
        self.tampilText(background, "Player 1 ( "+ str(self.value_player1)+" )[ "+ str(self.score_player1)+" ]",(10,(background.shape[0] // 2) + 20))
        for teksto in range(len(self.kartu_player1)):
            self.tampilText(background, self.kartu_player1[teksto],(10,(background.shape[0] // 2)+50+(30*teksto)))
        self.tampilText(background, "Komputer ( "+ str(self.value_komputer)+" )[ "+ str(self.score_komputer)+" ]",((background.shape[1] // 2) + 10,20))
        for teksto in range(len(self.kartu_komputer)):
            self.tampilText(background, self.kartu_komputer[teksto],((background.shape[1] // 2)+10,50+(30*teksto)))
        self.tampilText(background, "Player 2 ( "+ str(self.value_player2)+" )[ "+ str(self.score_player2)+" ]",((background.shape[1] // 2) + 10,(background.shape[0] // 2) + 20))
        for teksto in range(len(self.kartu_player2)):
            self.tampilText(background, self.kartu_player2[teksto],((background.shape[1] // 2)+10,(background.shape[0] // 2)+50+(30*teksto)))
        cv2.line(background, (background.shape[1] // 2, 0), (background.shape[1] // 2, background.shape[0]), (0, 0, 0), 2)
        cv2.line(background, (0, background.shape[0] // 2), (background.shape[1], background.shape[0] // 2), (0, 0, 0), 2)

        cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 0, 0), 2)
        cv2.line(frame, (0, frame.shape[0] // 2), (frame.shape[1], frame.shape[0] // 2), (0, 0, 0), 2)
        cv2.imshow("Game", background)
        cv2.imshow("State", side_screen)
        cv2.imshow("Scan Card",frame)


#################################################
#fungsi membaca webcam dan eksekusi fungsi utama
#################################################

webcam = cv2.VideoCapture(3)

CR=CardRec(webcam)

if not webcam.isOpened():
    print("webcam tidak terdeteksi")
    exit()

while True:
    CR.mainFunc()
    if cv2.waitKey(1)== ord('p'):
        print("--------------- Udah Kepencett ---------------")
        CR.BlackJackStart()

    if cv2.waitKey(1)== ord('n'):
        print("--------------- Udah Kepencett ---------------")
        CR.roundEnd()

    if cv2.waitKey(1)== ord('h'):
        print("--------------- Udah Kepencett ---------------")
        CR.hitMe()

    if cv2.waitKey(1)== ord('s'):
        print("--------------- Udah Kepencett ---------------")
        CR.standMe()

    if cv2.waitKey(1)== ord('z'):
        print("--------------- Udah Kepencett ---------------")
        CR.BlackJackEnd()

    if cv2.waitKey(1)==27:
        break

webcam.release()
cv2.destroyAllWindows()