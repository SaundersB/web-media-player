from __future__ import unicode_literals

from django.db import models

# Models
class AudioTrack(models.Model):
	song_title = models.CharField(max_length=50, null=True)
	artist = models.CharField(max_length=100, null=True)
	album = models.CharField(max_length=100, null=True)
	date_added = models.DateField(null=True)
	genre = models.CharField(max_length=50, null=True)
	play_count = models.IntegerField(null=True)
	rating = models.CharField(max_length=10, null=True)
	year = models.IntegerField(null=True)
	track_number = models.IntegerField(null=True)
	file_size = models.DecimalField(max_digits=20, decimal_places=5, null=True)

	def __str__(self):
		return u'%s %s %s %s %s %s %s %s %s %s' % (self.song_title, self.artist, self.album, self.date_added, self.genre, self.play_count, self.rating, self.year, self.track_number, self.file_size)


class VideoTrack(models.Model):
	video_title = models.CharField(max_length=50, null=True)
	artist = models.CharField(max_length=100, null=True)
	date_added = models.DateField()
	genre = models.CharField(max_length=50, null=True)
	play_count = models.IntegerField()
	rating = models.CharField(max_length=10, null=True)
	year = models.IntegerField()
	file_size = models.DecimalField(max_digits=20, decimal_places=5)

	def __str__(self):
		return u'%s %s %s %s %s %s %s %s %s %s' % (self.song_title, self.artist, self.album, self.date_added, self.genre, self.play_count, self.rating, self.year, self.track_number, self.file_size)
