import sympy as sp

# Fungsi untuk komposisi f(g(x)) dan g(f(x))
def komposisi_f_g(f, g, x):
    return f.subs(x, g)

def komposisi_g_f(f, g, x):
    return g.subs(x, f)

# Fungsi untuk penjumlahan (f + g)(x)
def penjumlahan_f_g(f, g, x):
    return f + g

# Fungsi untuk menghitung invers dari fungsi
def invers(f, x):
    # Menyelesaikan persamaan f(y) = x untuk y
    y = sp.symbols('y')
    invers_f = sp.solve(f - x, y)
    return invers_f

# Fungsi untuk memasukkan fungsi dari input pengguna
def input_function():
    func = input("Masukkan fungsi (gunakan x untuk variabel dan '^' untuk pangkat, misal: x**2 + 3*x + 2): ")
    x = sp.symbols('x')
    func = sp.sympify(func)
    return func, x

# Main Program
def main():
    print("Program untuk menghitung Komposisi Fungsi, Penjumlahan Fungsi, dan Invers Fungsi.")
    
    # Masukkan fungsi f(x)
    print("\nMasukkan fungsi f(x):")
    f, x = input_function()
    
    # Masukkan fungsi g(x)
    print("\nMasukkan fungsi g(x):")
    g, x = input_function()
    
    # Hitung komposisi f(g(x)) dan g(f(x))
    fg = komposisi_f_g(f, g, x)
    gf = komposisi_g_f(f, g, x)
    
    print(f"\nKomposisi f(g(x)) = {fg}")
    print(f"Komposisi g(f(x)) = {gf}")
    
    # Hitung penjumlahan (f + g)(x)
    fg_sum = penjumlahan_f_g(f, g, x)
    print(f"\nPenjumlahan (f + g)(x) = {fg_sum}")
    
    # Masukkan invers fungsi f(x)
    print("\nMasukkan invers fungsi f(x) jika ada (gunakan x untuk variabel dan '^' untuk pangkat, misal: x - 2):")
    invers_f = input_function()[0]
    
    # Hitung invers f(x)
    invers_result = invers(invers_f, x)
    print(f"\nInvers dari f(x) adalah: {invers_result}")

if __name__ == "__main__":
    main()
