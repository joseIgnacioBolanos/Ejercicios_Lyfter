class WiFi:
    def __init__(self, wifi_name, wifi_password):
        self.wifi_name = wifi_name
        self.wifi_password = wifi_password

    def connectDevice(self, password_entered):
        if password_entered == self.wifi_password:
            print('Conectado')
        else:
            print('Contraseña Incorrecta')
        
    def disconnectDevice(self):
        pass
    def showConnectedDevices(self):
        pass

class Firewall():
    def __init__(self, blocked_ips):
        self.blocked_ips = blocked_ips
        
    def showBlockIps(self):
        print(f'{self.blocked_ips}')

class Monitoring():
    
    def __init__(self,  network_speed):
        self.network_speed = network_speed

    def showNetworkStatus(self):
        print(self.network_speed)
        


class SmartRouter(WiFi, Firewall, Monitoring):
    def __init__(self, wifi_name, wifi_password, blocked_ips, network_speed):
        self.wifi_name = wifi_name
        self.wifi_password = wifi_password
        self.blocked_ips = blocked_ips
        self.network_speed = network_speed



router = SmartRouter('KolbiABC', '1234', '10.254.100.5', 19.15)
router.connectDevice('12345')
router.showBlockIps()
router.showNetworkStatus()


        