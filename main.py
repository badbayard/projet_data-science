from PyQt5 import QtWidgets , QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QFileDialog, QMainWindow,QLCDNumber, QSlider,QVBoxLayout, QPushButton,QLabel,QAction, QLineEdit, QMessageBox, QInputDialog, QComboBox, QSpinBox, QProgressBar,QRadioButton
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QBasicTimer
import sys
sys.path.append(".")
import lireGraph2
import test_lireGraph




class Ui_MainWindow():
    
    def __init__(self):
        self.a =-1
        self.nom=""
        self.op=""
        self.Nomserie=""
        self.step=0
        self.time=False
        self.type_graph=""
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10,10,556,392))
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,673,125))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.showDialog)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QApplication.quit)
        
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.showAbout)
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionAbout)  #<------
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      

        
                
        # Create textbox
        self.textbox = QLineEdit(MainWindow)
        self.textbox.move(580,280)
        self.textbox.resize(280,40)
 
        # Create a button in the window
        self.button = QPushButton('Ok', MainWindow)
        self.button.move(580,320)
        
        #Create a button 2 in the window
        self.button2 = QPushButton('Drawing graphs',MainWindow)
        self.button2.move(580,165)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.button2.clicked.connect(self.on_click2)
        
        #Getchoice
        self.cb = QComboBox(MainWindow)
        self.cb.move(580,250)
        self.cb.addItem("")
        self.cb.addItem("Degree")
        self.cb.addItem("Closeness")
        self.cb.addItems(["Pagerank", "Betweeness"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        
        
        #object presents the user with a integer
        self.l1 = QLabel("current value:")
        self.l1.move(650,250)
        self.sp = QSpinBox(MainWindow)
        self.sp.setMaximum(1049)
        self.sp.move(700,250)
        self.sp.valueChanged.connect(self.valuechange)
        
        #Getchoice 2
        self.cb2 = QComboBox(MainWindow)
        self.cb2.move(580,50)
        self.cb2.addItem("")
        self.cb2.addItem("Game of Thrones")
        self.cb2.addItem("Breaking Bad")
        self.cb2.addItem("House of Card")
        self.cb2.currentIndexChanged.connect(self.selectionchange2)
        
        
        #Radiobutton for graph
        
        self.b0 = QRadioButton("Classical",MainWindow)
        self.b0.move(580,140)
        self.b0.setChecked(True)
        self.b0.toggled.connect(lambda:self.btnstate(self.b0))
        self.b1 = QRadioButton("Random",MainWindow)
        self.b1.move(580,80)
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        self.b2 = QRadioButton("Circular",MainWindow)
        self.b2.move(580,95)
        self.b2.setChecked(True)
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        self.b3 = QRadioButton("Spectral",MainWindow)
        self.b3.move(580,110)
        self.b3.setChecked(True)
        self.b3.toggled.connect(lambda:self.btnstate(self.b3))
        self.b4 = QRadioButton("Shell",MainWindow)
        self.b4.move(580,125)
        self.b4.setChecked(True)
        self.b4.toggled.connect(lambda:self.btnstate(self.b4))
        
        
        
        if self.time == False :
            #ProgressBar
            self.bar = QProgressBar(MainWindow)
            self.bar.setGeometry(50, 80, 500, 39)
            self.bar.move(140,650)
            self.bar.setMaximum(50)
            self.bar.setMinimum(0)
            
        
 
   
    def showDialog(self): #permetde charger l'image avec la bar du menu
        fileName = QFileDialog.getOpenFileName(MainWindow, 'Open file')[0]
        print(fileName)
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(fileName))
        self.graphicsView.setScene(self.scene)
        
    def showAbout(self):#permet d'afficher le about du menu
        QMessageBox.question(MainWindow,'About',"Authors of the program: Yannis Hutt and Julien Cadier", QMessageBox.Ok, QMessageBox.Ok)

        
    def retranslateUi(self, MainWindow):#permet de faire le menu déroulant
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mainwindow"))
        self.menuFile.setTitle(_translate("MainWindow","F&ile"))
        self.actionOpen.setText(_translate("MainWindow","Open"))
        self.actionAbout.setText(_translate("MainWindow","About"))
        self.actionExit.setText(_translate("MainWindow","Exit"))
        
        
    def on_click(self): #permet de faire l'évenement pour faire le graph
        self.bar.setMaximum(0)
        textboxValue = self.textbox.text()
        QMessageBox.question(MainWindow, 'result', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.nom = self.textbox.text()

        print(self.nom)
        print(self.op)
        lireGraph2.start_main(self.Nomserie,self.a,self.nom,self.op)
        self.scene = QGraphicsScene()
        self.scene.clearSelection()
        self.scene.addPixmap(QPixmap("images/" + self.nom +self.op+ ".jpg"))
        self.graphicsView.setScene(self.scene)
        self.bar.setMaximum(50)
    
    def on_click2(self):
        self.bar.setMaximum(0)
        test_lireGraph.start_graph(self.Nomserie,self.type_graph)
        self.scene = QGraphicsScene()
        self.scene.clearSelection()
        self.scene.addPixmap(QPixmap("images/" + self.Nomserie+"_"+self.type_graph+ ".jpg"))
        self.graphicsView.setScene(self.scene)
        self.bar.setMaximum(50)
        
    def selectionchange(self,i): # permet de faire la selection des opérations
        print ("Items in the list are :")
        for count in range(self.cb.count()):
            print (self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())
        self.op = self.cb.currentText()
        def f(x):
            return {
                    "" : 'essai',
                    "Degree" : 'd',
                    "Closeness" : 'c',
                    "Pagerank" : 'p',
                    "Betweeness" : 'b'
                    }[x]
        self.op=f(self.op)
        print(self.op)
        
        
    def selectionchange2(self,i):
        print("Items in the second list are :")
        for count in range(self.cb2.count()):
            print (self.cb2.itemText(count))
        print ("current index", i,"selection changed ", self.cb.currentText())
        self.Nomserie = self.cb2.currentText()
        print(self.Nomserie)
        
        
        
        
    def valuechange(self):
      self.l1.setText("current value:"+str(self.sp.value()))
      print(self.sp.value())
      self.a = self.sp.value() #affectation valeur int
      
    def text_changed(self):
        """ updates the list of possible completions each time a key is 
            pressed """
        pattern = str(self.le.text())
        self.new_list = [item for item in lireGraph2.dicoNomToNum if item.find(pattern) == 0]
        self.lm.setAllData(self.new_list)
        
    def btnstate(self,b): #permet de savoir quelle graph faire
        if b.text() == "Random":
            if b.isChecked() == True:
                print(b.text()+" is selected")
                self.type_graph = "Random"
            else:
                print(b.text()+" is deselcted")
       
        if b.text() == "Circular":
            if b.isChecked() == True:
                print(b.text()+" is selected")
                self.type_graph = "Circular"
            else:
                print(b.text()+" is deselcted")
            
        if b.text() == "Spectral":
            if b.isChecked() == True:
                print(b.text()+" is selected")
                self.type_graph = "Spectral"
            else:
                print(b.text()+" is deselcted")	
  
        if b.text() == "Shell":
            if b.isChecked() == True:
                print(b.text()+" is selected")
                self.type_graph = "Shell"
            else:
                print(b.text()+" is deselcted")       

        if b.text() == "Classical":
            if b.isChecked() == True:
                print(b.text()+" is selected")
                self.type_graph = "Classical"
            else:
                print(b.text()+" is deselcted")       
        
if __name__=='__main__':
    
    app= QtCore.QCoreApplication.instance()
    if app is None:    
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())
