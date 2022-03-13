import { Component, OnInit,NgModule} from '@angular/core';
import { categories } from '../categories';
import { Category } from '../categories';
import { products } from '../products';
import {usbs} from '../usb';
import {sports} from '../sport';
import {beauties} from '../beauty';
import {LikeComponent} from '../like/like.component';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})


export class CategoryComponent implements OnInit {
  categories = categories;
  products = products;
  usbs = usbs;
  sports = sports;
  beauties = beauties;
  selectedHero?: Category;

  show  = false;
 

  constructor() { }

  ngOnInit(): void {
  }
  share() {
    window.open( "https://wa.me/87082463102/?text=https://stackblitz.com/edit/angular-edbzp8?file=src%2Fapp%2Fproduct-list%2Fproduct-list.component.ts", "_blank");
  }

  
  onSelect(category: Category): void {
    this.selectedHero = category;
  }
  isshow(){
    this.show = !this.show;
  }
  siu(){}



}