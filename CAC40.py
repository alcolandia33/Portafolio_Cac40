
from tkinter import *
import pandas as pd
import pandas_datareader.data as pdr
import datetime as date
import pylab as plt
import numpy as np
from scipy.optimize import minimize
from pandastable import Table

enddate= date.datetime.now()

startdate= enddate - date.timedelta(days=365)

lista=['AC.PA','AIR.PA','ATO.PA','BNP.PA','EN.PA','CAP.PA','CA.PA','SGO.PA','ML.PA','ACA.PA','BN.PA','ENGI.PA','KER.PA','AI.PA','LR.PA','OR.PA','MC.PA','ORA.PA','RI.PA','UG.PA','SAN.PA','SU.PA','GLE.PA','SW.PA','FTI.PA','HO.PA','FP.PA','VIE.PA','DG.PA','VIV.PA','MT','CS.PA','DSY.PA','EL.PA','RMS.PA','PUB.PA','RNO.PA','SAF.PA','STM.PA','UL.VI']
#lista=['SAN.PA','SU.PA','GLE.PA','SW.PA','FTI.PA','HO.PA','FP.PA','VIE.PA','DG.PA','VIV.PA','MT','CS.PA','DSY.PA','EL.PA','RMS.PA','PUB.PA','RNO.PA','SAF.PA','STM.PA','UL.VI']
 
df2 = pdr.get_data_yahoo(lista,startdate,enddate)['Adj Close'] 



ref=0.0471
#rentabilidad de cada accion

dfrent = df2.pct_change().mean()*365

#reisgo de cada accion

dfdesv = ((df2.pct_change().std())*((252)**(1/2)))


# grafica riesgo-rentabilidad todas las acciones



#lista acciones dominates

dom=   pd.concat([dfdesv, dfrent],  axis=1, sort=False)



dom["lista"]=lista
dom.columns= ['Riesgo', 'Rentabilidad','Nombre',]
dom1= dom.sort_values('Riesgo')


rref=0
lacciones=[]



for i in dom1.index:
         
    if (dom1.loc[i,'Rentabilidad'] > 0 and  rref==0  ):
        
        rref=dom1.loc[i,'Rentabilidad']
        lacciones.append(i)
                     
    elif (dom1.loc[i,'Rentabilidad']>=rref) and dom1.loc[i,'Riesgo']<=0.4:
        rref=dom1.loc[i,'Rentabilidad']
        lacciones.append(i)
        


dom2=dom1.loc[lacciones]

dgd=dom2

dgd["Nombre"]=lacciones

wi=1/dom2.Riesgo.count() 
dom2["Wi"]=wi

 #tabla de covarianza
acambios = pdr.get_data_yahoo(lacciones,startdate,enddate)['Adj Close'].pct_change() 
m_cov= acambios.cov()


# riesgo de portafolio

riesgo_portafolio=(np.sqrt(np.dot(dom2['Wi'].T, np.dot(m_cov, dom2['Wi']))))*np.sqrt(252)
riesgo_portafolio
peso=dom2.Wi.values.tolist()


def get_ret_vol_sr(peso):
    ref
    peso = np.array(peso)
    ret = 1-((peso*dom2['Rentabilidad']).sum())
    vol = (np.sqrt(np.dot(peso.T, np.dot(m_cov, peso))))*np.sqrt(252)
    ret2= ((peso*dom2['Rentabilidad']).sum())
    shar= 20-((ret2-ref)/vol)
    return np.array([ret,vol,ret2,shar])
  
def check_sum(peso):
    #return 0 if sum of the weights is 1

    return np.sum(peso)-1

def max_rent(peso):
    
    return get_ret_vol_sr(peso)[0]
def min_riesgo(peso):
    
    return get_ret_vol_sr(peso)[1]

def max_sharpe(peso):
    
    return get_ret_vol_sr(peso)[3]




b1=[]
g1=[]
gv=1/dom2.Riesgo.count()
boun_gues=dom2.Wi.values.tolist()
for i in boun_gues:
    b1.append((0,1))
    g1.append(gv)
