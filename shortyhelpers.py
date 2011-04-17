import sys
import urllib2
import traceback

def splitter(s, sep=None) :
	if not sep :
		s = [s]
		for sep in [' ', "\t"] :
			s = splitter(s, sep)
		return s
	else :
		r = []
		for p in s :
			p = p.split(sep)
			r += p
		return r

def shorten(url, thresh=None) :
	if thresh is not None :
		if len(url) < thresh :
			return None

	# TODO check url for evil characters
	sapiurl = 'http://tinyurl.com/api-create.php?url=%s' % url

	try :
		stream = urllib2.urlopen(sapiurl)
		return stream.read()
	except :
		sys.stderr.write("exception in tinyurl api access\n")
		traceback.print_exc(file=sys.stderr)

def short(msg, thresh) :
	for url in [bit for bit in splitter(msg) if bit.startswith('http://') or bit.startswith('https://')] :
		s = shorten(url, thresh)
		if s :
			yield s
