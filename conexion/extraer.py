
from app_registro.models import Persona, PertenenciaGrupoPoblacional
from app_diversidad_sexual.models import *
from app_informacion_general.models import *
import gspread
from google.oauth2 import service_account
from django.shortcuts import render
from datetime import datetime as dt
from django.db import IntegrityError
from django.http import HttpResponse

def persona(data):
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
                # Obtener o crear el objeto PertenenciaGrupoPoblacional
                nombre_grupo_poblacional = row['Grupo poblacional de pertenencia']
                grupo_poblacional, _ = PertenenciaGrupoPoblacional.objects.get_or_create(
                nombre_grupo_poblacional=nombre_grupo_poblacional)
                # Establecer la relación de muchos a muchos
                persona.pertenencia_grupo_poblacional.set([grupo_poblacional])
            except IntegrityError:
                pass

def diversidadSexual(data):
    for row in data:
        numero_documento = row['Número de identificación']
        persona = Persona.objects.filter(numero_documento=numero_documento).first()

        if persona:
            diversidad_sexual = DiversidadSexual.objects.create(
                id_persona=persona,
                cambio_nombre_sexo_documento=row['¿Ha realizado cambio de nombre y/o del componente sexo en el documento de identidad?'],
                recibir_orientacion_cambio_en_documento=True,
            )

            # Relación de muchos a muchos con Pronombre
            pronombres = row['Pronombre con el que se identifica:'].split(',')
            for pronombre_nombre in pronombres:
                pronombre, _ = Pronombre.objects.get_or_create(nombre_pronombre=pronombre_nombre.strip())
                diversidad_sexual.pronombres.add(pronombre)

            # Relación de muchos a muchos con IdentidadGenero
            identidades_genero = row['Identidad de géneros (¿Cómo te sientes, percibes, etc.?)'].split(',')
            for identidad_genero_nombre in identidades_genero:
                identidad_genero, _ = IdentidadGenero.objects.get_or_create(nombre_identidad_genero=identidad_genero_nombre.strip())
                diversidad_sexual.identidades_de_genero.add(identidad_genero)

            # Relación de muchos a muchos con ExpresionGenero
            expresiones_genero = row['¿Cuál es su expresión de género?'].split(',')
            for expresion_genero_nombre in expresiones_genero:
                expresion_genero, _ = ExpresionGenero.objects.get_or_create(nombre_expresion_genero=expresion_genero_nombre.strip())
                diversidad_sexual.expresiones_de_genero.add(expresion_genero)

            # Relación de muchos a muchos con OrientacionSexual
            orientaciones_sexuales = row['¿Cuál es su orientación sexual?'].split(',')
            for orientacion_sexual_nombre in orientaciones_sexuales:
                orientacion_sexual, _ = OrientacionSexual.objects.get_or_create(nombre_orientacion_sexual=orientacion_sexual_nombre.strip())
                diversidad_sexual.orientaciones_sexuales.add(orientacion_sexual)

            # Relación de muchos a muchos con RespuestaCambioDocumento
            respuestas_cambio_documento = row['¿Ha realizado cambio de nombre y/o del componente sexo en el documento de identidad?'].split(',')
            for respuesta_cambio_documento_nombre in respuestas_cambio_documento:
                respuesta_cambio_documento, _ = RespuestaCambioDocumento.objects.get_or_create(nombre_respuesta_cambio_documento=respuesta_cambio_documento_nombre.strip())
                diversidad_sexual.respuestas_cambio_documento.add(respuesta_cambio_documento)
