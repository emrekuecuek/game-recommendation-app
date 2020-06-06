import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

// değiştirilecek fields konacak 
export enum SearchType {
  all = '',
  movie = 'movie',
  series = 'series',
  episode = 'episode',
  //id= 'id',
  //screenshots = 'screenshots.*'
}
//





@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  items = [];
  //url = 'https://api-v3.igdb.com/games';
  //url = 'http://www.omdbapi.com/';
  url = 'https://api.rawg.io/api/';
  baskets: Observable<any>;
  baskets2=[];
  //apiKey = '99285A76A20DC1B5C3F4775FD24BB823'; // <-- Enter your own key here!
  //apiKey = '38ed9dca';
  //const headers = {'user-key' : '573798879e1cef13ab556c1cffb9419f'};
  //const headers = new HttpHeaders().set('user-key', '573798879e1cef13ab556c1cffb9419f')


  constructor(private http: HttpClient) { }

  searchData(title: string): Observable<any> {
    //const headers = new HttpHeaders({'Accept': 'application/json','user-key': '573798879e1cef13ab556c1cffb9419f'})
    //return this.http.get(`http://www.omdbapi.com/?s=${encodeURI(title)}&apikey=38ed9dca`).pipe(map(results => results['Search'])
    //return this.http.get(`${this.url}?s=${encodeURI(title)}&apikey=${this.apiKey}`).pipe(
     // map(results => results['Search'])
    return this.http.get(`${this.url}games?search=${encodeURI(title)}`).pipe(
        map(results => results['results'])
    );
  }


  getDetails(id) {
    return this.http.get(`${this.url}games/${id}`);
  }

  addToCart(product) {
    this.items.push(product);
  }

  getItems() {
    return this.items;
  }

  clearCart() {
    this.items = [];
    return this.items;
  }






  sendPostRequest(postData) {
   
  

  
      let headers = {
        'Content-Type': 'application/json'
       };

    return this.http.post<any>('http://127.0.0.1:5000/abd', postData ).subscribe(
    data  => {
    console.log("POST Request is successful ", data);
    },
    error  => {
    
    console.log("Error", error);
    
    }
    
    );


  }



  getResult() {
    return this.http.get('http://127.0.0.1:5000/resres');
  }

  


}



/**
 * apikey:99285A76A20DC1B5C3F4775FD24BB823
 */

