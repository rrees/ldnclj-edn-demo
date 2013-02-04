from edn_format import Keyword

from collections import namedtuple

Attribute = namedtuple('Attribute', ['name', 'score'])

def keyword_to_name(keyword):
	return str(keyword)[1:]

def keys_to_strings(data):
	return dict([(keyword_to_name(k), v) for k, v in data.iteritems()])

def make_character(data):
	return dict([(keyword_to_name(k), keys_to_strings(v)) for k, v in data.iteritems()])


def list(data):
	return [make_character(character) for character in data]

def as_template_data(character):
	attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

	return [Attribute(k, v['score']) for k,v in character.iteritems()]