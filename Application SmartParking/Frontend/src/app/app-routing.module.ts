import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClientInfoComponent } from './componnents/client-info/client-info.component';
import { FirstPageComponent } from './componnents/first-page/first-page.component';
import { LoginComponent } from './componnents/login/login.component';
import { AuthenticationGuard } from './guards/authentication.guard';

const routes: Routes = [
  { path: '', component: LoginComponent},
  { path: 'parking', component: FirstPageComponent, canActivate: [AuthenticationGuard]},
  { path: 'clientInfo/:id', component: ClientInfoComponent , canActivate: [AuthenticationGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)], 
  exports: [RouterModule]
})
export class AppRoutingModule { }
