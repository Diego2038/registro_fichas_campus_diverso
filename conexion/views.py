from app_registro.models import Persona, PertenenciaGrupoPoblacional
import gspread
from google.oauth2 import service_account
from django.shortcuts import render
from datetime import datetime as dt
from django.db import IntegrityError
from django.http import HttpResponse

def importar_desde_google_sheets(request):
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('./credentials.json', scopes=scopes)
    gc = gspread.authorize(credentials)

    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/12IdRTYfnPns-CAC4MOEpL0xNd71FC6w7C_ubTaJj-Ms/edit?usp=sharing'
    workbook = gc.open_by_url(spreadsheet_url)
    worksheet = workbook.worksheet('Solicitudes CD')

    data = worksheet.get_all_records()

    for row in data:
        fecha_nacimiento = row['Fecha de nacimiento']
        numero_documento = row['Número de identificación']

        try:
            fecha_nacimiento = dt.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        except ValueError: 
            fecha_nacimiento = None

        if not Persona.objects.filter(numero_documento=numero_documento).exists():
            persona = Persona(
                nombre_identitario=row['Nombre identitario'],
                nombre_y_apellido=row['First name'] + ' ' + row['Last name'],
                tipo_documento=row['Tipo de identificación'],
                numero_documento=row['Número de identificación'],
                fecha_nacimiento=fecha_nacimiento or dt.now(),  # Valor predeterminado para fecha de nacimiento
                estrato_socioeconomico=row['Estrato socioeconómico'],
                ciudad_nacimiento=row['Ciudad de nacimiento'],
                municipio_nacimiento=row['Ciudad de nacimiento'],
                corregimiento_nacimiento=row['Ciudad de nacimiento'],
                departamento_nacimiento=row['Departamento de nacimiento'],
                pais_nacimiento=row['País de nacimiento'],
                ciudad_residencia=row['Ciudad o municipio de residencia'],
                municipio_residencia=row['Ciudad o municipio de residencia'],
                corregimiento_residencia=row['Barrio de la residencia'],
                zona_residencial=row['Zona de residencia'],
                direccion_residencia=row['Address'],
                barrio_residencia=row['Barrio de la residencia'],
                comuna_barrio=row['Address'],
                telefono=row['Phone number'],
                estado_civil=row['Estado civil'],
                identidad_etnico_racial=row['Identidad Étnico-racial'],
                nombre_persona_de_confianza=row['Personas con las que vive'],
                relacion_persona_de_confianza=row['Personas con las que vive'],
                telefono_persona_de_confianza=row['Número de contacto de la persona de confianza para contactar'],
            )
            
            try:
                persona.save()
            except IntegrityError:
                pass

    return HttpResponse('Exitoso')
