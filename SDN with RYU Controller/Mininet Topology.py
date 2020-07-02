#!/usr/bin/python


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

def Mytopo():
	net = Mininet( controller=RemoteController, link=TCLink )
#Add hosts and switches
	info( '*** Adding controller\n' )
	net.addController( 'c0' )
	
#Add hosts and switches
	info( '*** Adding host\n' )
	h1=net.addHost('h1')
	h2=net.addHost('h2')
	h3=net.addHost('h3')
	h4=net.addHost('h4')
	h5=net.addHost('h5')
	h6=net.addHost('h6')
	info( '*** Adding switch\n' )
	S1=net.addSwitch('S1')
	S2=net.addSwitch('S2')
	S3=net.addSwitch('S3')
	S4=net.addSwitch('S4')
	S5=net.addSwitch('S5')
	S6=net.addSwitch('S6')
	# Add Links
	info( '*** Adding link\n' )
	net.addLink(h1,S1)
	net.addLink(h2,S2)
	net.addLink(h3,S3)
	net.addLink(h4,S4)
	net.addLink(h5,S5)
	net.addLink(h6,S6)
	net.addLink(S1,S2,bw=10)
	net.addLink(S1,S3,bw=10)
	net.addLink(S3,S4,bw=5)
	net.addLink(S1,S5,bw=5)
	net.addLink(S5,S6,bw=5)
	

	net.start()


	info( '*** Running CLI\n' )
	CLI( net )

	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	Mytopo()

