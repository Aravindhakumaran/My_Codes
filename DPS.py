import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mainwindow
import pandas as pd
import numpy as np
import csv

def clickable(widget):

    class Filter(QObject):
    
        clicked = pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

def hovered(widget):

    class Filter(QObject):
    
        hover = pyqtSignal()
        
        def eventFilter(self, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.QEvent.HoverMove:
                    if obj.rect().contains(event.pos()):
                        self.hover.emit()
                        
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.hover

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_symptoms()
        self.pressed=False
        # self.event=QtGui.QMouseEvent()
        global count,cnt,url,nm 
        nm=0
        cnt=1
        count=10
        
        self.stack=QtGui.QHBoxLayout(self.ui.scrollAreaWidgetContents)
        self.ui.selct_btn.clicked.connect(self.mvlist2)
        self.ui.deselct_btn.clicked.connect(self.mvlist1)
        self.ui.predictButton.clicked.connect(self.predict)
        self.ui.pushButton.clicked.connect(self.hidden)
        #clickable(self.ui.scrollArea).connect(self.openWeb)
    
    def list_symptoms(self):
      global df
      df=pd.read_csv('dataset_clean.csv')
      list=df['Target'].values
      from collections import Counter
      c=Counter(list)
      c=c.items()
      #print c
      df1=pd.DataFrame(c)
      df1=df1.sort_values(by=[1],ascending=[False])
      #print df1
      list1=df1[0].values.tolist()
      #list=sorted(list,key=str.lower)
      for item in list1:
          self.ui.symp_List.addItem(str(item).title())

    def mvlist1(self):
        self.ui.symp_List.addItem(self.ui.sel_Symp_List.currentItem().text())
        self.ui.sel_Symp_List.takeItem(self.ui.sel_Symp_List.currentIndex().row())

    def mvlist2(self):
        self.ui.sel_Symp_List.addItem(self.ui.symp_List.currentItem().text())
        self.ui.symp_List.takeItem(self.ui.symp_List.currentIndex().row())

    # def mousePressEvent(self.event):
    #     e=self.event
    #     if 

    def extract(self,data):
        dis=data['Disease'].values
        from collections import Counter
        dis1=Counter(dis)
        dis1=dis1.items()
        #print(dis1)
        gdf=pd.DataFrame(dis1,columns=["Disease","Count"])
        gdf=gdf.sort_values(by=['Count'],ascending=[False])
        gdf=gdf['Disease'].values.tolist()

        #print(gdf)
        r1=[]
        for i in gdf:
            re=data.loc[data['Disease']==i]
            re1=re['Accuracy'].values.mean()
            max_C=re.sort_values(by=['Accuracy'],ascending=[False])
            max_A=re['Accuracy'].values.max()
            max_C=max_C.loc[max_C['Accuracy']==max_A]
            max_C=max_C['Cluster'].values
            try:
                des = int(max_C[0])
            except IndexError:
                des = int(max_C)
            #max_C=max_C.ix[0]
            # print("---------------------------------------------------------------")
            # print(i)
            # print("---------------------------------------------------------------")
            # print(max_A)
            # print(des)
            # print("---------------------------------------------------------------")
            r1.append((i,int(re1),des))
        #print(r1)

        rr=[]
        for cclass in range(data['Cluster'].values.max()+1):
            data1=data.ix[data['Cluster']==cclass]
            l=data1['True Positive Rate'].values
            try:
                l=sum(l) / float(len(l))
            except ZeroDivisionError:
                l=0
            rr.append((cclass,l))
        re=pd.DataFrame(r1,columns=["Disease","Accuracy","Best_Cluster"])
        
        rep=Counter(re['Best_Cluster'].values.tolist())
        rep=rep.items()
        rep=pd.DataFrame(rep,columns=["Cluster","Count"])
        rep1=rep['Count'].values.max()
        rep=rep[rep['Count']==rep1]
        rep=rep['Cluster'].values
        #print(rep)
        re_r=pd.DataFrame()
        try:
            
            for i in rep:
                re=re[re['Best_Cluster']==int(i)]
                re_r=pd.concat([re_r,re],axis=0)
        except TypeError:
            re_r=re[re['Best_Cluster']==int(rep)]
        #print(re_r)
        return re_r        

        # for i ,j in dis:
        #     ex_df1=data.loc[data['Disease'] == str(i)]
        # print ex_df1
        #data_e=pd.DataFrame(lst_e,columns=["Disease","Percent","Cluster"])

    
    def txtreturn(self,text):
        global t,ddf
        # return url
        t=ddf.loc[ddf['Frame'] == str(text),'Disease'].item()
        df3=pd.read_csv('disease.csv')
        url1=df3.loc[df3['Source'] == str(t), 'Link'].item()
        self.openWeb(url1)
        self.qrcode(t)
        #print t
        return t


    def hidden(self):
        self.setFixedSize(720,500)

    def openWeb(self,url):        
        from PyQt4.QtCore import QUrl       
        #print url      
        self.setFixedSize(1310,500)
        self.ui.webView.load(QUrl(url))
        #self.ui.lineEdit.setText("")
        
    def qrcode(self,name):
        self.ui.image.setStyleSheet("border-image: url('img/"+str(name)+".png');")


    def label(self,text,level,percent):
        from PyQt4.QtCore import QObject, SIGNAL
        global count,cnt,nm,ddf,lss
        frame = QtGui.QFrame()
        #frame.setObjectName(QString("frame"+str(cnt))
        frame.setGeometry(QtCore.QRect(count, 25, 201, 101))
        
        if(level=="extreme"):
            frame.setStyleSheet("background-color: rgb(170, 0, 0);\nborder:0.5px solid;\nborder-radius: 5px;\nborder-color: qlineargradient(spread:pad, x1:0.519, y1:0, x2:0.531, y2:1, stop:0.0225989 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));")
        if(level=="high"):
            frame.setStyleSheet("background-color: rgb(255, 96, 0);\nborder:0.5px solid;\nborder-radius: 5px;\nborder-color: qlineargradient(spread:pad, x1:0.519, y1:0, x2:0.531, y2:1, stop:0.0225989 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));")
        if(level=="low"):
            frame.setStyleSheet("background-color: rgb(0, 197, 0);\nborder:0.5px solid;\nborder-radius: 5px;\nborder-color: qlineargradient(spread:pad, x1:0.519, y1:0, x2:0.531, y2:1, stop:0.0225989 rgba(164, 164, 164, 255), stop:1 rgba(255, 255, 255, 255));")	  
        #frame.setStyleSheet("background-color: rgb(255, 0, 0);")
        #frame.setFrameShape(QtGui.QFrame.StyledPanel)
    
        lbl = QtGui.QLabel(frame)
        lbl.setGeometry(QtCore.QRect(2, 5, 196, 61))
        lbl.setWordWrap(True)
        lbl.setStyleSheet("font: 14pt \"Segoe UI\";\nborder:none;")
        lbl.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        lbl.setText(text.title())
        lbl_2 = QtGui.QLabel(frame)
        lbl_2.setGeometry(QtCore.QRect(20, 55, 69, 41))
        lbl_2.setStyleSheet("font: 75 28pt \"Segoe UI\";\nborder:none;")
        lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        st=str(percent)
        st+="%"
        lbl_2.setText(st)
        count=count+210
        self.stack.addChildWidget(frame)
        frame.setMouseTracking(True)
        effect=QtGui.QGraphicsDropShadowEffect()
        effect.setBlurRadius(50)
        frame.setGraphicsEffect(effect)
        frame.setObjectName(str("Frame"+str(nm)))       
        lss.append((str("Frame"+str(nm)),text))
        clickable(frame).connect(lambda: self.txtreturn(str(frame.objectName())))            
        cnt=cnt+1
        nm=nm+1
        #frame.mouseMoveEvent=
    
    def addSublabel(self,text,xaxis):
        
        label=QtGui.QLabel()
        label.setText(text)
        label.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        label.setGeometry(QtCore.QRect(xaxis, 0, (count-20), 20))
        label.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.588, fx:0.5, fy:0.5, stop:0 rgba(117, 117, 117, 255), stop:1 rgba(142, 142, 142, 255));")
        self.stack.addChildWidget(label)
    
    def addLine(self,xaxis,height):
        ln = QtGui.QFrame()
        ln.setGeometry(QtCore.QRect(xaxis, 0, 6, height))
        ln.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.534, x2:1, y2:0.534, stop:0 rgba(112, 112, 112, 255), stop:1 rgba(215, 215, 215, 255));")
        self.stack.addChildWidget(ln)
        
    def classifier(self,df_class,classified_data):
        from sklearn.cross_validation import train_test_split
      # To model the Gaussian Navie Bayes classifier
        from sklearn.naive_bayes import GaussianNB
      # To calculate the accuracy score of the model
        from sklearn.metrics import accuracy_score 
        from sklearn.metrics import confusion_matrix
        cluster,accr,tpr,fpr,omit,dtr,fnr,ii=[],[],[],[],[],[],[],[]
        for cclass in range(classified_data.max()+1):
            data=df_class.copy()
            data=data.loc[df_class['Class'] == cclass]
            dummies = pd.get_dummies(data['Target']).rename(columns=lambda x: "Target=" + str(x))
            features = dummies
            classes=np.unique(features)
            from collections import Counter
            disease_names=Counter(data['Source'].values)
            disease_names=disease_names.items()
            disease_names=pd.DataFrame(disease_names)
            # print("Cluster "+str(cclass))
            # print(disease_names)
            disease_names=disease_names[0].values.tolist()
            target = pd.get_dummies(data['Source']).rename(columns=lambda x: "Source=" + str(x))
            target=pd.concat([target,dummies],axis=1)
            target_train, target_test,features_train, features_test = train_test_split(target,features,test_size = 0.33, random_state = 10)
            result_clf=pd.DataFrame()
            k=0
            # print("Length of Features_Train"+str(len(features_train)))
            # print("Target Train")
            # print(target_train)
            # print("Target Test")
            # print(target_test)
            for i in disease_names:
                try:
                    clf = GaussianNB()
                    lst1=[row[k] for row in target_train.values]
                    # print("List 1")
                    # print(lst1)
                    lst2=[row[k] for row in target_test.values]
                    # print("List 2")
                    # print(lst2)
                    # print("Length of Lst1 "+str(len(lst1)))
                    # print("Length of Lst2 "+str(len(lst2)))
                    clf.fit(features_train.values,lst1)
                    target_pred = clf.predict(features_test.values)
                    acc=accuracy_score(lst2, target_pred, normalize = True)
                    # print("Prediction")
                    # print(target_pred)
                    # print("Accuracy_Rate :"+str(acc))
                    accr.append(acc*100)
                    matrix=confusion_matrix(lst2, target_pred, classes)
                    # print("Confusion Matrix")
                    # print(matrix)
                    FP = np.sum(matrix, axis=0) - np.diag(matrix)
                    FN = np.sum(matrix,axis=1) - np.diag(matrix)
                    TP = np.diag(matrix)
                    TN = np.sum(matrix) - (FP + FN + TP)
                    # Sensitivity, hit rate, recall, or true positive rate
                    TPR = TP/(TP+FN)
                    # Specificity or true negative rate
                    TNR = TN/(TN+FP)
                    # Precision or positive predictive value
                    PPV = TP/(TP+FP)
                            # Negative predictive value
                    NPV = TN/(TN+FN)
                            # Fall out or false positive rate
                    FPR = FP/(FP+TN)
                            # False negative rate
                    FNR = FN/(TP+FN)
                    # False discovery rate
                    FDR = FP/(TP+FP)
                    DR = TP/ (TP+TN)
                    # print("Detection Rate")
                    # print(DR.mean()*100)
                    dtr.append(DR.mean()*100)
                    # print("True Positive Rate :")
                    # print(TPR.mean())
                    tpr.append(TPR.mean()*100)
                    # print("False Positive Rate :")
                    # print(FPR.mean())            
                    fpr.append(FPR.mean()*100)
                    # print("False Negative Rate :")
                    # print(FNR.mean())
                    fnr.append(FNR.mean()*100)
                    cluster.append(cclass)
                    ii.append(i)
                    # print("valueof K is "+str(k))
                    # k=k+1
                
                except ValueError:
                    print("No Sample Data Found the Disease "+i+" is removed from the operation")
                    k=k+1
            
        f = pd.DataFrame()
        f['Cluster']=pd.Series(cluster)
        f['Disease']=pd.Series(ii)
        f['Accuracy']=pd.Series(accr)
        f['True Positive Rate']=pd.Series(tpr)
        f['False Positive Rate']=pd.Series(fpr)
        f['Detection Rate']=pd.Series(dtr)
        return f
    
    def makePercent(self,c1,c2):
        lt=[]
        for i,j in c1:
            for l,k in c2:
                if(l==i):
                    percent=(float(j)/float(k))*100
                    percent=int(percent)
                    # print(k,j)
                    # print(l,percent)
                    if(percent<40):
                        serious="low"
                    if(percent>40):
                        serious="high"
                    if(percent>60):
                        serious="extreme"
                    if(percent>15):
                        lt.append((i,serious,percent))
        return lt
      
   # def makepercent1(self,dataf):
        


    def predict(self):
        global df
        global count
        kg=float(self.ui.kg.text())
        pound=kg*2.20462
        pound=int(round(pound))
        # print("Pound")
        # print(pound)
        list=[]
        for c in range(self.ui.sel_Symp_List.count()):
            list.append(str(self.ui.sel_Symp_List.item(c).text().toLower()))
        # print(list)
        diseas=df['Source'].values
        from collections import Counter
        x=Counter(diseas)
        x=x.items()
        # print(x)
        df1=df[df['Target'].isin(list)]
        # print(df1)

        #clustering starts
        global km_df
        km_df=pd.DataFrame(df1.values,columns=['Source','Target','Weight'])
        #km_df['Weight']=pd.to_numeric(km_df['Weight'])
        
        km_df1=km_df.copy()
        del km_df['Weight']
        for y in km_df.columns:
            c=str(km_df[y].dtype)
            # print(c)
            if(c=="object"):
	      dummies = pd.get_dummies(km_df[y]).rename(columns=lambda x: y+ "=" + str(x))
              km_df = pd.concat([km_df, dummies], axis=1)
              del km_df[y]
        #print(km_df)
                
        from sklearn.cluster import KMeans
        km = KMeans(n_clusters=5,init='k-means++', n_init=70, algorithm='auto')
        rst = km.fit(km_df)
        centroids = rst.cluster_centers_
        #clu=rst.transform(df)
        
        labels = rst.labels_
        #km_df['Class']=pd.Series(labels,index=km_df.index)
        km_df1['Class']=pd.Series(labels,index=km_df.index)
        #km_df=km_df.idxmax(axis=1)
        # print(km_df1)
        accuracy_matrix=self.classifier(km_df1,labels)
        #print(accuracy_matrix)
        #exc=self.extract(accuracy_matrix)
        exc=self.extract(accuracy_matrix)
        print exc
        dises=df1['Source'].values
        z=Counter(dises)
        z=z.items()
        lst=pd.DataFrame({'Weight':df1['Weight'].unique()})
        # print(lst)
        sel_Pound=lst.ix[(lst['Weight']-pound).abs().argsort()[:2]]
        sel_Pound=sel_Pound['Weight'].tolist()
        # print(sel_Pound)
        df2=df1[df1['Weight'].isin(sel_Pound)]
        # print("Selected Prediction")
        # print(df2)
        disease=df2['Source'].values
        c=Counter(disease)
        c=c.items()
        # print(c)
        global ddf,lss
        lss=[]        
        cnt=0
        percent=0
        serious=""
        t="As per Weight"
        cn=count
        lt=self.makePercent(c,x)

        pr_df=pd.DataFrame(lt,columns=["Disease","Serious","Percent"])
        pr_df=pr_df.sort_values("Percent",ascending=False)
        # print(pr_df)
        for i,j,k in pr_df.values:
            self.label(i,j,k)
        # print(count)
        self.addLine(count,self.ui.scrollAreaWidgetContents.height())
        count+=10
        self.ui.scrollAreaWidgetContents.resize(count,self.ui.scrollAreaWidgetContents.height())
        self.addSublabel(t,cn)
        ls=self.makePercent(z,x)
        lz=[]
        for i,j,k in ls:
            for f in exc['Disease'].values:
                        
                if i==f:
                    lz.append((i,j,k))

        pr_df1=pd.DataFrame(lz,columns=["Disease","Serious","Percent"])
        pr_df1=pr_df1.sort_values("Percent",ascending=False)
        # print(pr_df1)
        q="As Per Symptoms"
        cn=count
        for i,j,k in pr_df1.values:
            self.label(i,j,k)
        self.addSublabel(q,cn)
        # print(count)
        # print("Finished Prediction")
        self.ui.scrollAreaWidgetContents.resize(count,self.ui.scrollAreaWidgetContents.height())
        # print("Finished Prediction")
        ddf=pd.DataFrame(lss,columns=["Frame","Disease"])
        # print ddf 
        self.setFixedSize(720,500)

app= QtGui.QApplication(sys.argv)
my_mainWindow = MainWindow()
#my_mainWindow.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
my_mainWindow.setFixedSize(720,350)
my_mainWindow.show()
sys.exit(app.exec_())
