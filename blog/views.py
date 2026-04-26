from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
from .serializers import PostSerializer

class PostsView:
    @require_http_methods(["GET"])
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

class PostDetailView:
    @require_http_methods(["GET"])
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return JsonResponse(serializer.data, safe=False)
        except ObjectDoesNotExist:
            return Http404('Post not found.')