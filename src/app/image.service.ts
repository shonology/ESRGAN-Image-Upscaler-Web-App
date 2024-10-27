import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ImageService {

  constructor(private http: HttpClient) { }

  uploadImage(image: File) {
    const formData = new FormData();
    formData.append('image', image, image.name);

    return this.http.post('http://localhost:5000/upscale', formData, { responseType: 'blob' });
  }
}
