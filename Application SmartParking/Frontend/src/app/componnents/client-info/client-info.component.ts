import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AbonnementService } from 'src/app/services/abonnement.service';
import { CarService } from 'src/app/services/car.service';
import { AbonnementFormComponent } from '../abonnement-form/abonnement-form.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-client-info',
  templateUrl: './client-info.component.html',
  styleUrls: ['./client-info.component.css']
})
export class ClientInfoComponent {
  car: any;
  abonnement: any;

  constructor(
    private route: ActivatedRoute,
    private _car: CarService,
    private _abonnement: AbonnementService,
    public dialog: MatDialog,
    )
   {}

  ngOnInit() {
    this.route.params.subscribe(params => {
      const id = params['id'];
      console.log(id);
      
      this._car.getOneCar(id).subscribe((car: any) =>{
        this.car = car;
        console.log(car);
      })
      
      this._abonnement.getOneAbonnement(id).subscribe((abonnement: any) =>{
        this.abonnement = abonnement;
        console.log(abonnement.car);
      })
    });
    
  }

  editAbonnementDialoge(data: any, enterAnimationDuration: string, exitAnimationDuration: string) {
    this.dialog.open(AbonnementFormComponent, {
      width: '40%',
      height: '74.5%',
      enterAnimationDuration,
      exitAnimationDuration,
      disableClose: false,
      data: data,
    });
  }

  printReport(): void{
    window.print();
  }
}
