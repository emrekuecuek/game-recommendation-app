import { ServicesService, SearchType } from './../../services.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Router, NavigationExtras } from '@angular/router';



@Component({
  selector: 'app-game-details',
  templateUrl: './game-details.page.html',
  styleUrls: ['./game-details.page.scss'],
})
export class GameDetailsPage implements OnInit {

  information = null;
  public basketarray= [];
  //information2 =null;
  constructor(private activatedRoute: ActivatedRoute, private gameService: ServicesService, private router: Router) { }


  ngOnInit() {
    let id = this.activatedRoute.snapshot.paramMap.get('id');
    
    this.gameService.getDetails(id).subscribe(result => {
      this.information = result;

    });

    
  }



  openDetailsWithState() {
    let id = this.activatedRoute.snapshot.paramMap.get('id');
    this.basketarray.push({id})
    let navigationExtras: NavigationExtras = {
      state: {
        id: this.activatedRoute.snapshot.paramMap.get('id')
      }
    };

    this.router.navigate(['basket'], navigationExtras);
  }

  addToCart() {
    let id = this.activatedRoute.snapshot.paramMap.get('id');
    //this.gameService.addToCart(id);
    this.gameService.getDetails(id).subscribe(result => {
      let information2 = result;
      this.gameService.addToCart(information2);
    });
    
    window.alert('Your product has been added to the cart!');
    }

}
