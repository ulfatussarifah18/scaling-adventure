class _jarak():
    def __init__(self, nama, tmpt_lahir, tgl_lahir, alamat, hobi, cita_cita, status, gender, jarak, wajah,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.alamat = alamat
        self.hobi = hobi
        self.cita_cita = cita_cita
        self.status = status
        self.gender = gender
        self.jarak = jarak
        self.wajah = wajah
        
    def _set (self, nama, tmpt_lahir, tgl_lahir, alamat, hobi, cita_cita, status, gender, jarak, wajah,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.alamat = alamat
        self.hobi = hobi
        self.cita_cita = cita_cita
        self.status = status
        self.gender = gender
        self.jarak = jarak
        self.wajah = wajah

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tmpt_lahir + ', ' +  self.tgl_lahir)
        print('Alamat  :'+ self.alamat)
        print('hobi&cita-cita  :' + self.hobi + ', ' + self.cita_cita)
        print('status saya  :' + self.status)
        if self.gender in ['L', 'l']:
            gender = 'Perempuan'
        else:
            gender = 'laki-laki'
        print('Gender      :' + gender)

        if self.jarak >40:
            print('jarak dari rumah ke kampus jauh')
        else:
            if self.jarak >35:
                print('jarak dari rumah ke kampus lumayan dekat')
            else:
                if self.jarak <35:
                    print('jarak dari rumah dekat')
        if self.wajah <1-6:
           print('lebar wajah gak ideal')
        else:
           if self.wajah <1-4:
              print('lebar wajah ideal')
           else:
              if self.wajah >1-4:
              	print('lebar wajah gak semupurna')
           	

print('=============================================================')
print('    \t PROGRAM CEK JARAK DAN LEBAR WAJAH    ')
print('=============================================================')

nama      = input('Nama lengkap        :')
tmpt_lahir = input('Tempat lahir        :')
tgl_lahir  = input('Tanggal lahir       :')
alamat = input('Alamat              :')
hobi = input('Hobi                :')
cita_cita = input('Cita-Cita           :')
status = input('Status              :')
gender     = input('Gender L/P          :')
jarak = int(input('Masukan jarak       :'))
wajah = float(input('Masukan ukuran wajah:'))

print('=============================================================')

proses = _jarak(nama,tmpt_lahir,tgl_lahir,alamat,hobi,cita_cita,status,gender,jarak,wajah,)
print (proses._get())

print('=============================================================')
print('    \tSEKIAN TERIMA KASIH     ')
print('=============================================================')