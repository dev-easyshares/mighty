"""
Model class
Add [file, name, mimetype] field at the model

(file_url) return the url file static/media
(download_url) return the download url
(pdf_url) get the pdf in a viewer
(get_mime_type) return the mime type
(image_html) return the html tag <img>
(file_name) return the file name
(valid_file_name) get a valid name for filesystem
(file_extension) return the extension
"""
from django.db import models
from django.utils.text import get_valid_filename
from django.utils.html import format_html
from django.http import FileResponse
from django.core.exceptions import  PermissionDenied
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mighty.functions import file_directory_path, pretty_size_long, pretty_size_short
from mighty.fields import JSONField

import os, magic, logging, requests, tempfile
logger = logging.getLogger(__name__)

class File(models.Model):
    file = models.FileField(upload_to=file_directory_path, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filemimetype = models.CharField(max_length=255, blank=True, null=True, editable=False)
    charset = models.CharField(max_length=255, blank=True, null=True, editable=False)
    extracontenttype = JSONField(blank=True, null=True)
    size = models.BigIntegerField(default=0, editable=False)
    client_date = models.DateTimeField(null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True)
    object_id = models.PositiveBigIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    thumbnail = models.TextField(null=True, blank=True)
    hashid = models.CharField(max_length=40, db_index=True, blank=True, null=True)

    enable_hashid = False
    enable_thumbnail = False
    proxy_cloud_streaming = False
    chunk_size = 1024

    class Meta:
        abstract = True

    @property
    def file_url(self): return self.file.url

    @property
    def file_name(self):
        return self.filename if self.filename else os.path.basename(self.file.name)

    @property
    def valid_file_name(self):
        logger.warning('test: %s' % self.file)
        return get_valid_filename(self.file.name)

    @property
    def file_extension(self): return os.path.splitext(self.file_name)[-1]

    @property
    def download_url(self):
        if hastattr(self, 'uid'):
            return self.get_url('download', arguments={'uid': self.uid})
        return self.get_url('download', arguments={'pk': self.pk})

    @property
    def pdf_url(self):
        if hastattr(self, 'uid'):
            return self.get_url('pdf', arguments={'uid': self.uid})
        return self.get_url('pdf', arguments={'pk': self.pk})

    @property
    def name(self):
        return self.filename

    def set_thumbnail(self):
        if self.enable_thumbnail:
            from mighty.thumbnail import Thumbnail
            bck = Thumbnail(self.file, self.mime_or_ext)
            self.thumbnail = bck.base64

    def get_extra_data(self, _file):
        if not self.filename:
            self.filename = self.file_name
        self.filemimetype = _file.content_type
        self.size = _file.size
        self.charset = _file.charset
        self.extracontenttype = _file.content_type_extra

    def set_hashid(self):
        if self.enable_hashid:
            import hashlib
            hashid = hashlib.sha1(self.file.read())
            self.hashid = hashid.hexdigest()

    @property
    def mime_or_ext(self):
        return self.filemimetype if self.filemimetype else self.file_extension[1:]

    def some_extra_system(self):
        self.set_thumbnail()
        self.set_hashid()

    def make_data(self):
        if self.file._file:
            self.get_extra_data(self.file._file)
        self.some_extra_system()

    def size_long(self, unit=None):
        return pretty_size_long(self.size, unit) if self.size else None

    def size_short(self, unit=None):
        return pretty_size_short(self.size, unit) if self.size else None

    @property
    def cloud_file(self):
        cloud_file = requests.get(self.file.url, stream=True)
        cloud_file.raise_for_status()
        status_code = str(cloud_file.status_code)[0]
        if status_code == "2" or status_code == "3":
            #with tempfile.NamedTemporaryFile(mode='w+b') as tmp_file:
            #    for chunk in cloud_file.iter_content(self.chunk_size):
            #        tmp_file.write(chunk)
            return cloud_file
        raise PermissionDenied()

    def http_download(self):
        todl_file = self.cloud_file if self.proxy_cloud_streaming else self.file
        response = FileResponse(todl_file)
        response['Content-Disposition'] = 'attachment; filename="%s"' % self.file_name
        return response
