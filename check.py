import ntplib
from time import ctime,time
from datetime import datetime, timezone

server1='br.pool.ntp.org'
server2='jp.pool.ntp.org'

c = ntplib.NTPClient()
remote1 = c.request(server2)
remote2 = c.request(server2)

local = time()
# delay = (horário que o server recebeu o pedido) - (horario que o get saido do client)
# Por tanto: o server_time irá ser o relógio dele rescontando a latencia de rede (delay)
server1_time = remote1.tx_time - remote1.delay
server2_time = remote2.tx_time - remote2.delay
diff = abs(server1_time - server2_time)
diff_raw = abs(remote1.tx_time - remote2.tx_time)

print("Local: {}".format(datetime.fromtimestamp(local, timezone.utc)))

print("REMOTE1 RAW - {}: {} ".format(server1, datetime.fromtimestamp(remote1.tx_time, timezone.utc)))
print("REMOTE2 RAW - {}: {}" .format(server2, datetime.fromtimestamp(remote2.tx_time, timezone.utc)))

print("REMOTE1 - {}: {} ".format(server1, datetime.fromtimestamp(server1_time, timezone.utc)))
print("REMOTE2 - {}: {}" .format(server2, datetime.fromtimestamp(server2_time, timezone.utc)))
print("Diferença entre os servers: {} segundos".format(diff))
print("Diferença raw entre os servers: {} segundos".format(diff_raw))
