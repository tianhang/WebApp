

from app_hyperlink.models import Snippet
snippet = Snippet(code='foo = "bar"\n',owner_id=1)
snippet.save()

snippet = Snippet(code='print "hello, world"\n',owner_id=1)
snippet.save()

