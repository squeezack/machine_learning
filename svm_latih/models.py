from django.db import models

# Create your models here.
class DataPasien(models.Model):
    no = models.IntegerField(primary_key=True)
    nama_pasien = models.CharField(max_length=100)
    umur_pasien = models.IntegerField()
    nyeri_dada = models.IntegerField()
    sulit_menelan = models.IntegerField()
    rasa_terbakar = models.IntegerField()
    regurgitasi = models.IntegerField()
    batuk_kronis = models.IntegerField()
    sakit_tenggorokan = models.IntegerField()
    peningkatan_airliur = models.IntegerField()
    gangguan_tidur = models.IntegerField()
    gangguan_pernapasan = models.IntegerField()
    perubahan_beratbadan = models.IntegerField()
    kelelahan = models.IntegerField()
    gangguan_pencernaan = models.IntegerField()
    species = models.CharField(max_length=50)