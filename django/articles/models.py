from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)
    # category_id = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)

    STATUS_CHOICES = [
        (0, 'Удалено'),
        (1, 'Черновик'),
        (2, 'Опубликовано'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)

    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        indexes = [
            # models.Index(fields=['user_id']),
            # models.Index(fields=['category_id']),
            models.Index(name='article_status', fields=['status']),
        ]