b1=tuple(b1)




def gac1():
	entiq = laccion.get(laccion.curselection())
	
	df2 = pdr.get_data_yahoo(entiq,startdate,enddate)['Adj Close'] 
	basea=[]
	baseb=[]
	for i in df2.index:
		basea.append(i)
		baseb.append(df2.loc[i])
	plt.plot(basea,baseb)
	plt.title('Datos historicos de '+entiq)
	plt.xlabel("Fecha")
	plt.ylabel('Precio de cierre') 
	plt.show()

def dat1():

	datos(df2)

def rra1():
	datos(dom1)



def datos(df):
	tabla= Toplevel(raiz)
	
	pt = Table(tabla,dataframe=df)
	pt.show()
def grra1():
	plt.scatter(dom1['Riesgo'], dom1['Rentabilidad'])
	plt.title('Riesgo Vs Rentabilidad de acciones')
	plt.xlabel("Riesgo")
	plt.ylabel('Rentabilidad') 
	plt.show()	

def dcac40():
	df2 = pdr.get_data_yahoo('^FCHI',startdate,enddate)['Adj Close'] 
	basea=[]
	baseb=[]
	for i in df2.index:
		basea.append(i)
		baseb.append(df2.loc[i])
	plt.plot(basea,baseb)
	plt.title('Datos historicos de CAC40')
	plt.xlabel("Fecha")
	plt.ylabel('Precio de cierre') 
	plt.show()  
	
def gafi1():
	plt.scatter(dom1['Riesgo'], dom1['Rentabilidad'])
	plt.scatter(dom2['Riesgo'], dom2['Rentabilidad'], c="red")
	plt.title('Gráfica de Dominancia')
	plt.xlabel("Riesgo")
	plt.ylabel('Rentabilidad') 
	plt.show()



	


def dafi1():
	dgd
	dgd2=dgd
	
	datos(dgd2)


datosFI=[]
nriesgo=[]

def froe1():
	
	nportafolios=int(npor.get())

	global datosFI
	global nriesgo
	if  maxmin.get(maxmin.curselection())=="" :
		messagebox.showinfo(message="Selecciones si va a maximizar o minizar", title="Datos incompletos")
	else:

		if nportafolios=="" and nportafolios.isdigit()==False and nportafolios<=0:
			messagebox.showinfo(message="digite un nuemro portafolios entero positivo", title="Datos incompletos")
		else:
			if maxmin.get(maxmin.curselection())=="Maximizando Rentabilidad":
				miin=0
				maax=0
				for i in [0,1]:
				    if i==0:
				        dado=0
				    else:
				        dado=2
				        
				    cons =({'type':'eq', 'fun':check_sum},
				     {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[1] - dado})
				    result = minimize( max_rent,g1,method='SLSQP', bounds=b1, constraints=cons)
				    kk=result['x']
				    if i==0:
				        miin=((np.sqrt(np.dot(kk.T, np.dot(m_cov, kk))))*np.sqrt(252))
				       
				    else:
				        maax=(np.sqrt(np.dot(kk.T, np.dot(m_cov, kk))))*np.sqrt(252)


				nportafolios=int(npor.get())        
				factor=(maax-miin)/(nportafolios -1)
				dadoriesgo=[maax]
				i=1
				while i <= nportafolios-1:
				    dadoriesgo.append(dadoriesgo[-1]-factor)
				    i += 1

				nriesgo1=[0]    
				datosFI1=[]
				for i in dadoriesgo:
				    dado=i

				    datos=[]  
				    cons =({'type':'eq', 'fun':check_sum},
				     {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[1] - dado})
				    result = minimize( max_rent,g1,method='SLSQP', bounds=b1, constraints=cons)
				    kk=result['x']
				    
				    datos.append(i)
				    nriesgo1.append(i)
				    datos.append(1-result['fun'])
				    for j in result['x']:
				        datos.append(j)
				    datosFI1.append( datos)
				datosFI=datosFI1
				nriesgo=nriesgo1
				tabfron()
			else:
				miin=0
				maax=0
				for i in [0,1]:
				    if i==0:
				        dado=0
				    else:
				        dado=2
				        
				    cons =({'type':'eq', 'fun':check_sum},
				     {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[2]- dado})
				    result = minimize( min_riesgo,g1,method='SLSQP', bounds=b1, constraints=cons)
				    kk=result['x']
				    if i==0:
				        miin=(((kk*dom2['Rentabilidad']).sum()))
				       
				    else:
				        maax=(((kk*dom2['Rentabilidad']).sum()))
				        


				nportafolios=int(npor.get())       
				factor=(maax-miin)/(nportafolios -1)
				dadoriesgo=[maax]
				i=1
				while i <= nportafolios -1:
				    dadoriesgo.append(dadoriesgo[-1]-factor)
				    i += 1
				datosFI1=[]
				nriesgo1=[0]
				for i in dadoriesgo:
				    dado=i
				    datos=[]  
				    cons =({'type':'eq', 'fun':check_sum},
				     {'type':'eq', 'fun':lambda w: get_ret_vol_sr(w)[2] - dado})
				    result = minimize( min_riesgo,g1,method='SLSQP', bounds=b1, constraints=cons)
				    kk=result['x']
				    datos.append(result['fun'])
				    nriesgo1.append(result['fun'])
				    datos.append((kk*dom2['Rentabilidad']).sum())
				    for o in result['x']:
				        datos.append(o)
				    datosFI1.append( datos)
				datosFI=datosFI1
				nriesgo=nriesgo1
				tabfron()

