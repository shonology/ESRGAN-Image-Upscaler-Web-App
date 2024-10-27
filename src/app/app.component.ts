import { Component, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  selectedFile: File | null = null;

  @ViewChild('downloadLink') downloadLink!: ElementRef;

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      console.log('File selected:', this.selectedFile.name);
    }
  }

  onUpload() {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('image', this.selectedFile, this.selectedFile.name);
      console.log('Uploading file:', this.selectedFile.name);

      this.http.post('http://127.0.0.1:5000/upscale', formData, { responseType: 'blob' }).subscribe(response => {
        console.log('Response received');
        const blob = new Blob([response], { type: 'image/png' });
        const url = window.URL.createObjectURL(blob);
        const a = this.downloadLink.nativeElement;
        a.href = url;
        a.download = 'output.png';
        a.style.display = 'block';
        a.textContent = 'Download Processed Image';
      }, error => {
        console.error('Error during file upload:', error);
      });
    }
  }
}
