import csv
from django.shortcuts import render
from .models import DataPasien
from .forms import InputForm
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.apps import apps

def populate_database():
    with open('data_pasien.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
              # Tambahkan pernyataan log
            _, created = DataPasien.objects.get_or_create(
                no=row[0],
                nama_pasien=row[1],
                umur_pasien=row[2],
                nyeri_dada=row[3],
                sulit_menelan=row[4],
                rasa_terbakar=row[5],
                regurgitasi=row[6],
                batuk_kronis=row[7],
                sakit_tenggorokan=row[8],
                peningkatan_airliur=row[9],
                gangguan_tidur=row[10],
                gangguan_pernapasan=row[11],
                perubahan_beratbadan=row[12],
                kelelahan=row[13],
                gangguan_pencernaan=row[14],
                species=row[15],
            )

# Populate database when the application starts
populate_database()

# Load data from the database
data_pasien = DataPasien.objects.all()

# Prepare features and labels
features = [[data.nyeri_dada,data.sulit_menelan,data.rasa_terbakar,data.regurgitasi,data.batuk_kronis,data.sakit_tenggorokan,data.peningkatan_airliur,data.gangguan_tidur,data.gangguan_pernapasan,data.perubahan_beratbadan,data.kelelahan,data.gangguan_pencernaan] for data in data_pasien]
labels = [data.species for data in data_pasien]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Initialize and train SVM model
svm_model = svm.SVC(kernel='linear', C=1, gamma='auto') #SVM Jenis model linear
svm_model.fit(X_train, y_train)

def index(request):
    context = {
        'title' : 'Data Latih',
        'data_pasien' : DataPasien.objects.all()
    }
    return render(request, 'pages/latih/index.html', context)
    
def data_detail(request, pk):
    data_pasien = DataPasien.objects.get(pk=pk)
    return render(request, 'pages/latih/detail.html', {'data_pasien': data_pasien})

def classify(request):
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            nama_pasien = form.cleaned_data['nama_pasien']
            umur_pasien = form.cleaned_data['umur_pasien']
            nyeri_dada = form.cleaned_data['nyeri_dada']
            sulit_menelan = form.cleaned_data['sulit_menelan']
            rasa_terbakar = form.cleaned_data['rasa_terbakar']
            regurgitasi = form.cleaned_data['regurgitasi']
            batuk_kronis = form.cleaned_data['batuk_kronis']
            sakit_tenggorokan = form.cleaned_data['sakit_tenggorokan']
            peningkatan_airliur = form.cleaned_data['peningkatan_airliur']
            gangguan_tidur = form.cleaned_data['gangguan_tidur']
            gangguan_pernapasan = form.cleaned_data['gangguan_pernapasan']
            perubahan_beratbadan = form.cleaned_data['perubahan_beratbadan']
            kelelahan = form.cleaned_data['kelelahan']
            gangguan_pencernaan = form.cleaned_data['gangguan_pencernaan']


            # Make prediction using SVM model
            predicted_label = svm_model.predict([[nyeri_dada, sulit_menelan, rasa_terbakar, regurgitasi, batuk_kronis, sakit_tenggorokan, peningkatan_airliur, gangguan_tidur, gangguan_pernapasan, perubahan_beratbadan, kelelahan,gangguan_pencernaan]])[0]

            # Convert numeric label back to species name
            nama_pasien = form.cleaned_data['nama_pasien']
            result = predicted_label
    else:
        form = InputForm()

    return render(request, 'pages/klasifikasi/index.html', {'form': form,'nama_pasien':nama_pasien, 'result': result})