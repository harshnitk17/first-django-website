from django.db import models

from django.utils import timezone
class Category(models.Model):
	
	category_text = models.CharField(max_length=200)
	def __str__(self):
		return self.category_text
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text