nombres=['Riesgo','Rentabilidad']
for i in dom2.index:
	nombres.append(i)

def tabfron():

	fro_efi=pd.DataFrame( datosFI)
	fro_efi.columns=[nombres]
	datos(fro_efi)			
	

def froe1g():
	fro_efi=pd.DataFrame( datosFI)
	fro_efi.columns=[nombres]

	plt.scatter(fro_efi[['Riesgo']], fro_efi[['Rentabilidad']])
	plt.title('Frontera eficente'+maxmin.get(maxmin.curselection()))
	plt.xlabel("riesgo")
	plt.ylabel('rentablidad') 
	plt.show()  
	
optimo=pd.DataFrame()
def porop1():
	global optimo
	ref
	cons =({'type':'eq', 'fun':check_sum})
	optimo1=[]
	result = minimize( max_sharpe,g1,method='SLSQP', bounds=b1, constraints=cons)
	kk=20-result['fun'] 
	x=result['x']
	optimo1.append((np.sqrt(np.dot(x.T, np.dot(m_cov, x))))*np.sqrt(252))
	optimo1.append((x*dom2['Rentabilidad']).sum())
	for o in result['x']:
	    optimo1.append(o)
	optimo1=pd.DataFrame( optimo1)
	optimo1.index=[nombres]
	optimo=optimo1
	
	datos(optimo)

def porop1g():
	
	fro_efi=pd.DataFrame( datosFI)
	fro_efi.columns=[nombres]
	

	plt.title('Portafolio optimo')
	plt.xlabel('Riesgo')
	plt.ylabel('Rentabilidad')

	plt.scatter(fro_efi[['Riesgo']], fro_efi[['Rentabilidad']],s=10)
	plt.scatter(optimo.loc['Riesgo'], optimo.loc['Rentabilidad'],c='red',s=100)
	plt.show()

def lmc1():
	ref

	re=[]
	for i in nriesgo:
	    v=ref+(((optimo.loc['Rentabilidad'].sum()-ref)/optimo.loc['Riesgo'].sum())*i)
	    re.append(v)
	re=pd.DataFrame(re)
	re.columns=['Re']
	datos(re)

	

	
