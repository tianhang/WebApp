

from app.seralizers import SnippetSerializer

from app.models import Snip
snippet = Snip(code='foo = "bar"\n',owner_id=1)
snippet.save()

snippet = Snip(code='print "hello, world"\n',owner_id=1)
snippet.save()

serializer = SnippetSerializer(snippet)
print serializer.data