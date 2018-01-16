import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_rocky.settings")
django.setup()

from movie_search import models as msm

def main():
    f = open('oldblog.txt')
    for line in f:
        title,content = line.split('****')
        msm.Blog.objects.create(title=title, content=content)
    f.close()

if __name__ == '__main__':
    main()
    print("done!")