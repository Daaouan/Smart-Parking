import { Component ,Inject, OnInit} from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AbonnementService } from 'src/app/services/abonnement.service';
import { DialogRef } from '@angular/cdk/dialog';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { CarService } from 'src/app/services/car.service';

@Component({
  selector: 'app-abonnement-form',
  templateUrl: './abonnement-form.component.html',
  styleUrls: ['./abonnement-form.component.css']
})
export class AbonnementFormComponent{
  AbonnementForm: FormGroup;
  errorMsg: any;
  loading: boolean = false; // Flag variable
  pickerStart: any;
  pickerEnd: any;
  abonnement: any;
  cars: any;

  constructor(
    private _abonnement: AbonnementService,
    private _car: CarService,
    private _fb: FormBuilder,
    private _dialogRef: DialogRef<AbonnementFormComponent>,
    private _router: Router,
    @Inject(MAT_DIALOG_DATA) public data: any,
  ) {
    this.AbonnementForm = this._fb.group({
      start_date: this._fb.control(""),
      end_date: this._fb.control(""),
      car: this._fb.control(""),
    })
  }

  ngOnInit(): void {
      this.AbonnementForm.patchValue(this.data);

      this._car.getCar().subscribe((cars: any) =>{
        this.cars = cars;
        console.log(cars);
      })
  }

  OnSave() {
    if (this.AbonnementForm.valid) {
      const jsonData = {
        start_date: this.AbonnementForm.value.start_date,
        end_date: this.AbonnementForm.value.end_date,
        car: this.AbonnementForm.value.car,
      };
  
      this.loading = true;
  
      if (this.data) {
        this._abonnement.editAbonnement(this.data.id, jsonData).subscribe(() => {
          this._dialogRef.close();
        });
      } else {
        this._abonnement.createAbonnement(jsonData).subscribe(
          (response: any) => {
            console.log(response);
            const savedData = {
              start_date: this.AbonnementForm.value.start_date,
              end_date: this.AbonnementForm.value.end_date,
              car: this.AbonnementForm.value.car,
            };
            console.log(savedData);
            this.loading = false;
            this._dialogRef.close();
          },
          (error: any) => {
            console.error(error);
            this.loading = false;
          }
        );
      }
    }
  } 
}