def lmc1g():
	ref
	fro_efi=pd.DataFrame( datosFI)
	fro_efi.columns=[nombres]


	re=[]
	for i in nriesgo:
	    v=ref+(((optimo.loc['Rentabilidad'].sum()-ref)/optimo.loc['Riesgo'].sum())*i)
	    re.append(v)
	re=pd.DataFrame(re)
	re
	plt.title('Línea del Mercado de Capitales')
	plt.xlabel('Riesgo')
	plt.ylabel('Rentabilidad')

	

	plt.scatter(fro_efi[['Riesgo']], fro_efi[['Rentabilidad']],c='red',s=1)
	plt.plot(nriesgo, re)
	plt.show()


acambios1 = pdr.get_data_yahoo(lacciones,startdate,enddate)['Adj Close'].pct_change() 
indice= pdr.get_data_yahoo('^FCHI',startdate,enddate)['Adj Close'] 
indchange = indice.pct_change() 
indmean =((1+indice.pct_change().mean())**252)-1
indvol = (indice.pct_change().std())*((252)**(1/2))

acambios1["indice"]=indice.pct_change() 
i_cov= acambios1.cov()
Req=[]
def lmv1():
	beta=[]
	ref
	for i in dom2.index:
	    b= i_cov.iloc[-1].loc[i]
	  
	    b = (b*252)/(indvol)
	    beta.append(b)


	dom2['Beta']=beta
	global Req
	Req=[]
	for i in dom2.index:
	    
	    rq= ref+(dom2.loc[i,'Beta']*(indmean-ref))
	    Req.append(rq)


	dom2['ReQ']=Req
	lmvv=dom2
	
	datos(lmvv)

def lmv1g():
	plt.scatter(dom2['Beta'], dom2['Rentabilidad'], c="red")
	plt.scatter(dom2['Beta'], dom2['ReQ'], c="blue")
	plt.plot(dom2['Beta'], dom2['ReQ'])
	plt.title('Línea del Mercado de Capitales')
	plt.xlabel('Beta')
	plt.ylabel('Rentabilidad')
	plt.show()



raiz= Tk()

raiz.title("PORTAFOLIO CON CAC40")
raiz.iconbitmap("banderaico.ico")
raiz.config(bg="cyan2")
raiz.geometry("1200x800")
raiz.resizable(0,0)




Label(raiz,text="Fecha de recopilacion de datos:",bg="cyan2" ,fg="black",font=("Loma",15)).grid(row=0,column=0,columnspan=4,sticky=W)
fechaaa=Label(raiz,text=startdate, fg="black",font=("Loma",15),bg="cyan2" ).grid(row=0,column=4,columnspan=3,sticky=E)

Label(raiz,text="Componentes de CAC40", bg="azure",fg="black",font=("Loma",15)).grid(row=1,column=0,columnspan=2, sticky=S+N+E+W)

laccion=Listbox(raiz,width=60, height= 18,bg="cornsilk2")
laccion.insert(0,*lista)
laccion.grid(row=2,column=0,columnspan=2)
scrollbar = Scrollbar(raiz,width=10,command=laccion.yview)
scrollbar.grid(row=2,column=2,sticky="nsew")

gac=Button(raiz, text="Ver grafico de accion seleccionada",font=("Loma",10),bg= "thistle1",command=gac1,fg="black",width=25)
gac.grid(row=3,column=0)

dat=Button(raiz, text="Datos de las acciones",font=("Loma",10),bg= "thistle1",command=dat1,fg="black",width=20)
dat.grid(row=3,column=1)

rra=Button(raiz, text="Rentabilidad y riesgo de acciones",font=("Loma",10),bg= "thistle1",command=rra1,fg="black",width=25)
rra.grid(row=4,column=0)

grra=Button(raiz, text="Grafico riesgo vs rentabilidad" ,font=("Loma",10),bg= "thistle1",command=grra1,fg="black",width=20)
grra.grid(row=4,column=1)

