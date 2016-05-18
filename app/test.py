
from app.models import Snippet
from app.seralizers import SnippetSerializer


snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print "hello, world"\n')
snippet.save()

serializer = SnippetSerializer(snippet)
print serializer.data