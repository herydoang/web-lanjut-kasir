from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    def __str__ (self):
        return self.nama
    
class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.nama