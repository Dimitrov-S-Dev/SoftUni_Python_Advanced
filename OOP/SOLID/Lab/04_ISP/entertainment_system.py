from abc import ABC, abstractmethod


class EthernetConnector(ABC):
    @abstractmethod
    def connect_device_via_ethernet_cable(self, device):
        pass


class HDMIConnector(ABC):
    def connect_device_via_hdmi_connector(self, device):
        pass


class PowerConnector(ABC):
    @abstractmethod
    def connect_device_to_power_outlet(self, device):
        pass


class RcaConnector:
    def connect_to_device_via_rca_cable(self, device):
        pass


class Television(RcaConnector, HDMIConnector, PowerConnector, ABC):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_device_via_hdmi_connector(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMIConnector, PowerConnector, ABC):
    def connect_to_tv(self, television):
        self.connect_device_via_hdmi_connector(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HDMIConnector, PowerConnector, EthernetConnector, ABC):
    def connect_to_tv(self, television):
        self.connect_device_via_hdmi_connector(television)

    def connect_to_router(self, router):
        self.connect_device_via_ethernet_cable(router)

    def plug_in_to_power(self):
        self.connect_device_to_power_outlet(self)


class Router(PowerConnector, EthernetConnector, ABC):

    def connect_to_tv(self, television):
        self.connect_device_via_ethernet_cable(television)

    def plug_in_to_power(self):
        self.connect_device_to_power_outlet(self)
"""
class EntertainmentDevice:
    def connect_to_device_via_hdmi_cable(self, device): pass
    def connect_to_device_via_rca_cable(self, device): pass
    def connect_to_device_via_ethernet_cable(self, device): pass
    def connect_device_to_power_outlet(self, device): pass


class Television(EntertainmentDevice):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


"""