s, i, f = 'asep', 123, 12.0

st, igr, flt = type(s), type(i), type(f)

if st == str and igr == int and flt == float:
    print("Tipe input Valid")
else:
    print('Tipe input tidak valid')