from django.urls import path

from .views import (
    generate_chops_build,
    generate_line,
    get_progessions,
    main,
    render_line,
)

urlpatterns = [
    path("", main),
    path("generate", generate_line),
    path("chops_builder", generate_chops_build),
    path("progressions", get_progessions),
    path("render", render_line),
]
