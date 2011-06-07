#!/usr/bin/env python

import sys
import irclib
import shortyhelpers

class Shorty(irclib.SimpleIRCClient) :
	def __init__(self, server, nick, chan, len=40) :
		self.len = len
		irclib.SimpleIRCClient.__init__(self)
		self.connect(server, 6667, nick)
		self.connection.join(chan)
	
	def on_join(self, c, e) :
		pass

	def on_pubmsg(self, c, e) :
		nick = e.source().split("!")[0]
		chan = e.target()
		txt = e.arguments()[0]
		n = 0
		msg = "%s's link%s:" % (nick, '%s')
		for short in shortyhelpers.short(txt, self.len) :
			msg += " " + short
			n += 1

		if n > 0 :
			plur = ' is'
			if n > 1 :
				plur = 's are'
			msg = msg % plur

			self.connection.privmsg(chan, msg)

if __name__ == '__main__' :
	try :
		try :
			s = Shorty(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
		except IndexError :
			s = Shorty(sys.argv[1], sys.argv[2], sys.argv[3])
	except IndexError :
		print 'usage: python shorty.py server nick channel [minlen]\n\n\texample:\n\tpython shorty.py irc.example.com shortbot \#hackers 40\n\n(Escape of # character is needed in most shells.)'
		sys.exit(1)
	s.start();
