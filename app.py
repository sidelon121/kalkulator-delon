from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate(operation, angka1, angka2):
    if operation == "penjumlahan":
        return angka1 + angka2
    elif operation == "pengurangan":
        return angka1 - angka2
    elif operation == "perkalian":
        return angka1 * angka2
    elif operation == "pembagian":
        if angka2 == 0:
            return "Tidak bisa membagi dengan nol."
        return angka1 / angka2
    elif operation == "pangkat":
        return angka1 ** angka2
    elif operation == "persentase":
        if angka2 == 0:
            return "Total nilai tidak boleh nol."
        return (angka1 / angka2) * 100
    else:
        return "Operasi tidak valid."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        operation = request.form['operation']
        hasil = calculate(operation, angka1, angka2)
        return render_template('index.html', hasil=hasil, angka1=angka1, angka2=angka2, operation=operation)
    return render_template('index.html', hasil=None)

if __name__ == '__main__':
    app.run(debug=True)