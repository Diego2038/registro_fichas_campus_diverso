from app_registro.models import Persona, PertenenciaGrupoPoblacional
import gspread
from google.oauth2 import service_account
from django.shortcuts import render
from datetime import datetime as dt
from django.db import IntegrityError
from django.http import HttpResponse
from conexion.extraer import persona, diversidadSexual, infoAcademica, DocumentoAutorizacion, infoGeneral

def importar_desde_google_sheets(request):
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('./credentials.json', scopes=scopes)
    gc = gspread.authorize(credentials)

    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/12IdRTYfnPns-CAC4MOEpL0xNd71FC6w7C_ubTaJj-Ms/edit?usp=sharing'
    workbook = gc.open_by_url(spreadsheet_url)
    worksheet = workbook.worksheet('Solicitudes CD')

    data = worksheet.get_all_records()

    ##Hace la conexion con el modelo de persona
    persona(data)
    diversidadSexual(data)
    DocumentoAutorizacion(data)
    infoAcademica(data)
    infoGeneral(data)


    return HttpResponse('Exitoso')
