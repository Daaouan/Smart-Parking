import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { DomSanitizer } from '@angular/platform-browser';
import { VideoService } from 'src/app/services/video.service';
import { CarFormComponent } from '../car-form/car-form.component';
import { CarsListComponent } from '../cars-list/cars-list.component';
import { AbonnementFormComponent } from '../abonnement-form/abonnement-form.component';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-first-page',
  templateUrl: './first-page.component.html',
  styleUrls: ['./first-page.component.css']
})
export class FirstPageComponent implements OnInit{
  title = 'Frontend';
  videoSrc: any;

  constructor(
    public dialog: MatDialog,
    private videoService: VideoService,
    private sanitizer: DomSanitizer,
    private authService: AuthenticationService,
    private router: Router
  ) { }

  //peut etre supprimer
  ngOnInit(): void {
    this.loadVideoStream();
  }

  loadVideoStream(): void {
    this.videoService.getVideoStream().subscribe(
      (data: any) => {
        this.videoSrc = this.sanitizer.bypassSecurityTrustUrl(URL.createObjectURL(data));
      },
      error => {
        console.error('Error loading video stream:', error);
      }
    );
  }

  openCarDialog(enterAnimationDuration: string, exitAnimationDuration: string): void {
    this.dialog.open(CarFormComponent, {
      width: '40%',
      height: '75%',
      enterAnimationDuration,
      exitAnimationDuration,
      disableClose: false,
    });
  }
  editCarDialoge(data: any, enterAnimationDuration: string, exitAnimationDuration: string) {
    this.dialog.open(CarFormComponent, {
      width: '40%',
      height: '75%',
      enterAnimationDuration,
      exitAnimationDuration,
      disableClose: false,
      data: data,
    });
  }
  openCarsListe(enterAnimationDuration: string, exitAnimationDuration: string): void {
    this.dialog.open(CarsListComponent, {
      width: '100%',
      height: '100%',
      enterAnimationDuration,
      exitAnimationDuration,
      disableClose: false,
    });
  }
  openAbonnementDialog(enterAnimationDuration: string, exitAnimationDuration: string): void {
    this.dialog.open(AbonnementFormComponent, {
      width: '40%',
      height: '74.5%',
      enterAnimationDuration,
      exitAnimationDuration,
      disableClose: false,
    });
  }

  logout(){
    this.authService.logout().subscribe({
      next:()=>{
        this.router.navigateByUrl("");
      }
    })
  }
}
