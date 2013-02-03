from edn_format import Keyword

def keyword_to_name(keyword):
	return str(keyword)[1:]

def keys_to_strings(data):
	return dict([(keyword_to_name(k), v) for k, v in data.iteritems()])

def make_character(data):
	return dict([(keyword_to_name(k), keys_to_strings(v)) for k, v in data.iteritems()])


def list(data):
	return [make_character(character) for character in data]