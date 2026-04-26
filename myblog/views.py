from django.shortcuts import render


def home(request):
    """Render the homepage using the ``index.html`` template.

    This view is mapped to the root URL ``/`` and serves the main
    landing page of the blog platform.
    """
    return render(request, "index.html")