Label(raiz, text="Portafolio con el indice CAC40", width=35,justify="center", fg="red4",bg="gold2",font=("Loma",15)).grid(row=1,column=3,columnspan=2,sticky=S+N+E+W)
texto = Label(raiz,justify="center",bg="cyan2", fg="black",font=("Loma",15) ,text="En este programa ofrece la \ncapacidada de observar los \ncomponentes del CAC40, asi \ncomo el desarrollo de un Portafolio \neficiente con el metodo de  Markowitz, \ntodos los datos son extraidos de\nYahoo Finance en tiempo real ")
texto.grid(row=2,column=3,columnspan=2,padx=5,sticky=S+N+E+W)
Button(raiz, text="CAC40 Gráfico",font=("Loma",10),bg= "thistle1",fg="black" ,command= dcac40).grid(  row=3, column=3,columnspan=2)


Label(raiz,text="Acciones dominantes", fg="black",font=("Loma",15)).grid(row=1,column=5,columnspan=2,sticky=S+N+E+W)
accdom=Listbox(raiz, width=60,height= 18,bg="cornsilk2")
accdom.insert(0,*lacciones)
accdom.grid(row=2,column=5,columnspan=2)

gafi=Button(raiz, text="Gráfico de dominancia",font=("Loma",10),bg= "thistle1",command=gafi1,fg="black", width=20)
gafi.grid(row=3,column=5)

dafi=Button(raiz, text="Rentabilidad y riesgo",font=("Loma",10),bg= "thistle1",command=dafi1,fg="black", width=20)
dafi.grid(row=3,column=6)

Label(raiz,text="Numero de Portafolios: ",bg="cyan2", fg="black",font=("Loma",15)).grid(row=4,column=3,padx=5)
npor= Entry(raiz)
npor.grid(row=4,column=4)

maxmin=Listbox(raiz, width=30,height= 2,bg="cornsilk2",font=("Loma",15))
maxmin.insert(0,"Maximizando Rentabilidad")
maxmin.insert(1,"Minimizando Riesgo")
maxmin.grid(row=5,column=3,padx=5,columnspan=2)


froe=Button(raiz, text="Frontera eficiente",font=("Loma",15),bg= "thistle1",command=froe1,fg="black",width=20)
froe.grid(row=6,column=3,padx=5,sticky=E)
froeg=Button(raiz, text="Gráfico",font=("Loma",15),bg= "thistle1",command=froe1g,fg="black")
froeg.grid(row=6,column=4,sticky=W)

porop=Button(raiz, text="Portafolio óptimo",font=("Loma",15),bg= "thistle1",command=porop1,fg="black",width=20)
porop.grid(row=7,column=3,padx=5,sticky=E)
poropg=Button(raiz, text="Gráfico",font=("Loma",15),bg= "thistle1",command=porop1g,fg="black")
poropg.grid(row=7,column=4,sticky=W)

lmc=Button(raiz, text="Línea de Mercado de Capitales ",font=("Loma",13),bg= "thistle1",command=lmc1,fg="black",width=25)
lmc.grid(row=8,column=3,padx=5,sticky=E)
lmcg=Button(raiz, text="Gráfico ",font=("Loma",15),bg= "thistle1",command=lmc1g,fg="black")
lmcg.grid(row=8,column=4,padx=5,sticky=W)

lmv=Button(raiz, text="Línea del Mercado de Valores",font=("Loma",13),bg= "thistle1",command=lmv1,fg="black",width=25)
lmv.grid(row=9,column=3,padx=5,sticky=E)
lmvg=Button(raiz, text="Gráfico",font=("Loma",15),bg= "thistle1",command=lmv1g,fg="black")
lmvg.grid(row=9,column=4,padx=5,sticky=W)


bolsa=PhotoImage(file="bolsa.png",master=raiz)
bolsaa =Label(raiz, image=bolsa)
bolsaa.grid(row=5,column=0,rowspan=7,columnspan=3)

bbander=PhotoImage(file="bandera.png",master=raiz)
bandera=Label(raiz, image=bbander)
bandera.grid(row=4,column=5,rowspan=8,columnspan=2)




raiz.mainloop()









