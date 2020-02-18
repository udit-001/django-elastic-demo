from django.utils.text import slugify

def expert_article_upload_path(instance, filename): 
    return f"expert-article/user_{instance.created_by.username}/{filename}"