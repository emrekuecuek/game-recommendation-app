import { ServicesService, SearchType } from './../../services.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute , Router} from '@angular/router';
import { getLocaleWeekEndRange } from '@angular/common';

@Component({
  selector: 'app-basket',
  templateUrl: './basket.page.html',
  styleUrls: ['./basket.page.scss'],
})
export class BasketPage implements OnInit {

  data: any;
  items;
  mappeditems;
  

  constructor(private activatedRoute: ActivatedRoute, private gameService: ServicesService, private router: Router) { 
    this.activatedRoute.queryParams.subscribe(params => {
      if (this.router.getCurrentNavigation().extras.state) {
        this.data = this.router.getCurrentNavigation().extras.state.id;
      }
    });
  }


  ngOnInit() {
    this.items = this.gameService.getItems();

    //this.mappeditems = this.items.map(val => this.gameService.getDetails(val))
    

  }


  removeItemFromList(item){
    let index = this.items.indexOf(item);

    if(index > -1){
      this.items.splice(index, 1);
    }

  }


sendgames() {

  let postData = {
    "gamename": "oyun"
   
    
}
  this.gameService.sendPostRequest(this.items)
  window.alert('Your product has been added to the cart!');
}
  



}
