from haystack import indexes
from alumni_search.models import Alumni

class AlumniIndex(indexes.SearchIndex,indexes.Indexable):
	text=indexes.CharField(document=True,use_template=True)
	#yop=indexes.CharField(model_attr='yop')
	#city=indexes.CharField(model_attr='city')
	#branch=indexes.CharField(model_attr='branch')

	def get_model(self):
		return Alumni

