import time
import network
import socket
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# connect Wi-Fi CHANGE THIS!!!!!!!!
ssid = 'WiFiName'
password = 'password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# start Web server and listen
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('Web server is active...')
print('IP Address:', wlan.ifconfig()[0])

# Main loop
while True:
    cl, addr = s.accept()
    print('Connection waiting...')
    request = cl.recv(1024)
    request = str(request)
    print('Request:', request)

    if 'POST /lcd' in request:
        lcd.clear()
        text = request.split('text=')[1].split(' ')[0]
        lcd.putstr(text)

    response = """<!DOCTYPE html>
<html>
<head>
    <title>LCD Screen</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Write Text to LCD Screen</h1>
    <form onsubmit="sendText(event)">
        <label for="text">Text:</label>
        <input type="text" id="text" name="text"><br><br>
        <input type="submit" value="Submit">
    </form>

    <script>
        function sendText(event) {
            event.preventDefault();
            const text = document.getElementById("text").value;
            const xhr = new XMLHttpRequest();
            xhr.open("POST", "/lcd", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.send("text=" + text);
            alert("Text submitted!");
        }
    </script>
</body>
</html>
"""
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()

