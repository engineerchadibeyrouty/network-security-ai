from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSBridge

class SimpleTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SimpleTopo()
    net = Mininet(topo=topo, controller=None, switch=OVSBridge)
    net.start()
    CLI(net)
    net.stop()
