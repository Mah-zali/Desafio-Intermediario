#entradas
inicio = int(input().split()[1])
horasinicio, minutosinicio, segundosinicio = map(int, input().split(" : "))

fim = int(input().split()[1])
horasfim, minutosfim, segundosfim = map(int, input().split(" : "))

#colocar tudo em segundos
iniciototal = inicio * 86400 + horasinicio * 3600 + minutosinicio * 60 + segundosinicio
fimtotal = fim * 86400 + horasfim * 3600 + minutosfim * 60 + segundosfim

#diferença em segundos
duracao = fimtotal - iniciototal

#voltar para dias 
dias = duracao // 86400
duracao = duracao % 86400

horas = duracao // 3600
duracao = duracao % 3600

minutos = duracao // 60
segundos = duracao % 60

#saidas
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")