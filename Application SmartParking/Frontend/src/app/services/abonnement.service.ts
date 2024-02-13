import { Injectable } from '@angular/core';
import { WebRequestService } from './web-request-service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AbonnementService {
  constructor(private _webReqService: WebRequestService) { }

  createAbonnement(jsonData: any) : Observable<any>{
    return this._webReqService.post('abonnement', jsonData) 
  }

  getAbonnement(){
    return this._webReqService.get('abonnement')  ;
  }
  
  getOneAbonnement(id: string){
    return this._webReqService.get(`abonnement/${id}`);
  }

  editAbonnement(id: string, jsonData: any){
    return this._webReqService.put(`abonnement/${id}`, jsonData)  ;
  }

  deleteAbonnement(id: string){
    return this._webReqService.delete(`abonnement/${id}`)
  }
}
