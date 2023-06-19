
from app_registro.models import Persona, PertenenciaGrupoPoblacional
import gspread
from google.oauth2 import service_account
from django.shortcuts import render


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
        persona = Persona(
            # incluir_correo_en_respuesta=row['incluir_correo_en_respuesta'],
            nombre_identitario=row['Nombre identitario'],
            nombre_y_apellido=row['First name'] + ' ' + row['Last name'],
            # tipo_documento=row['tipo_documento'],
            # numero_documento=row['numero_documento'],
             fecha_nacimiento=row['Fecha de nacimiento'],
            # estrato_socioeconomico=row['estrato_socioeconomico'],
            # ciudad_nacimiento=row['ciudad_nacimiento'],
            # municipio_nacimiento=row['municipio_nacimiento'],
            # corregimiento_nacimiento=row['corregimiento_nacimiento'],
            # departamento_nacimiento=row['departamento_nacimiento'],
            # pais_nacimiento=row['pais_nacimiento'],
            # ciudad_residencia=row['ciudad_residencia'],
            # municipio_residencia=row['municipio_residencia'],
            # corregimiento_residencia=row['corregimiento_residencia'],
            # zona_residencial=row['zona_residencial'],
            # direccion_residencia=row['direccion_residencia'],
            # barrio_residencia=row['barrio_residencia'],
            # comuna_barrio=row['comuna_barrio'],
            # telefono=row['telefono'],
            # estado_civil=row['estado_civil'],
            # identidad_etnico_racial=row['identidad_etnico_racial'],
            # nombre_persona_de_confianza=row['nombre_persona_de_confianza'],
            # relacion_persona_de_confianza=row['relacion_persona_de_confianza'],
            # telefono_persona_de_confianza=row['telefono_persona_de_confianza'],
        )
        persona.save()

    return render(request, 'importacion_exitosa.html')