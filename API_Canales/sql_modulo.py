import sqlite3

class SQL:

	conn = None
	cursor = None

	def __init__( self , dir_SQLITE3 ):
		self.connect_db( dir_SQLITE3 )
		self.cursor = self.conn.cursor()
		
	def connect_db( self , dir_SQLITE3 ):
		self.conn = sqlite3.connect( dir_SQLITE3 )

	def cerrar_db( self ):
		self.conn.close()

	def consulta_sql( self , query ):
		self.cursor.execute( query )
		try:
			self.conn.commit()
		except:
			pass
		return self.cursor.fetchall()
		
if __name__ == "__main__":
	obj_sql = SQL( "D:/Proyectos_Particulares/Lista/Django_Lista/DB_Videos.sqlite3" )
	resultado = obj_sql.consulta_sql("SELECT * , MAX(Historial_Video.fecha_crecion) FROM Videos INNER JOIN Historial_Video ON Historial_Video.id_video=Videos.id GROUP BY Videos.id ORDER BY views DESC")
	print( resultado[0] )
	print( resultado[1] )
	print( resultado[2] )
	obj_sql.cerrar_db()