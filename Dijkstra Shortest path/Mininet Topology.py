#!/usr/bin/python


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

def Mytopo():
	net = Mininet( controller=RemoteController, link=TCLink ,autoStaticArp=True)
#Add hosts and switches
	info( '*** Adding controller\n' )
	c0=net.addController( 'c0',controller=RemoteController,ip='127.0.0.1',port=6633 )
	
#Add hosts and switches
	info( '*** Adding host\n' )
	h1=net.addHost('h1',ip='10.0.0.1',mac='00:00:00:00:00:01',defaultRoute=None, protocols='OpenFlow13')
	h2=net.addHost('h2',ip='10.0.0.2',mac='00:00:00:00:00:02',defaultRoute=None, protocols='OpenFlow13')
	h4=net.addHost('h4',ip='10.0.0.4',mac='00:00:00:00:00:04',defaultRoute=None, protocols='OpenFlow13')
	h5=net.addHost('h5',ip='10.0.0.5',mac='00:00:00:00:00:05',defaultRoute=None, protocols='OpenFlow13')
	h6=net.addHost('h6',ip='10.0.0.6',mac='00:00:00:00:00:06',defaultRoute=None, protocols='OpenFlow13')

	info( '*** Adding switch\n' )
	S1=net.addSwitch('S1',stp=True)
	S2=net.addSwitch('S2',stp=True)
	S3=net.addSwitch('S3',stp=True)
	S4=net.addSwitch('S4',stp=True)
	S5=net.addSwitch('S5',stp=True)
	S6=net.addSwitch('S6',stp=True)
	# Add Links
	info( '*** Adding link\n' )
	net.addLink(h1,S1)
	net.addLink(h2,S2)
	net.addLink(h4,S4)
	net.addLink(h5,S5)
	net.addLink(h6,S6)
	net.addLink(S1,S2,bw=10)
	net.addLink(S2,S4,bw=15)
	net.addLink(S1,S3,bw=10)
	net.addLink(S3,S4,bw=5)
	net.addLink(S1,S5,bw=15)
	net.addLink(S5,S6,bw=15)
	net.addLink(S4,S6,bw=10)
	net.addLink(S2,S3,bw=15)
	
	net.build()
	S1.start([c0])
	S2.start([c0])
	S3.start([c0])
	S4.start([c0])
	S5.start([c0])
	S6.start([c0])


	info( '*** Running CLI\n' )
	CLI( net )

	info( '*** Stopping network' )
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	Mytopo()

