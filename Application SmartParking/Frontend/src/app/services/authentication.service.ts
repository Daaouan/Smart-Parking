import { Injectable } from '@angular/core';
import { Observable, of, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private users=[
    {username:"admin", password:"20232023"},
  ]

  authenticatedUser:any;
  
  constructor() {}

  public login(username: string, password: string){
    let appUser= this.users.find(u => u.username==username);
    if(!appUser){
      return throwError(()=>new Error("Bad credentials"));
    }
    if(appUser.password!=password){
      return throwError(()=>new Error("Bad credentials"));
    }
    return of(appUser);
  } 

  public authenticateUser(appUser: any):Observable<boolean>{
    this.authenticatedUser=appUser;
    localStorage.setItem("authUser", JSON.stringify({username:appUser.username, jwt:"TOKEN"}));
    return of(true);
  }

  public isAuthenticated(){
    return this.authenticatedUser!=undefined;
  }

  public logout(): Observable<boolean>{
    this.authenticatedUser=undefined;
    localStorage.removeItem("authUser");
    return of(true);
  }
}
