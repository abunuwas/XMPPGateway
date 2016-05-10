import sys
import logging
import getpass
from optparse import OptionParser

import sleekxmpp

reload(sys)
sys.setdefaultencoding('utf8')


class EchoBot(sleekxmpp.ClientXMPP):

	def __inti__(self, jid, password):
		sleekxmpp.ClientXMPP.__init__(self, jid, password)

		self.add_event_handler('session_start', self.start)

		self.add_event_handler('message', self.message)

	def start(self, event):
		self.send_presence()
		self.get_roster()

	def message(self, msg):
		if msg['type'] in ('chat', 'normal'):
			msg.reply('Thanks for sending\n%(body)s' % msg).send()

if __name__ == '__main__':
	xmpp = EchoBot('user1@localhost', 'mypassword')
	if xmpp.connect():
		print('connecting...')
		xmpp.process(block=True)
		print('Done')
	else:
		print('Unable to connect')

