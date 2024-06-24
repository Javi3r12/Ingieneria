# views.py

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm,EstadoSolicitud
from .models import estadoSoli,Solicitudes

def index(request):
    estados = estadoSoli.objects.all()
    form = ContactForm()  # Instancia del formulario vacío

    context = {
        'estados': estados,
        'form': form,
    }

    return render(request, 'index.html', context)

def solicitud(request):
    solicitudes = Solicitudes.objects.all()

    context= {'solicitudes': solicitudes}
    return render(request,'solicitudes.html', context)

def soliFind(request,pk):
    if pk != "":
        solicitud=Solicitudes.objects.get(id=pk)
        estados=estadoSoli.objects.all()

        print(type(solicitud.id))

        context = {
        'estados': estados,
        'solicitud': solicitud,
        }
        
        return render(request,'CambioEstado.html',context)

def solicitudUpdate(request):
    if request.method == "POST":
        id = request.POST["id"]
        nombre = request.POST["nombre"]
        correo = request.POST["correo"]
        estado_id = request.POST["estado"]
        detalle = request.POST["detalle"]
        
        try:
            objEstado = estadoSoli.objects.get(idEstado=estado_id)
            solicitud = Solicitudes.objects.get(id=id)
            
            solicitud.nombre = nombre
            solicitud.correo = correo
            solicitud.idEstado = objEstado
            solicitud.detalle = detalle
            solicitud.save()
            
            # Envío de correo
            subject = 'Actualización de Solicitud'
            mensaje = f'Su solicitud está en el estado: {objEstado.estado} \n Detalle: {detalle}'
            recipient_list = [correo]
            
            template = render_to_string('email-template.html', {
                'name': nombre,
                'email': correo,
                'subject': subject,
                'message': mensaje  
            })
            
            emailSender = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                recipient_list
            )
            emailSender.content_subtype = 'html'
            emailSender.send()
            
            return redirect('solicitud')
            
        except estadoSoli.DoesNotExist:
            return HttpResponse('El estado especificado no existe')
        except Solicitudes.DoesNotExist:
            return HttpResponse('La solicitud especificada no existe')
        except Exception as e:
            return HttpResponse(f'Ocurrió un error: {str(e)}')
        
    else:
        id = request.GET["id"]
        try:
            solicitud = Solicitudes.objects.get(id=id)
            estados = estadoSoli.objects.all()
            context = {
                'mensaje': "Ok, datos actualizados...",
                'estados': estados,
                'solicitud': solicitud
            }
            return render(request, 'CambioEstado.html', context)
        except Solicitudes.DoesNotExist:
            return HttpResponse('La solicitud especificada no existe')

def correoSoli(request):
    estados = estadoSoli.objects.all()
    solicitud_id = request.POST.get("id", None)
    if solicitud_id:
        try:
            solicitud = Solicitudes.objects.get(id=solicitud_id)
            form = EstadoSolicitud(request.POST or None)
            
            if request.method == 'POST':
                if form.is_valid():
                    destinatarios = form.cleaned_data.get('correo', '')
                    nombre = form.cleaned_data['nombre']
                    email = form.cleaned_data.get('correo', '')
                    estado_id = form.cleaned_data['estado']
                    detalle = form.cleaned_data['detalle']
                    
                    try:
                        objEstado = estadoSoli.objects.get(idEstado=estado_id)
                    except estadoSoli.DoesNotExist:
                        return HttpResponse('El estado especificado no existe')
                    
                    subject = 'Actualización de Solicitud'
                    mensaje = f'Su solicitud está en el estado: {objEstado.estado} \n Detalle: {detalle}'
                    recipient_list = [email.strip() for email in destinatarios.split(',')]
    
                    template = render_to_string('email-template.html', {
                        'name': nombre,
                        'email': email,
                        'subject': subject,
                        'message': mensaje  
                    })
                    emailSender = EmailMessage(
                        subject,
                        template,
                        settings.EMAIL_HOST_USER,
                        recipient_list
                    )
                    emailSender.content_subtype = 'html'
                    try:
                        emailSender.send()
                        messages.success(request, 'El correo electrónico se envió correctamente')
                    except:
                        messages.error(request, 'Hubo un error al enviar el correo electrónico. Inténtelo de nuevo más tarde.')
                    return redirect('solicitud')
                
            context = {
                'estados': estados,
                'solicitud': solicitud,
            }
            return render(request, 'cambioEstado.html', context)
        
        except Solicitudes.DoesNotExist:
            return HttpResponse('La solicitud especificada no existe')
    
    return HttpResponse('Se requiere un ID de solicitud válido')


def contact(request):
    estados = estadoSoli.objects.all()
    form = ContactForm(request.POST or None)  # Manejar solicitud POST

    if request.method == 'POST':
        if form.is_valid():
            destinatarios = form.cleaned_data.get('destinatarios', '')  
            name = form.cleaned_data['name']
            email = form.cleaned_data.get('destinatarios', '')
            subject = f'Cambio estado de su solicitud'
            opcion_mensaje_id = form.cleaned_data['opcion_estado']
            razon = form.cleaned_data['razon']
            
            mensaje = f'Su solicitud esta en el estado: {opcion_mensaje_id} \n Detalle: {razon}'
            # Separar los correos electrónicos por comas y eliminar espacios en blanco
            recipient_list = [email.strip() for email in destinatarios.split(',')]

            template = render_to_string('email-template.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': mensaje
            })

            emailSender = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                recipient_list  
            )
            emailSender.content_subtype = 'html'

            try:
                emailSender.send()
                messages.success(request, 'El correo electrónico se envió correctamente')
            except:
                messages.error(request, 'Hubo un error al enviar el correo electrónico. Inténtelo de nuevo más tarde.')

            return redirect('index')

    context = {
        'estados': estados,
        'form': form,
    }

    return render(request, 'index.html', context)
