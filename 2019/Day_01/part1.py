

def compute_fuel_needed_1(masses_file_name):
    masses = open(masses_file_name, 'r').read().split('\n')
    total_fuel = 0
    for mass in masses:
        total_fuel += compute_module_fuel(int(mass))

    return total_fuel

def compute_module_fuel(module_mass):
    return (module_mass // 3) - 2


def compute_fuel_needed_2(masses_file_name):
    masses = open(masses_file_name, 'r').read().split('\n')
    masses = map(int, masses)
    
    total_fuel = 0
    for mass in masses:
        module_fuel = compute_module_fuel(mass)
        fuel_fuel = compute_module_fuel(module_fuel)
        while fuel_fuel > 0:
            module_fuel += fuel_fuel
            fuel_fuel = compute_module_fuel(fuel_fuel)
        total_fuel += module_fuel

    return total_fuel

print(compute_fuel_needed_2("module_masses.txt"))
