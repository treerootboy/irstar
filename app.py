IR_LIB = "/tmp/ir"

from flask import Flask, jsonify
import broadlink
import time

app = Flask(__name__)

print " * discovering broadlink devices..."
device = broadlink.discover(timeout=5)[0]
print " * device discovered, authing..."
device.auth()
print " * device authed."

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home/temperature")
def temperature():
    temp = device.check_temperature()
    return jsonify({ 'status': 'ok', 'temperature': temp})

@app.route("/home/learn/<cmd>")
def learn(cmd):
    device.enter_learning()
    timeout = time.time() + 30
    ir_pack = None
    while (ir_pack is None) and timeout > time.time():
      ir_pack = device.check_data()
      time.sleep(1)

    # recieved ir_pack
    if (ir_pack is not None):
      with open("%s/%s.ir" % (IR_LIB, cmd), 'w') as f:
        f.write(ir_pack)
      return jsonify({ 'status': 'ok', 'message': 'command %s has learned' % (cmd) })
    
    # recieve timeout
    if (timeout<time.time()):
      return jsonify({ 'status': 'error', 'message': 'command recieve timeout'})  

    # recieve empty command
    return jsonify({ 'status': 'error', 'message': 'recieved command is empty'})  

@app.route("/home/<dev>/status")
def status(dev):
  try:
    with open("%s/%s.st" % (IR_LIB, dev)) as f:
      status = f.read()
    return 'ON' if status == 'ON' else 'OFF'
  except:
    return 'OFF'

@app.route("/home/<dev>/<cmd>")
def command(dev, cmd):
#    try:
      with open("%s/%s_%s.ir" % (IR_LIB, dev, cmd)) as f:
        ir_packet = f.readline()

      if ir_packet:
        device.send_data(ir_packet)
        if cmd == 'open' or cmd == 'ON':
          status = 'ON'
          with open("%s/%s.st" % (IR_LIB, dev), 'w') as f:
            f.write('ON')
        elif cmd == 'close' or cmd == 'OFF':
          status = 'OFF'
          with open("%s/%s.st" % (IR_LIB, dev), 'w') as f:
            f.write('ON')
        
        
        return jsonify({ 'status': 'ok', 'message': '%s %sed' % (dev, cmd)})
      
      return jsonify({ 'status': 'error', 'message': 'ir_packet is empty' })

#    except:
#      return  jsonify({ 'status': 'error', 'message': 'server got an exception' })

