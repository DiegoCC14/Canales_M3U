from .sql_modulo import SQL
from pathlib import Path
import os
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse

from Config.settings import BASE_DIR

def log_usuario( Tipo , page ):
	try:
		path_file_histori = BASE_DIR/"historial.txt"
		if os.path.exists( path_file_histori ) == False:
			with open( path_file_histori , 'w') as file:
				file.write( "" )

		with open( path_file_histori , 'r') as file:
			text_original = file.read()		
		with open( path_file_histori , 'w') as file:
			file.write( f"- {Tipo} {page}: " + str(datetime.now()) )
			file.write( "\n" + text_original )
	except:
		print("Error Log Usuario -->>")


class Canales_M3U( APIView ):

	def get( self , request ):
			
		try:
			
			sql_object = None

			try:		
				sql_object = SQL( BASE_DIR/'Canales_M3U.sqlite3' )
				resultado_sql = sql_object.consulta_sql( f"SELECT * FROM Canales_M3U WHERE cant_reintentos=0" )
				resultado = [ { "id":elem[0] , "name":elem[1] , "url":elem[2] } for elem in resultado_sql ]
			except:
				resultado = []
			finally:
				if sql_object != None:
					sql_object.cerrar_db() 
			
			log_usuario( "Canales Obtenidos" , "" )
			return Response( resultado )		
		except:
			return Response( [] )