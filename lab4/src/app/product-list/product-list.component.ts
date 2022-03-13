import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = products;

  

  share() {
    window.open( "https://wa.me/87082463102/?text=https://stackblitz.com/edit/angular-edbzp8?file=src%2Fapp%2Fproduct-list%2Fproduct-list.component.ts", "_blank");
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/