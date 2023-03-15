name = "Jhon Doe"
age = 23

#Menampilkan Output
print("my name is ",name,". I'am ",age," years old")

#Menghilangkan nama yang sama
friends = ["Nolan", "Mary", "Abby", "Nolan", "Abby"]
result = set(friends)
print (result)
print(50*"-")


def jhon():
    name = "jOhn DoE"

    #Huruf Besar
    upper = name.upper()
    print(upper)

    #Huruf Kecil
    lower = name.lower()
    print(lower)

    #Perbaiki
    fix = name.title()
    print(fix)

jhon()
print(50*"-")

#Array

employees = [
{
"name": "Adam Moore",
"gender": "male",
"age": 39,
"salary": 15_000_000,
"position": "manager",
"work_time": 5
},
{
"name": "Ellis McCoy",
"gender": "female",
"age": 31,
"salary": 10_000_000,
"position": "supervisor",
"work_time": 8
},
{
"name": "Mary Jane",
"gender": "female",
"age": 24,
"salary": 25_000,
"position": "admin",
"work_time": 8
},
{
"name": "Alex Murphy",
"gender": "male",
"age": 35,
"salary": 10_000,
"position": "developer",
"work_time": 12
},
{
"name": "Norman Bourne",
"gender": "male",
"age": 18,
"salary": 5000,
"position": "developer",
"work_time": 7.5
}
]

#1. Jumlah karyawan laki - laki
male_count = 0
female_count = 0

for employee in employees:
    if employee ["gender"] == "male":
        male_count += 1
    elif employee ["gender"] == "female":
        female_count += 1
print("Jumlah karyawan Laki - laki adalah ", male_count)
print("Jumlah karyawan Perempuan adalah ", female_count)

#Mencari tahu manager
manager_name = None
for employee in employees:
    if employee ["position"] == "manager":
        manager_name = employee["name"]
        break
if manager_name:
    print ("Nama manager nya adalah ", manager_name)
else:
    print("Tidak ada manager")

#Menghitung bonus
total_salary = 0

for employee in employees:
    if employee ["work_time"] > 7 and employee["position"] != "maanager":
        bonus = employee["salary"]* employee["work_time"] / 100
        total_salary = employee["salary"] + bonus

print(employee["name"], "have total salary ",total_salary)
print(50*"-")

#First Number
first_numbers = [9, 7, 10, 7, 10]
total_nilai = sum(first_numbers)
print("Total nilainya adalah ",total_nilai)

#Nilai Maksimum
nilai_max = max(first_numbers)
print("Nilai maksimumnya adalah ",nilai_max)

#Nilai Minimum
nilai_min = min(first_numbers)
print("Nilai Minimumnya adalah ",nilai_min)

print(50*"-")

#Menemukan angka yang bisa dibagi  2
total_angka = 0
for number in first_numbers:
    if number % 2 == 0:
        total_angka += 1
print("Total angka dalam data yang bisa dibagi dua adalah ",total_angka)

#Mengkali 2 baris ganjil dan menambah 4 baris genap
for i in range(len(first_numbers)):
    if i % 2 == 0:
        first_numbers[i] *= 2
    else:
        first_numbers[i] += 4
print("Hasil setelah bari ganjil dikasi 2 dan baris genap ditambah 4 = ",first_numbers)

first_numbers = [9, 7, 10, 7, 10]
muncul = {}
for number in first_numbers:
    if number in muncul:
        muncul[number] += 1
    else:
        muncul[number]=1
for number, kemunculan in muncul.items():
    if kemunculan > 1:
        print(f"Angka {number} muncul sebanyak {kemunculan} kali")

#Second Numbers
second_numbers = [2, 3]
result = []

#perkalian silang
for number in second_numbers:
    list = []
    for i in range(len(first_numbers)):
        list.append(number*first_numbers[i])
    result.append(list)
print("Result =",result)

#penjumlahan sesuai posisi
result_jumlah = []
for i in range(len(first_numbers)):
    total = 0;
    for j in range(len(result)):
        total += result[j][i]
    result_jumlah.append(total)
print("Result =",result_jumlah)
print(50*"-")

def palindrome(word):
    return word == word[::-1]
kata = str(input("Masukkan kata : "))
print(palindrome(kata))
