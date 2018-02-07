# djangoProduction
HANDLING CUSTOM ERROR PAGES(404, 500) IN DJANGO
AND DEBUG = False
<pre><code>
Steps：
+DEBUG = False
+ALLOWED_HOSTS = ['10.10.13.99']
+STATIC_ROOT = os.path.join(BASE_DIR, 'static')
+
 STATICFILES_DIRS = (
-    "%s/%s" % (BASE_DIR, "static"),
+    "%s/%s" % (BASE_DIR, "test/static"), //不能和STATIC_ROOT一样
 )
 
 
 
 +++ b/DjangoProduction/urls.py
@@ -15,9 +15,14 @@ Including another URLconf
 """
 from django.conf.urls import url
 from django.contrib import admin
+from django.views import static
+from django.conf import settings
 import views
 
+handler404 = views.page_not_found
+
 urlpatterns = [
+    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static'),// Display an error， to see the source code



+def page_not_found(request):
+    return render(request, '404.html')

</pre></code>