"""
def infoGeneral(data):
    for row in data:
        numero_documento = row['Número de identificación']
        persona = Persona.objects.filter(numero_documento=numero_documento).exists()

        if persona:
            #info_general = InfoGeneral.objects.create(
            dedicacion_externa = row['Si no es estudiante, ¿A qué se dedica?']
            tipo_acompanamiento_recibido = row['¿A recibido acompañamiento en los últimos 3 meses?']
            observacion_tipo_acompanamiento_recibido = row['Observación del acompañamiento']
            tipo_entidad_acompanamiento_recibido = row['Entidad que brindó el acompañamiento']
            tipo_profesional_acompanamiento_recibido = row['Profesional que le brindó la atención']
            calificacion_acompanamiento_recibido = row['Calificación de la atención brindada']
            motivo_calificacion_acompanamiento = row['Motivo de la calificación']
            actividades_especificas_tiempo_libre = row['Tipos de actividades que se realizan durante el tiempo libre']
            observacion_general_actividades_especificas_tiempo_libre = row['Observación general de las actividades']
            observacion_general_fuente_de_ingresos = row['Observación general de las fuentes de ingresos']
            observacion_general_relacion_familiar = row['Observación general de la relación familiar']
            relacion_familiar = row['Calificación de la relación familiar']
            observacion_general_redes_de_apoyo = row['Observación general de las redes de apoyo']
            observacion_general_factores_de_riesgo = row['Factores de riesgo que podría poner en riesgo a la persona']
            creencia_religiosa = row['Creencia religiosa']
            encuentro_inicial = row['*Día de elección *']+ ' ' + row['*Horario de elección *']
            observacion_horario = row['Observación general del horario de elección']
            origen_descubrimiento_campus_diverso = row['Comentarios o sugerencias']
            comentarios_o_sugerencias_de_usuario = row['Comentarios o sugerencias']

            informacion_general = InformacionGeneral.objects.create(
                id_persona=persona,
                dedicacion_externa=dedicacion_externa,
                tipo_acompanamiento_recibido=tipo_acompanamiento_recibido,
                observacion_tipo_acompanamiento_recibido=observacion_tipo_acompanamiento_recibido,
                tipo_entidad_acompanamiento_recibido=tipo_entidad_acompanamiento_recibido,
                tipo_profesional_acompanamiento_recibido=tipo_profesional_acompanamiento_recibido,
                calificacion_acompanamiento_recibido=calificacion_acompanamiento_recibido,
                motivo_calificacion_acompanamiento=motivo_calificacion_acompanamiento,
                actividades_especificas_tiempo_libre=actividades_especificas_tiempo_libre,
                observacion_general_actividades_especificas_tiempo_libre=observacion_general_actividades_especificas_tiempo_libre,
                observacion_general_fuente_de_ingresos=observacion_general_fuente_de_ingresos,
                observacion_general_relacion_familiar=observacion_general_relacion_familiar,
                relacion_familiar=relacion_familiar,
                observacion_general_redes_de_apoyo=observacion_general_redes_de_apoyo,
                observacion_general_factores_de_riesgo=observacion_general_factores_de_riesgo,
                creencia_religiosa=creencia_religiosa,
                encuentro_inicial=encuentro_inicial,
                observacion_horario=observacion_horario,
                origen_descubrimiento_campus_diverso=origen_descubrimiento_campus_diverso,
                comentarios_o_sugerencias_de_usuario=comentarios_o_sugerencias_de_usuario,
            )

            # Ocupaciones actuales
            ocupaciones_actuales = row['Ocupación actual']
            if ocupaciones_actuales:
                ocupaciones_actuales = ocupaciones_actuales.split(',')
                for ocupacion_actual in ocupaciones_actuales:
                    ocupacion_actual = ocupacion_actual.strip()
                    ocupacion, _ = OcupacionActual.objects.get_or_create(nombre_ocupacion_actual=ocupacion_actual)
                    informacion_general.ocupaciones_actuales.add(ocupacion)

            # Actividades de tiempo libre
            actividades_tiempo_libre = row['Tipos de actividades que se realizan durante el tiempo libre']
            if actividades_tiempo_libre:
                actividades_tiempo_libre = actividades_tiempo_libre.split(',')
                for actividad_tiempo_libre in actividades_tiempo_libre:
                    actividad_tiempo_libre = actividad_tiempo_libre.strip()
                    actividad = ActividadTiempoLibre.objects.create(
                        nombre_actividad_tiempo_libre=actividad_tiempo_libre,
                        id_informacion_general=informacion_general
                    )

            # Fuentes de ingresos
            fuentes_ingresos = row['Fuente/s de ingresos']
            if fuentes_ingresos:
                fuentes_ingresos = fuentes_ingresos.split(',')
                for fuente_ingresos in fuentes_ingresos:
                    fuente_ingresos = fuente_ingresos.strip()
                    fuente = FuenteIngresos.objects.create(
                        nombre_fuente_ingresos=fuente_ingresos,
                        id_informacion_general=informacion_general
                    )

            # Convivencias en vivienda
            convivencias_vivienda = row['Personas con las que vive']
            if convivencias_vivienda:
                convivencias_vivienda = convivencias_vivienda.split(',')
                for convivencia_vivienda in convivencias_vivienda:
                    convivencia_vivienda = convivencia_vivienda.strip()
                    convivencia = ConvivenciaVivienda.objects.create(
                        nombre_convivencia_vivienda=convivencia_vivienda,
                        id_informacion_general=informacion_general
                    )

            # Redes de apoyo
            redes_apoyo = row['Redes de apoyo con los que cuenta la persona']
            if redes_apoyo:
                redes_apoyo = redes_apoyo.split(',')
                for red_apoyo in redes_apoyo:
                    red_apoyo = red_apoyo.strip()
                    red = RedApoyo.objects.create(
                        nombre_red_apoyo=red_apoyo,
                        id_informacion_general=informacion_general
                    )

            # Factores de riesgo
            factores_riesgo = row['Factores de riesgo que podría poner en riesgo a la persona']
            if factores_riesgo:
                factores_riesgo = factores_riesgo.split(',')
                for factor_riesgo in factores_riesgo:
                    factor_riesgo = factor_riesgo.strip()
                    factor = FactorRiesgo.objects.create(
                        nombre_factor_riesgo=factor_riesgo,
                        id_informacion_general=informacion_general
                    )

            # Encuentros día-hora
            encuentros_dias_horas = row['*Día de elección *']+ ' ' + row['*Horario de elección *']
            if encuentros_dias_horas:
                encuentros_dias_horas = encuentros_dias_horas.split(',')
                for encuentro_dia_hora in encuentros_dias_horas:
                    encuentro_dia_hora = encuentro_dia_hora.strip()
                    if '-' in encuentro_dia_hora:
                        dia, hora = encuentro_dia_hora.split('-')
                        encuentro = EncuentroDiaHora.objects.create(
                            dia=dia,
                            hora=hora
            )
                    informacion_general.encuentro_dias_horas.add(encuentro)

            informacion_general.save()

        else:
            print(f"No se encontró ninguna persona con el número de documento {numero_documento}")
"""