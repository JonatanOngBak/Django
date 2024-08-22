from django.db import models

class Topic(models.Model):
    """Um assunto sobre o qual o usúario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em uma string modelo."""
        return self.text
        

