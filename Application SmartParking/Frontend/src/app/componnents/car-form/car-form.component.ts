import { Component ,Inject} from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { CarService } from 'src/app/services/car.service';
import { DialogRef } from '@angular/cdk/dialog';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-car-form',
  templateUrl: './car-form.component.html',
  styleUrls: ['./car-form.component.css']
})
export class CarFormComponent {
  CarForm: FormGroup;
  errorMsg: any;
  loading: boolean = false; // Flag variable
  car: any;

  constructor(
    private _car: CarService,
    private _fb: FormBuilder,
    private _dialogRef: DialogRef<CarFormComponent>,
    private _router: Router,
    @Inject(MAT_DIALOG_DATA) public data: any,
  ) {
    this.CarForm = this._fb.group({
      clientName: this._fb.control(""),
      email: this._fb.control(""),
      matricule: this._fb.control(""),
    })
  }

  ngOnInit(): void {
      this.CarForm.patchValue(this.data);
  }

  OnSave() {
    if (this.CarForm.valid) {
      const jsonData = {
        clientName: this.CarForm.value.clientName,
        email: this.CarForm.value.email,
        matricule: this.CarForm.value.matricule,
      };
  
      this.loading = true;
  
      if (this.data) {
        this._car.editCar(this.data._id, jsonData).subscribe(() => {
          this._router.navigate(['/']);
        });
      } else {
        this._car.createCar(jsonData).subscribe(
          (response: any) => {
            console.log(response);
            const savedData = {
              clientName: this.CarForm.value.clientName,
              email: this.CarForm.value.email,
              matricule: this.CarForm.value.matricule,
            };
            console.log(savedData);
            this.loading = false;
            this._dialogRef.close();
            this._router.navigate(['/']);
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
