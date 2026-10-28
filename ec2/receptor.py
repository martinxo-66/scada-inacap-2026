from http.server import HTTPServer, BaseHTTPRequestHandler
import json, threading, time, random

history_data = []

def emisor_autonomo():
    global history_data
    nivel = 45.0
    subiendo = True
    while True:
        if subiendo:
            nivel += random.uniform(1.5, 3.5)
            if nivel >= 85.0:
                subiendo = False
        else:
            nivel -= random.uniform(1.5, 3.5)
            if nivel <= 25.0:
                subiendo = True

        cloro = round(random.uniform(0.48, 0.58), 2)
        bomba = "ENCENDIDA" if subiendo else "APAGADA"
        alarma = "CRITICA" if nivel > 80.0 else "NORMAL"
        
        # Timestamp en milisegundos reales
        ts = int(time.time() * 1000)

        payload = {
            "timestamp": ts,
            "nivel_estanque": round(nivel, 2),
            "cloro_ppm": cloro,
            "bomba": bomba,
            "alarma": alarma
        }
        
        history_data.append(payload)
        if len(history_data) > 30:
            history_data.pop(0)
        time.sleep(2)

threading.Thread(target=emisor_autonomo, daemon=True).start()

class AWSReceiver(BaseHTTPRequestHandler):
    def do_POST(self):
        sz = int(self.headers.get("Content-Length", 0))
        if sz > 0:
            body = self.rfile.read(sz).decode()
            data_recibida = json.loads(body)
            if "timestamp" not in data_recibida:
                data_recibida["timestamp"] = int(time.time() * 1000)
            history_data.append(data_recibida)
            if len(history_data) > 30:
                history_data.pop(0)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({"status": "ok"}).encode())

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        data_to_send = history_data if history_data else [{"timestamp": int(time.time() * 1000), "nivel_estanque": 50.0, "cloro_ppm": 0.5}]
        self.wfile.write(json.dumps(data_to_send).encode())

    def log_message(self, format, *args):
        return

print("[AWS-SCADA] Servidor activo con milisegundos en puerto 5000...")
HTTPServer(("0.0.0.0", 5000), AWSReceiver).serve_forever()
