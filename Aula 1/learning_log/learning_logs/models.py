from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usúario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em uma string modelo."""
        return self.text
    

class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # o argumento cascade fará com que ele seja deletado tbm caso o tópico relacionado seja deletado
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'       
