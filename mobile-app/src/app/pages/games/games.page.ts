import { ServicesService, SearchType } from './../../services.service';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-games',
  templateUrl: './games.page.html',
  styleUrls: ['./games.page.scss'],
})
export class GamesPage implements OnInit {

  results: Observable<any>;
  searchTerm: string = '';  // burası search buton için 
  showlist;
  model_res;
  

  constructor(private gameService: ServicesService) { }

  ngOnInit() {
    // this.gameService.getResult().subscribe(result => {
    //   this.showlist =  result['gamename'];
    //   this.model_res = this.showlist.map(val => {
        

    //   }
    //     this.gameService.searchData(val)) ;
    // });
    
  }

  searchChanged() {
    // Call our service function which returns an Observable
    this.results = this.gameService.searchData(this.searchTerm);
  }

result_to_show() {

  this.model_res = this.showlist.map(val => this.gameService.searchData(val)) ;
}
 

}
