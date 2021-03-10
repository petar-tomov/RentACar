from Customer import Customer

pesho = Customer("Pesho")
pesho.print_cars()
pesho.rentacar_hours("PB5079TT", 5)
pesho.rentacar_day("CB4078BM")
pesho.rentacar_week("PB9189PC")
pesho.rentacar_hours("PB0168MX", 3)  # Pesho's fourth car
pesho.checkout()