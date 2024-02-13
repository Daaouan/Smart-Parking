import { DialogRef } from '@angular/cdk/dialog';
import { Component } from '@angular/core';
import { CarService } from 'src/app/services/car.service';

@Component({
  selector: 'app-cars-list',
  templateUrl: './cars-list.component.html',
  styleUrls: ['./cars-list.component.css']
})
export class CarsListComponent {
  cars: any;

  constructor(private _car: CarService,
    public _dialogRef: DialogRef){}

  ngOnInit(){
    this._car.getCar().subscribe((cars: any) =>{
    this.cars = cars;
    console.log(cars);
  })
  }
}
