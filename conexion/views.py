
from app_registro.models import Persona, PertenenciaGrupoPoblacional
import gspread
from google.oauth2 import service_account
from django.shortcuts import render
from datetime import datetime

def importar_desde_google_sheets(request):
    # Configuración de autenticación para gspread
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('./credentials.json', scopes=scopes)
    gc = gspread.authorize(credentials)


    # Abrir la hoja de cálculo y seleccionar la hoja deseada
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/12IdRTYfnPns-CAC4MOEpL0xNd71FC6w7C_ubTaJj-Ms/edit?usp=sharing'
    workbook = gc.open_by_url(spreadsheet_url)

    worksheet = workbook.worksheet('Solicitudes CD')

    # Extraer los datos de la hoja de cálculo
    data = worksheet.get_all_records()

       # Crear instancias del modelo Persona y guardarlas en la base de datos
    for row in data:
        fecha_nacimiento=row['Fecha de nacimiento']
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
            persona = Persona(
                # incluir_correo_en_respuesta=row['incluir_correo_en_respuesta'],
                nombre_identitario=row['Nombre identitario'],
                nombre_y_apellido=row['First name'] + ' ' + row['Last name'],
                 tipo_documento=row['Tipo de identificación'],
                 numero_documento=row['Número de identificación'],
                fecha_nacimiento=fecha_nacimiento,
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
            persona.save()
        except ValueError: 
            pass
    return print('Exitoso')