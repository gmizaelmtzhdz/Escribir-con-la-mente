# -*- encoding: utf-8 -*-
'''
  
  Created on: 2015
  Author: Mizael Martinez

'''
import MySQLdb
class BaseDatos:
	def __init__(self):
		self.__host="127.0.0.1"
		self.__usuario="root"
		self.__contrasena=""
		self.__baseDatos="red"
		self.__conexion=None
		self.__cursor=None
		self.__query=""

	def setHost(self,host):
		self.__host=host
	def setUsuario(self,usuario):
		self.__usuario=usuario
	def setContrasena(self,contrasena):
		self.__contrasena=contrasena
	def setBaseDatos(self,baseDatos):
		self.__baseDatos=baseDatos
	def setQuery(self,query):
		self.__query=query


	def getHost(self):
		return self.__host
	def getUsuario(self):
		return self.__usuario
	def getContrasena(self):
		return self.__contrasena
	def getBaseDatos(self):
		return self.__baseDatos
	def getQuery(self):
		return self.__query	

	def conectar(self):
		self.__conexion=MySQLdb.connect(*[self.__host,self.__usuario,self.__contrasena,self.__baseDatos])
	def consultaGenerica(self,query):
		self.conectar()
		self.__cursor=self.__conexion.cursor()
		self.__cursor.execute(query)
		datos=self.__cursor.fetchall()
		self.__cursor.close()
		self.__conexion.commit()
		self.__conexion.close()
		return datos

	#Login
	def agregarUsuario(self,nick):
		query="INSERT INTO usuario(nick) VALUES('%s')"%nick
		self.consultaGenerica(query)
		return self.obtenerIdUsuario(nick)

	def obtenerIdUsuario(self,nick):
		query="SELECT id_usuario FROM usuario WHERE nick='%s' ORDER BY id_usuario DESC LIMIT 0,1"%nick
		resultado=self.consultaGenerica(query)
		return resultado[0][0]

	def cuantosHay(self,tabla,campo,valor):
		query="SELECT COUNT(*) FROM %s WHERE %s='%s'"%(tabla,campo,valor)
		resultado=self.consultaGenerica(query)
		return resultado[0][0]

	def insertarStreamOndas(self,datos):
		query="INSERT INTO ondas(delta,tetha,lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma,meditacion,atencion,fk_id_letras, fk_id_usuario,ruido) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(str(datos["delta"]),str(datos["tetha"]),str(datos["lowAlpha"]),str(datos["highAlpha"]),str(datos["lowBeta"]),str(datos["highBeta"]),str(datos["lowGamma"]),str(datos["midGamma"]),str(datos["meditacion"]),str(datos["atencion"]),str(datos["id_letras"]),str(datos["id_usuario"]),str(datos["ruido"]))
		self.consultaGenerica(query)
		return

	#Letras
	def obtenerLetras(self):
		query="SELECT * FROM letras"
		resultado=self.consultaGenerica(query)
		diccionario={}
		for i in resultado:
			diccionario.update({i[1]:i[0]})
		return diccionario

	#Entrenamiento
	def agregarEntrenamiento(self,datos):
		query="INSERT INTO entrenamiento(numerodeneuronas,error,tipo) VALUES (%s,%s,'%s')"%(str(datos["numerodeneuronas"]),str(datos["error"]),str(datos["tipo"]))
		self.consultaGenerica(query)
		return self.obtenerUltimoRegistroEntrenamiento()

	def obtenerUltimoRegistroEntrenamiento(self):
		query="SELECT id_entrenamiento FROM entrenamiento ORDER BY id_entrenamiento DESC LIMIT 0,1"
		resultado=self.consultaGenerica(query)
		return resultado[0][0]
		
	def actualizarRegistroEntrenamiento(self,url,id):
		query="UPDATE entrenamiento SET url='%s' WHERE id_entrenamiento=%s"%(url,id)		
		self.consultaGenerica(query)
		return 
	#Lectura/Escritura Archivo
	def obtenerRegistrosOndas(self):
		#query="SELECT * FROM entrenamiento_prueba"
		query="SELECT * FROM entrenamiento_prueba LIMIT 0, 5839"
		#query="SELECT * FROM entrenamiento_prueba LIMIT 0, x" x limite excluyente
		return self.consultaGenerica(query)

	def obtenerRegistrosOndasPruebaDeLaRedNeuronal(self):
		#query="SELECT * FROM entrenamiento_prueba"
		query="SELECT * FROM entrenamiento_prueba LIMIT 5839,1459"
		#query="SELECT * FROM entrenamiento_prueba LIMIT 0, x" x limite excluyente
		return self.consultaGenerica(query)


	def obtenerRegistrosOndasGamma(self):
		#query="SELECT lowGamma,midGamma,valor FROM entrenamiento_prueba_gamma"
		query="SELECT lowGamma,midGamma,valor FROM entrenamiento_prueba_gamma LIMIT 0, 5839"
		return self.consultaGenerica(query)
	def obtenerRegistrosOndasGammaNormalizado(self):
		#query="SELECT lowGamma,midGamma,valor FROM entrenamiento_prueba_gamma"
		query="SELECT lowgamma,midgamma,valor FROM entrenamiento_prueba_normalizado LIMIT 0,5839"
		return self.consultaGenerica(query)

	def obtenerRegistrosOndasPruebaDeLaRedNeuronalGamma(self):
		#query="SELECT * FROM entrenamiento_prueba_gamma"
		query="SELECT * FROM entrenamiento_prueba_gamma LIMIT 5839,1459"
		#query="SELECT * FROM entrenamiento_prueba LIMIT 0, x" x limite excluyente
		return self.consultaGenerica(query)

	def obtenerRegistrosOndasNormalizados(self):
		#query="SELECT * FROM entrenamiento_prueba"
		query="SELECT * FROM entrenamiento_prueba_normalizado LIMIT 0, 5839"
		#query="SELECT * FROM entrenamiento_prueba LIMIT 0, x" x limite excluyente
		return self.consultaGenerica(query)
	def obtenerRegistrosOndasPruebaDeLaRedNeuronalNormalizados(self):
		#query="SELECT * FROM entrenamiento_prueba"
		query="SELECT * FROM entrenamiento_prueba_normalizado LIMIT 5839,1459"
		#query="SELECT * FROM entrenamiento_prueba LIMIT 0, x" x limite excluyente
		return self.consultaGenerica(query)

	#Probando la aplicacion convirtiendo senales => Letras
	def obtenerArchivoErrorMinimo(self):
		query="SELECT MIN(error), url FROM entrenamiento"
		return self.consultaGenerica(query)[0][1]
	def obtenerArchivoErrorMinimoNormalizado(self):
		query="SELECT MIN(error), url FROM entrenamiento WHERE tipo='normalizado'"
		return self.consultaGenerica(query)[0][1] 
	def obtenerLetrasValor(self):
		query="SELECT * FROM letras"
		resultado=self.consultaGenerica(query)
		diccionario={}
		for i in resultado:
			diccionario.update({i[1]:i[2]})
		return diccionario
	#Probando la red neuronal, checando con otros valores
	def obtenerErroresMenoresDeEntrenamiento(self):
		query="SELECT numerodeneuronas,error,url FROM entrenamiento WHERE tipo='total' ORDER BY error ASC LIMIT 5"
		return self.consultaGenerica(query)
	def obtenerErroresMenoresDeEntrenamientoGamma(self):
		query="SELECT numerodeneuronas,error,url FROM entrenamiento WHERE tipo='gamma' ORDER BY error ASC LIMIT 5"
		return self.consultaGenerica(query)
	def obtenerErroresMenoresDeEntrenamientoNormalizado(self):
		query="SELECT numerodeneuronas,error,url FROM entrenamiento WHERE tipo='normalizado' ORDER BY error ASC LIMIT 5"
		return self.consultaGenerica(query)

	def auxiliarOndasNormalizadas(self):
		query="SELECT * FROM entrenamiento_prueba_normalizado LIMIT 0, 50"
		return self.consultaGenerica(query)
'''
datos={"numerodeneuronas":1,"error":1,"url":"url","id_letras":1}
db=BaseDatos()
print db.obtenerUltimoRegistroEntrenamiento()
db.actualizarRegistroEntrenamiento("modificacion",1)
'''
#db=BaseDatos()
#print db.obtenerRegistrosOndasPruebaDeLaRedNeuronalGamma()
#print db.obtenerLetrasValor()
#print db.obtenerArchivoErrorMinimo()
#print type(db.obtenerArchivoErrorMinimo())
