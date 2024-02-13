import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarFormComponent } from './componnents/car-form/car-form.component';
import { EntryTableComponent } from './componnents/entry-table/entry-table.component';
import { OutTableComponent } from './componnents/out-table/out-table.component';
import { AbonnementFormComponent } from './componnents/abonnement-form/abonnement-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { HttpClientModule } from '@angular/common/http';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatNativeDateModule} from '@angular/material/core';
import { CarsListComponent } from './componnents/cars-list/cars-list.component';
import {MatSelectModule} from '@angular/material/select';
import { ClientInfoComponent } from './componnents/client-info/client-info.component';
import { FirstPageComponent } from './componnents/first-page/first-page.component';
import { LoginComponent } from './componnents/login/login.component';

@NgModule({
  declarations: [
    AppComponent,
    CarFormComponent,
    EntryTableComponent,
    OutTableComponent,
    AbonnementFormComponent,
    CarsListComponent,
    ClientInfoComponent,
    FirstPageComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule, 
    ReactiveFormsModule,
    HttpClientModule,
    MatDialogModule,
    MatFormFieldModule, 
    MatInputModule, 
    MatDatepickerModule, 
    MatNativeDateModule,
    MatSelectModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
