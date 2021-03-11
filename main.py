from Customer import Customer

pesho = Customer("Pesho")
pesho.check_catalogue()
pesho.rentacar_hours("PB5079TT", 5)
pesho.rentacar_day("CB4078BM")
pesho.rentacar_week("PB9189PC")
pesho.rentacar_hours("PB9189PC", 10)  # You can't rent a car which is already rented
pesho.rentacar_day("PB9999AH")  # You also can't rent a car which isn't in the catalogue, of course
pesho.rentacar_hours("PB0168MX", 3)  # Pesho's fourth car
pesho.checkout()

drago = Customer("Drago")
drago.check_catalogue()  # The cars rented by Pesho are no longer in the catalogue
drago.rentacar_hours("PA5460AB", 4)
drago.rentacar_hours("EB6633AH", 4)
drago.checkout()