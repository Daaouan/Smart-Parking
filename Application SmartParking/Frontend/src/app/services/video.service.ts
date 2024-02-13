import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VideoService {

  private apiUrl = 'http://127.0.0.1:8000/video_feed/';

  constructor(private http: HttpClient) { }

  getVideoStream(): Observable<Blob> {
    return this.http.get(this.apiUrl, { responseType: 'blob' });
  }
}
