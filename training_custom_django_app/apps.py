"""
training_custom_django_app Django application initialization.
"""

from django.apps import AppConfig


class TrainingCustomDjangoAppConfig(AppConfig):
    """
    Configuration for the training_custom_django_app Django application.
    """

    name = 'training_custom_django_app'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "training_custom_django_app",
                "regex": r"^training",
                'relative_path': 'urls',
            },
            "cms.djangoapp": {
                "namespace": "training_custom_django_app",
                "regex": r"^training",
                'relative_path': 'urls',
            }
        },
}
