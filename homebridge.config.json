{
     "bridge": {
        "name": "HomeBridge",
        "username": "CC:22:3D:E3:CE:31",
        "port": 51826,
        "pin": "031-45-154"
     },
     "description": "My HomeBridge OpenRemote sample",
     "accessories": [ 
         {
            "accessory": "Http",
            "name": "客廳電視",
	    "http_method": "GET",
            "on_url": "http://192.168.199.179:5000/home/tv/power",
            "off_url": "http://192.168.199.179:5000/home/tv/power"
         },
         {
            "accessory": "Http",
            "name": "客廳空調",
	    "http_method": "GET",
            "on_url": "http://192.168.199.179:5000/home/air/open",
            "off_url": "http://192.168.199.179:5000/home/air/close"
         },
         {
            "accessory": "HttpTemperature",
            "name": "客廳溫度",
            "url": "http://192.168.199.179:5000/home/temperature",
            "http_method": "GET"
         }
     ]
}
