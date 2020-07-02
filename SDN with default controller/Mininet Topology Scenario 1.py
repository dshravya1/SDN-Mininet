#!/usr/bin/python


from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info


def Mytopo():
	net = Mininet( controller=Controller, link=TCLink )
#Add hosts and switches
	info( '*** Adding controller\n' )
	net.addController( 'c0' )
	info( '*** Adding host\n' )
	H1=net.addHost('H1', ip="10.0.1.10/24")
	H2=net.addHost('H2', ip="10.0.1.11/24")
	H3=net.addHost('H3',ip="10.0.1.12/24")
	H4=net.addHost('H4',ip="10.0.1.13/24")
	H5=net.addHost('H5',ip="10.0.2.10/24")
	H6=net.addHost('H6',ip="10.0.2.11/24")
	H7=net.addHost('H7',ip="10.0.2.12/24")
	H8=net.addHost('H8',ip="10.0.2.13/24")
	H9=net.addHost('H9',ip="10.0.1.1/24")
	H10=net.addHost('H10',ip="10.0.2.1/24")
	info( '*** Adding switch\n' )
	S9=net.addSwitch('S9')
	S10=net.addSwitch('S10')
	S11=net.addSwitch('S11')
	S12=net.addSwitch('S12')
	S13=net.addSwitch('S13')
	S14=net.addSwitch('S14')
	S15=net.addSwitch('S15')
	# Add Links
	info( '*** Adding link\n' )
	net.addLink(H9,S9)
	net.addLink(H10,S9)
	net.addLink(S9,S10,bw=10)
	net.addLink(S9,S13)
	net.addLink(S10,S11)
	net.addLink(S10,S12,bw=15,delay='10ms')
	net.addLink(S13,S14)
	net.addLink(S13,S15)
	net.addLink(S11,H1)
	net.addLink(S11,H2)
	net.addLink(S12,H3)
	net.addLink(S12,H4)
	net.addLink(S14,H5)
	net.addLink(S14,H6)
	net.addLink(S15,H7)
	net.addLink(S15,H8)

	net.start()


	info( '*** Running CLI\n' )
	CLI( net )

	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	Mytopo()

