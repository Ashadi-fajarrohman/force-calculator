nama = 'AshadiFajarrohman'
program ='gaya'

print(f'program {program} oleh {nama}')

def hitung_gaya (massa, percepatan):
    gaya = massa * percepatan
    print(f'massa = {massa / 1}kg bergerak dengan percepatan = {percepatan / 1} m/s**')
    print(f'sehingga gaya = {gaya} newton')
    return massa * percepatan

# massa = 1
# percepatan =1
gaya = hitung_gaya(1, 5 )
gaya = hitung_gaya(1, 70)
gaya = hitung_gaya(3, 25)

print(f'massa = {massa/1}kg bergerak dengan percepatan = {percepatan/1}m/s**')
print(f'sehingga gaya = {gaya}newton')
