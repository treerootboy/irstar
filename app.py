IR_LIB = "/tmp/ir"

from flask import Flask, jsonify
import broadlink

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

@app.route("/home/<dev>/<cmd>")
def command(dev, cmd):
#    try:
      with open("%s/%s_%s.ir" % (IR_LIB, dev, cmd)) as f:
        ir_packet = f.readline()

      if ir_packet:
        device.send_data(ir_packet)
        return jsonify({ 'status': 'ok', 'message': '%s %sed' % (dev, cmd)})
      
      return jsonify({ 'status': 'error', 'message': 'ir_packet is empty' })

#    except:
#      return  jsonify({ 'status': 'error', 'message': 'server got an exception' })

@app.route("/home/learnir/<cmd>")
def learn(cmd):
    device.enter_learning()
    timeout = time.time() + 30
    while (ir_pack is None) and timeout > time.time():
      ir_pack = device.check_data()
      time.sleep(1)

    # recieved ir_pack
    if (ir_pack is not None):
      with open("%s/%s.ir" % (IR_LIB, cmd)) as f:
        f.write(ir_pack)
      return jsonify({ 'status': 'ok', 'message': 'command %s has learned' })
    
    # recieve timeout
    if (timeout<time.time()):
      return jsonify({ 'status': 'error', 'message': 'command recieve timeout'})  

    # recieve empty command
    return jsonify({ 'status': 'error', 'message': 'recieved command is empty'})  
