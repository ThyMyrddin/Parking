from http.server import BaseHTTPRequestHandler, HTTPServer
import time,json
from PIL import Image

hostName = "196.74.183.149"
serverPort = 65432

poslist = [(0,0),(150,0),(350,0),(500,0),(0,250),(150,250),(350,250),(500,250)]


class MyServer(BaseHTTPRequestHandler):
    

    def do_POST(self):
        
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        
        data = json.loads(json.loads(body))
        print(type(data))

        imageVoiture = Image.open("voiture.jpg")
        imagePark = Image.open("park.png")

        imageVoiture = imageVoiture.convert("RGBA")
        imageVoiture = imageVoiture.resize((100,100))
        imagePark = imagePark.convert("RGBA")


        for i in range(8):
            if i in data[2]["amount"]:
                continue
            imagePark.alpha_composite(imageVoiture, dest=poslist[i])

        #imagePark.show()
        imagePark.save("ParkMeReact\\src\\components\\parking.png")
        self.send_response(200)
        with open("ParkMeReact\\src\\example.json",mode="w")as jsonFile:
        #with open("obj.json",mode="w")as jsonFile:
            #for(i in data)
            json.dump(data,jsonFile)
            jsonFile.close()

        
        


    

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")