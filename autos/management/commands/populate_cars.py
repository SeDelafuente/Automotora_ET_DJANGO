import os
from django.core.management.base import BaseCommand
from autos.models import Car

class Command(BaseCommand):
    help = 'Populate the database with car data'

    def handle(self, *args, **kwargs):
        cars = [
            {
                'brand': 'Toyota',
                'model': 'Corolla',
                'year': 2020,
                'price': 15000000,
                'image': 'img/toyota_corolla.jpg',
                'description': 'Un sedán confiable y eficiente en combustible.'
            },
            {
                'brand': 'Honda',
                'model': 'Civic',
                'year': 2019,
                'price': 13000000,
                'image': 'img/honda_civic.jpg',
                'description': 'Un coche compacto con un estilo deportivo.'
            },
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': 2021,
                'price': 25000000,
                'image': 'img/ford_mustang.jpg',
                'description': 'Un clásico coche deportivo americano.'
            },
            {
                'brand': 'Chevrolet',
                'model': 'Camaro',
                'year': 2021,
                'price': 28000000,
                'image': 'img/chevrolet_camaro.jpg',
                'description': 'Un coche deportivo con gran rendimiento.'
            },
            {
                'brand': 'BMW',
                'model': 'Serie 3',
                'year': 2020,
                'price': 32000000,
                'image': 'img/bmw_serie3.jpg',
                'description': 'Un sedán de lujo con tecnología avanzada.'
            },
            {
                'brand': 'Audi',
                'model': 'A4',
                'year': 2020,
                'price': 30000000,
                'image': 'img/audi_a4.jpg',
                'description': 'Un coche de lujo con excelente rendimiento.'
            },
            {
                'brand': 'Mercedes-Benz',
                'model': 'Clase C',
                'year': 2021,
                'price': 35000000,
                'image': 'img/mercedes_clasec.jpg',
                'description': 'Un coche de lujo con características premium.'
            },
            {
                'brand': 'Volkswagen',
                'model': 'Golf',
                'year': 2019,
                'price': 18000000,
                'image': 'img/volkswagen_golf.jpg',
                'description': 'Un hatchback confiable y eficiente.'
            },
            {
                'brand': 'Nissan',
                'model': 'Altima',
                'year': 2020,
                'price': 17000000,
                'image': 'img/nissan_altima.jpg',
                'description': 'Un sedán cómodo y espacioso.'
            },
            {
                'brand': 'Mazda',
                'model': 'Mazda3',
                'year': 2019,
                'price': 16000000,
                'image': 'img/mazda_mazda3.jpg',
                'description': 'Un coche compacto con buen rendimiento.'
            },
            {
                'brand': 'Hyundai',
                'model': 'Elantra',
                'year': 2020,
                'price': 14000000,
                'image': 'img/hyundai_elantra.jpg',
                'description': 'Un sedán compacto y eficiente.'
            },
            {
                'brand': 'Kia',
                'model': 'Rio',
                'year': 2019,
                'price': 12000000,
                'image': 'img/kia_rio.jpg',
                'description': 'Un coche económico y confiable.'
            },
            {
                'brand': 'Subaru',
                'model': 'Impreza',
                'year': 2020,
                'price': 19000000,
                'image': 'img/subaru_impreza.jpg',
                'description': 'Un coche con tracción en las cuatro ruedas y buen rendimiento.'
            },
        ]

        for car_data in cars:
            car, created = Car.objects.get_or_create(
                brand=car_data['brand'],
                model=car_data['model'],
                year=car_data['year'],
                defaults={
                    'price': car_data['price'],
                    'image': car_data['image'],
                    'description': car_data['description'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {car}'))
            else:
                self.stdout.write(self.style.WARNING(f'{car} already exists'))
